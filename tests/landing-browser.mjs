/**
 * Die Landingpage in einem echten Browser pruefen.
 *
 *   node tests/landing-browser.mjs
 *
 * ⚠ Warum dieses Blatt entstanden ist.
 *
 * Am 18.09.2026 haben drei AI-Agenten die Landingpage geprueft und
 * ueberarbeitet: 25 Befunde, 22 geschlossen. Alles davon war aus dem
 * Quelltext geschlossen — gelesen, gerechnet, abgeglichen. Timos Frage
 * danach war "hast du einen kompletten Test durchlaufen lassen?", und die
 * ehrliche Antwort war nein: **die Seite selbst war nie gelaufen.**
 *
 * Dieses Blatt drueckt die Knoepfe. Chrome ohne Fenster, gegen einen Server,
 * der die Seite genau so ausliefert wie der echte (siehe
 * docker-compose.yml: `landing` auf die Wurzel, `branding` daneben).
 *
 * **Die Gegenprobe gehoert dazu.** Ein Test, der vor und nach einer Behebung
 * gruen ist, beweist nichts. Auf dem Stand vor der Ueberarbeitung
 * (e96026a0) fallen neun dieser Pruefungen durch, jede zu einem Befund:
 *
 *   0 von 18 Stilknoepfen abgeschaltet, und ein Klick warf die Seite
 *   wirklich auf Deutsch zurueck                                  FND-0014
 *   Kontrast 1,06 zu 1 in den Luecken-Kaesten im Systemdunkel     FND-0008
 *   aria-label blieben deutsch                                    FND-0013
 *   og:locale blieb de_DE, die Kreislauf-Seite hatte keine        FND-0018
 *   76 oeffnende und 77 schliessende div                          FND-0015
 *
 * So pruefen:
 *
 *   git stash && node tests/landing-browser.mjs   (oder ein worktree)
 */
import { spawn } from 'node:child_process';
import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { existsSync, mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, extname, normalize, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

// tests/landing-browser.mjs -> die Wurzel des Repos
const WURZEL = dirname(dirname(fileURLToPath(import.meta.url)));
const PORT = Number(process.env['PORT'] ?? 8099);
const DEBUG_PORT = Number(process.env['DEBUG_PORT'] ?? 9333);
const SEITE = `http://127.0.0.1:${PORT}`;

/** Wo Chrome liegt. Kein festgenagelter Pfad: das haelt keine Maschine aus. */
function browserSuchen() {
  const kandidaten = [
    process.env['CHROME'],
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
    'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
    'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
    '/usr/bin/google-chrome',
    '/usr/bin/chromium',
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  ].filter(Boolean);

  for (const p of kandidaten) if (existsSync(p)) return p;

  throw new Error(
    'Kein Chrome gefunden. Den Pfad in CHROME setzen:\n' +
      '  CHROME="C:/Pfad/zu/chrome.exe" node tests/landing-browser.mjs',
  );
}

// ---------------------------------------------------------------------------
// Der Server, genau wie der echte
// ---------------------------------------------------------------------------

const TYPEN = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.webp': 'image/webp',
  '.woff2': 'font/woff2',
  '.ico': 'image/x-icon',
};

function serverStarten() {
  const server = createServer(async (req, res) => {
    // Nach docker-compose.yml: ./landing auf /, ./branding auf /branding.
    // Wer das anders aufsetzt, prueft eine Seite, die es nicht gibt.
    const roh = normalize(decodeURIComponent((req.url ?? '/').split('?')[0])).replace(
      /^[/\\]+/,
      '',
    );
    let ziel = roh.startsWith('branding') ? join(WURZEL, roh) : join(WURZEL, 'landing', roh);

    try {
      const s = await stat(ziel).catch(() => null);
      if (s?.isDirectory()) ziel = join(ziel, 'index.html');

      const inhalt = await readFile(ziel);
      res.writeHead(200, {
        'content-type': TYPEN[extname(ziel).toLowerCase()] ?? 'application/octet-stream',
        'cache-control': 'no-store',
      });
      res.end(inhalt);
    } catch {
      res.writeHead(404, { 'content-type': 'text/plain; charset=utf-8' });
      res.end(`nicht gefunden: ${req.url}`);
    }
  });

  return new Promise((ok) => server.listen(PORT, '127.0.0.1', () => ok(server)));
}

// ---------------------------------------------------------------------------
// CDP, so klein wie moeglich
// ---------------------------------------------------------------------------

class Cdp {
  constructor(ws) {
    this.ws = ws;
    this.id = 0;
    this.warten = new Map();
    this.ereignisse = [];
    ws.addEventListener('message', (e) => {
      const m = JSON.parse(e.data);
      if (m.id !== undefined && this.warten.has(m.id)) {
        const { ok, nein } = this.warten.get(m.id);
        this.warten.delete(m.id);
        m.error ? nein(new Error(JSON.stringify(m.error))) : ok(m.result);
      } else if (m.method) {
        this.ereignisse.push(m);
      }
    });
  }

  send(method, params = {}) {
    const id = ++this.id;
    return new Promise((ok, nein) => {
      this.warten.set(id, { ok, nein });
      this.ws.send(JSON.stringify({ id, method, params }));
      setTimeout(() => {
        if (this.warten.delete(id)) nein(new Error(`${method} antwortet nicht`));
      }, 30_000);
    });
  }

  async evaluate(ausdruck) {
    const r = await this.send('Runtime.evaluate', {
      expression: `(function(){${ausdruck}})()`,
      returnByValue: true,
      awaitPromise: true,
    });
    if (r.exceptionDetails) {
      throw new Error(r.exceptionDetails.exception?.description ?? 'Fehler in der Seite');
    }
    return r.result.value;
  }

  async warteAufLast() {
    for (let i = 0; i < 100; i += 1) {
      if (await this.evaluate('return document.readyState === "complete"')) return;
      await new Promise((r) => setTimeout(r, 100));
    }
    throw new Error('Die Seite wurde nicht fertig');
  }

  async taste(key, code) {
    for (const type of ['keyDown', 'keyUp']) {
      await this.send('Input.dispatchKeyEvent', { type, key, code, windowsVirtualKeyCode: 27 });
    }
  }
}

// ---------------------------------------------------------------------------

const ergebnisse = [];
let aktuell = '';

function pruefe(name, bedingung, gesehen = '') {
  ergebnisse.push({ gruppe: aktuell, name, ok: Boolean(bedingung), gesehen });
  process.stdout.write(
    `  ${bedingung ? 'ok   ' : 'NEIN '} ${name}${gesehen && !bedingung ? ` — ${gesehen}` : ''}\n`,
  );
}

function gruppe(name) {
  aktuell = name;
  process.stdout.write(`\n${name}\n`);
}

const warte = (ms) => new Promise((r) => setTimeout(r, ms));

// ---------------------------------------------------------------------------

async function main() {
  const chromePfad = browserSuchen();
  const server = await serverStarten();
  const profil = mkdtempSync(join(tmpdir(), 'landing-pruef-'));

  const chrome = spawn(
    chromePfad,
    [
      '--headless=new',
      `--remote-debugging-port=${DEBUG_PORT}`,
      `--user-data-dir=${profil}`,
      '--no-first-run',
      '--no-default-browser-check',
      '--disable-gpu',
      '--window-size=1280,900',
      'about:blank',
    ],
    { stdio: ['ignore', 'pipe', 'pipe'] },
  );

  const aufraeumen = () => {
    chrome.kill();
    server.close();
    // Chrome haelt das Profil noch einen Moment. Ein Rest im Temp-Ordner
    // darf keinen Lauf als gescheitert melden.
    try {
      rmSync(profil, { recursive: true, force: true, maxRetries: 5, retryDelay: 200 });
    } catch {
      /* raeumt das Betriebssystem selbst auf */
    }
  };

  try {
    let version = null;
    for (let i = 0; i < 60; i += 1) {
      try {
        const r = await fetch(`http://127.0.0.1:${DEBUG_PORT}/json/version`);
        if (r.ok) {
          version = await r.json();
          break;
        }
      } catch {
        /* noch nicht da */
      }
      await warte(250);
    }
    if (!version) throw new Error('Chrome antwortet nicht auf dem Debugger-Port');
    process.stdout.write(`${version.Browser}\nSeite: ${SEITE}\n`);

    const neu = await fetch(
      `http://127.0.0.1:${DEBUG_PORT}/json/new?${encodeURIComponent(SEITE)}`,
      { method: 'PUT' },
    ).then((r) => r.json());

    const ws = new WebSocket(neu.webSocketDebuggerUrl);
    await new Promise((ok, nein) => {
      ws.addEventListener('open', ok, { once: true });
      ws.addEventListener('error', () => nein(new Error('Kein Draht zum Blatt')), { once: true });
    });

    const cdp = new Cdp(ws);
    for (const bereich of ['Runtime', 'Page', 'Network', 'Log']) {
      await cdp.send(`${bereich}.enable`);
    }

    // -----------------------------------------------------------------------
    gruppe('1. Die Startseite laedt');

    await cdp.send('Page.navigate', { url: `${SEITE}/` });
    await cdp.warteAufLast();

    const fehlgeschlagen = cdp.ereignisse
      .filter((e) => e.method === 'Network.responseReceived' && e.params.response.status >= 400)
      .map((e) => `${e.params.response.status} ${e.params.response.url}`);
    pruefe('keine Anfrage scheitert', fehlgeschlagen.length === 0, fehlgeschlagen.join(', '));

    const konsole = cdp.ereignisse
      .filter((e) => e.method === 'Log.entryAdded' && e.params.entry.level === 'error')
      .map((e) => e.params.entry.text);
    pruefe('kein Fehler in der Konsole', konsole.length === 0, konsole.join(' | '));

    const langDe = await cdp.evaluate('return document.documentElement.lang');
    pruefe('die Sprache steht auf de', langDe === 'de', langDe);

    const titelDe = await cdp.evaluate('return document.title');
    pruefe('ein Titel steht da', titelDe.length > 10, titelDe);

    // -----------------------------------------------------------------------
    gruppe('2. Der Sprachwechsel (FND-0007, FND-0013, FND-0018)');

    await cdp.evaluate('spracheSetzen("en"); return true');
    await warte(300);

    const langEn = await cdp.evaluate('return document.documentElement.lang');
    pruefe('lang wechselt auf en', langEn === 'en', langEn);

    const ogLocale = await cdp.evaluate(
      'var m=document.querySelector(\'meta[property="og:locale"]\'); return m ? m.content : "(fehlt)"',
    );
    pruefe('og:locale wechselt mit', ogLocale.startsWith('en'), ogLocale);

    const ariaNav = await cdp.evaluate(
      'var n=document.querySelector("nav.nav-links"); return n ? n.getAttribute("aria-label") : "(fehlt)"',
    );
    pruefe('das aria-label der Navigation ist englisch', ariaNav === 'Main navigation', ariaNav);

    const ariaDiagramm = await cdp.evaluate(
      'var d=document.querySelector("svg.diagram"); return d ? d.getAttribute("aria-label") : "(fehlt)"',
    );
    pruefe(
      'das aria-label des Geflechts ist englisch',
      /network|trust/i.test(ariaDiagramm),
      ariaDiagramm,
    );

    const titelEn = await cdp.evaluate('return document.title');
    pruefe('der Titel wechselt mit', titelEn !== titelDe, titelEn);

    const rohe = await cdp.evaluate(
      'var t=document.body.innerText; return (t.match(/\\b[a-z]+\\.[a-z]+\\.[a-z]+\\b/g)||[]).slice(0,3).join(", ")',
    );
    pruefe('kein roher Schluessel steht im Text', rohe.length === 0, rohe);

    // -----------------------------------------------------------------------
    gruppe('3. Die Stilknoepfe auf English (FND-0014)');

    const stand = await cdp.evaluate(`
      var b = document.querySelectorAll("[data-stil]");
      var aus = 0;
      for (var i = 0; i < b.length; i++) if (b[i].disabled) aus++;
      return { gesamt: b.length, aus: aus };
    `);
    pruefe(
      'alle Stilknoepfe tragen disabled',
      stand.gesamt > 0 && stand.aus === stand.gesamt,
      `${stand.aus} von ${stand.gesamt}`,
    );

    // Der eigentliche Punkt des Befundes: Ein Klick darf nichts bewirken.
    await cdp.evaluate(`
      var b = document.querySelector('[data-stil]:not([data-stil="klar"])');
      if (b) b.click();
      return true;
    `);
    await warte(400);
    const nachKlick = await cdp.evaluate('return document.documentElement.lang');
    pruefe(
      'ein Klick wirft die Seite nicht auf Deutsch zurueck',
      nachKlick === 'en',
      `lang ist ${nachKlick}`,
    );

    // -----------------------------------------------------------------------
    gruppe('4. Ein Sprachstil wird wirklich geholt (FND-0016)');

    await cdp.evaluate('spracheSetzen("de"); stilSetzen("klar"); return true');
    await warte(300);

    /**
     * ⚠ Ein Schluessel, den der Stil wirklich ueberschreibt.
     *
     * Der erste Lauf prueste `hero.h1` und schlug fehl — zu Recht: Ein Stil
     * traegt 107 von 217 Schluesseln, `hero.h1` ist keiner davon, und was
     * fehlt faellt auf T.de zurueck. Das war ein Fehler im Test, nicht im
     * Code. `nav.ressourcen` steht in kindgerecht.json als "Schatzkiste".
     */
    const vorStil = await cdp.evaluate(
      'var e=document.querySelector(\'[data-t="nav.ressourcen"]\'); return e ? e.innerText.trim() : "(fehlt)"',
    );

    await cdp.evaluate('stilSetzen("kindgerecht"); return true');
    await warte(1200);

    const nachStil = await cdp.evaluate(
      'var e=document.querySelector(\'[data-t="nav.ressourcen"]\'); return e ? e.innerText.trim() : "(fehlt)"',
    );
    pruefe(
      'der Text aendert sich mit dem Stil',
      nachStil !== vorStil && nachStil.length > 0,
      `"${vorStil}" -> "${nachStil}"`,
    );

    pruefe(
      'die Stil-Datei kam mit 200',
      cdp.ereignisse.some(
        (e) =>
          e.method === 'Network.responseReceived' &&
          e.params.response.url.includes('/stile/kindgerecht.json') &&
          e.params.response.status === 200,
      ),
    );

    const marke = await cdp.evaluate(
      'var b=document.querySelector(\'[data-stil="kindgerecht"]\'); return b ? b.getAttribute("aria-checked") : "(fehlt)"',
    );
    pruefe('der gewaehlte Stil ist als gewaehlt markiert', marke === 'true', marke);

    // Zwei Klicks schnell hintereinander: Der Befund fragte genau danach.
    await cdp.evaluate('stilSetzen("schamanisch"); stilSetzen("marktschreier"); return true');
    await warte(1500);

    /**
     * ⚠ Gezaehlt wird der gewaehlte **Stil**, nicht der gewaehlte Knopf.
     *
     * Der erste Lauf verlangte genau einen markierten Knopf und schlug fehl.
     * Die Seite traegt 18 Stilknoepfe, jeden Stil zweimal: einmal im
     * Aufklappmenue, einmal im Burger. Zwei markierte Knoepfe fuer eine Wahl
     * sind richtig. Wieder ein Fehler im Test, nicht im Code.
     */
    const zwei = await cdp.evaluate(`
      var g = document.querySelectorAll('[data-stil][aria-checked="true"]');
      var stile = {};
      for (var i = 0; i < g.length; i++) stile[g[i].dataset.stil] = true;
      var e = document.querySelector('[data-t="nav.ressourcen"]');
      return { stile: Object.keys(stile), knoepfe: g.length, text: e ? e.innerText.trim() : "(fehlt)" };
    `);
    pruefe(
      'nach zwei schnellen Klicks ist genau ein Stil gewaehlt',
      zwei.stile.length === 1,
      `${zwei.stile.join(', ')} (${zwei.knoepfe} Knoepfe)`,
    );
    pruefe(
      'und der gewaehlte ist der zuletzt geklickte',
      zwei.stile[0] === 'marktschreier',
      zwei.stile.join(', '),
    );
    pruefe('und es steht Text da', zwei.text.length > 2, zwei.text);

    // -----------------------------------------------------------------------
    gruppe('5. Der Prototyp-Schluessel (FND-0011)');

    await cdp.evaluate('try { localStorage.setItem("wir-stil", "constructor") } catch(e) {} return true');
    await cdp.send('Page.navigate', { url: `${SEITE}/` });
    await cdp.warteAufLast();
    await warte(400);

    const proto = await cdp.evaluate(`
      var e = document.querySelector('[data-t="nav.ressourcen"]');
      var g = document.querySelectorAll('[data-stil][aria-checked="true"]');
      return {
        text: e ? e.innerText.trim() : "(fehlt)",
        gewaehlt: g.length ? g[0].dataset.stil : "(keiner)",
        anzeige: (document.getElementById("lang-label") || {}).textContent || "(kein Feld)"
      };
    `);
    pruefe(
      '"constructor" landet nicht als Stil in der Leiste',
      proto.gewaehlt === 'klar' || proto.gewaehlt === '(keiner)',
      `gewaehlt: ${proto.gewaehlt}, Anzeige: ${proto.anzeige}`,
    );
    pruefe('und der Text steht', proto.text.length > 2, proto.text);
    await cdp.evaluate('try { localStorage.removeItem("wir-stil") } catch(e) {} return true');

    // -----------------------------------------------------------------------
    gruppe('6. Escape gibt den Fokus zurueck (FND-0012, FND-0022)');

    await cdp.evaluate(`
      var k = document.querySelector(".has-menu > button");
      if (k) { k.focus(); k.click() }
      return true;
    `);
    await warte(200);
    await cdp.taste('Escape', 'Escape');
    await warte(300);

    const escape = await cdp.evaluate(`
      var k = document.querySelector(".has-menu > button");
      return {
        aufKnopf: document.activeElement === k,
        wo: document.activeElement === document.body ? "body" : (document.activeElement.tagName || "?"),
        offen: k ? k.getAttribute("aria-expanded") : "?"
      };
    `);
    pruefe('das Menue ist zu', escape.offen === 'false', `aria-expanded: ${escape.offen}`);
    pruefe('der Fokus liegt wieder auf dem Knopf', escape.aufKnopf, `Fokus auf: ${escape.wo}`);

    // -----------------------------------------------------------------------
    gruppe('7. Hell und Dunkel');

    const schema = await cdp.evaluate(`
      var vorher = document.documentElement.dataset.theme || "(nicht gesetzt)";
      schemaUmschalten();
      return { vorher: vorher, nachher: document.documentElement.dataset.theme || "(nicht gesetzt)" };
    `);
    pruefe(
      'der Schalter aendert das Schema',
      schema.vorher !== schema.nachher,
      `${schema.vorher} -> ${schema.nachher}`,
    );

    const gemerkt = await cdp.evaluate(
      'try { return localStorage.getItem("rls-theme") || "(nichts)" } catch(e) { return "(kein Zugriff)" }',
    );
    pruefe('und merkt sich die Wahl', gemerkt === schema.nachher, gemerkt);

    // -----------------------------------------------------------------------
    gruppe('8. Die Rechts-Seite (FND-0007, FND-0008, FND-0010)');

    await cdp.evaluate('try { localStorage.clear() } catch(e) {} return true');

    // Systemdunkel, ohne dass jemand den Schalter beruehrt hat: genau der
    // Fall aus FND-0008.
    await cdp.send('Emulation.setEmulatedMedia', {
      features: [{ name: 'prefers-color-scheme', value: 'dark' }],
    });
    await cdp.send('Page.navigate', { url: `${SEITE}/recht/` });
    await cdp.warteAufLast();
    await warte(300);

    const rechtLang = await cdp.evaluate('return document.documentElement.lang');
    pruefe('die Rechts-Seite bleibt deutsch', rechtLang === 'de', rechtLang);

    const kontrast = await cdp.evaluate(`
      function leuchte(c) {
        var m = c.match(/\\d+(\\.\\d+)?/g).slice(0, 3).map(Number);
        var k = m.map(function (v) {
          v = v / 255;
          return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
        });
        return 0.2126 * k[0] + 0.7152 * k[1] + 0.0722 * k[2];
      }
      var kasten = document.querySelector(".luecke");
      if (!kasten) return { anzahl: 0 };
      var s = getComputedStyle(kasten);
      var v = leuchte(s.color), h = leuchte(s.backgroundColor);
      var hell = Math.max(v, h), dunkel = Math.min(v, h);
      return {
        anzahl: document.querySelectorAll(".luecke").length,
        grund: s.backgroundColor,
        schrift: s.color,
        verhaeltnis: Math.round(((hell + 0.05) / (dunkel + 0.05)) * 100) / 100
      };
    `);
    pruefe('es gibt Luecken-Kaesten', kontrast.anzahl > 0, `${kontrast.anzahl}`);
    pruefe(
      'im Systemdunkel sind sie lesbar (mindestens 4.5 zu 1)',
      kontrast.verhaeltnis >= 4.5,
      `${kontrast.verhaeltnis} zu 1 (${kontrast.schrift} auf ${kontrast.grund})`,
    );
    /**
     * ⚠ Geprueft wird die Eigenschaft, nicht die Anzahl.
     *
     * Die erste Fassung verlangte mindestens vier Luecken-Kaesten. Als Timo
     * am 19.09.2026 drei Pflichtangaben nachreichte, fiel der Test — obwohl
     * genau das Fortschritt war. Eine Zahl, die mit der Arbeit sinkt, taugt
     * nicht als Probe.
     *
     * Was wirklich zaehlt: **Ein Kasten, der dasteht, sagt was fehlt.** Ein
     * leerer Kasten waere eine Luecke, die sich als Inhalt ausgibt.
     */
    const luecken = await cdp.evaluate(`
      var k = document.querySelectorAll(".luecke");
      var stumm = 0;
      for (var i = 0; i < k.length; i++) {
        if (!/fehlt|fehlen/i.test(k[i].innerText)) stumm++;
      }
      return { anzahl: k.length, stumm: stumm };
    `)
    pruefe(
      'jede verbliebene Luecke sagt, was fehlt',
      luecken.stumm === 0,
      `${luecken.anzahl} Kaesten, davon ${luecken.stumm} ohne Angabe`,
    );

    const robots = await cdp.evaluate(
      'var m=document.querySelector(\'meta[name="robots"]\'); return m ? m.content : "(fehlt)"',
    );
    pruefe('robots steht auf index, follow', robots.includes('index'), robots);

    // -----------------------------------------------------------------------
    gruppe('9. Der Weg zum Impressum (FND-0023)');

    await cdp.send('Emulation.setEmulatedMedia', { features: [] });
    await cdp.send('Page.navigate', { url: `${SEITE}/` });
    await cdp.warteAufLast();

    const wege = await cdp.evaluate(
      'return document.querySelectorAll(\'a[href*="/recht/"]\').length',
    );
    pruefe('die Startseite verweist auf das Impressum', wege >= 2, `${wege} Verweise`);

    await cdp.send('Page.navigate', { url: `${SEITE}/kreislauf/` });
    await cdp.warteAufLast();

    const wegeK = await cdp.evaluate(
      'return document.querySelectorAll(\'a[href*="/recht/"]\').length',
    );
    pruefe('die Kreislauf-Seite auch', wegeK >= 2, `${wegeK} Verweise`);

    const og = await cdp.evaluate(
      'return document.querySelectorAll(\'meta[property^="og:"]\').length',
    );
    pruefe('und traegt og-Angaben (FND-0018)', og >= 4, `${og} Angaben`);

    // -----------------------------------------------------------------------
    gruppe('10. Das ueberzaehlige div (FND-0015)');

    // Der Browser raeumt falsches Markup still auf. Darum der Rohtext.
    const divs = await cdp.evaluate(`
      return fetch("/kreislauf/").then(function (r) { return r.text() }).then(function (t) {
        return { auf: (t.match(/<div\\b/g) || []).length, zu: (t.match(/<\\/div>/g) || []).length };
      });
    `);
    pruefe('auf und zu stimmen ueberein', divs.auf === divs.zu, `${divs.auf} auf, ${divs.zu} zu`);

    // -----------------------------------------------------------------------
    const nein = ergebnisse.filter((e) => !e.ok);
    process.stdout.write(`\n${'-'.repeat(66)}\n`);
    process.stdout.write(
      `${ergebnisse.length - nein.length} von ${ergebnisse.length} Pruefungen bestanden.\n`,
    );
    if (nein.length > 0) {
      process.stdout.write('\nNicht bestanden:\n');
      for (const e of nein) process.stdout.write(`  ${e.gruppe} — ${e.name}: ${e.gesehen}\n`);
    }

    ws.close();
    return nein.length;
  } finally {
    aufraeumen();
  }
}

main()
  .then((anzahl) => process.exit(anzahl > 0 ? 1 : 0))
  .catch((e) => {
    process.stderr.write(`\nAbgebrochen: ${e.message}\n`);
    process.exit(2);
  });
