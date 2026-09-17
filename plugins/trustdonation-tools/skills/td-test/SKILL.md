---
name: td-test
description: "Was in trustdonation getestet wird und was nicht. Die Regel: jede Liste und jede Regel aus der Definition bekommt einen Test. Vitest, die sechs Tore in pruefen.py, Zugang mit axe-core, und was ein Test nicht leisten soll."
---

# Testen

**Wir messen, was bricht, wenn es fehlt.** Nicht Abdeckung in Prozent, nicht Zeilenzahl.

## Die eine Regel

> **Jede Liste und jede Regel aus `docs/DEFINITION.md` bekommt einen Test.**

Listen sind die Stelle, an der Software auseinanderlaeuft. Antons beide Register sind aus genau dieser Not entstanden: Dieselbe Frage war an vier bis fuenf Stellen beantwortet, die Antworten liefen auseinander, und es fiel lautlos aus.

Eine Regel ohne Test ist eine Absichtserklaerung.

## Was einen Test braucht

| Sache | Warum |
|---|---|
| **Register-Zusammensetzung** | Core, App, Space in der richtigen Reihenfolge, additiv |
| **Konflikt bei doppelter Id** | muss abbrechen, nicht still gewinnen |
| **Fragment ueberschreibt kein Skalar** | kein Shadowing, weder still noch ausdruecklich |
| **Unbekannter Eintrag** | bleibt erhalten, wird nicht dargestellt, bricht nichts |
| **Rueckfall ohne Eintrag** | generische Darstellung statt leer |
| **Reihenfolge einer Liste** | was steht wo, und was faellt weg, wenn es leer ist |
| **Pruefung von Eingaben** | eine fehlerhafte Art verwirft nur sich selbst, nie die Liste |
| **Reine Rechnungen** | Matching-Gruende, Schluesselbildung, Farbskalen |

## Was keinen Test braucht

- Reines Aussehen ohne Regel dahinter. Dafuer ist der Augenschein da.
- Antons Code. Er hat eigene Tests, und wir pflegen sie nicht mit.
- Musterdaten. Sie aendern sich staendig und tragen keine Regel.
- Was ein Typ schon garantiert. TypeScript ist das erste Tor.

## Befehle

```bash
cd /d/Workspace/20-repos/rls-uebersicht

pnpm -r test                                   # alle Pakete
pnpm --filter @real-life-stack/toolkit test    # ein Paket
cd packages/toolkit && npx vitest run tests/space-kinds.test.ts   # eine Datei
cd packages/toolkit && npx vitest                                 # mitlaufend
```

Die Tests laufen mit **Vitest**. Sie liegen je Paket in `tests/`.

## Die Tore

Ein Befehl faehrt sie alle:

```bash
python td-tools/pruefen.py            # alles
python td-tools/pruefen.py --schnell  # ohne Bau und Tests, Sekunden
```

| Tor | Was es sagt | haelt auf? |
|---|---|---|
| **Typen** | `pnpm build` laeuft durch | ja |
| **Regeln** | alle Tests gruen | ja |
| **Naehte** | keine unbenannte Stelle in Antons Code | ja |
| **Grenze** | keine Protokoll-Aufrufe in unseren Paketen | ja |
| **Budget** | die Groesse bleibt im Rahmen | nein, warnt |
| **Durchgang** | die zwoelf Erwartungen aus dem Testplan | ja |
| **Gedaechtnis** | der Stand ist gepflegt | ja |

Rot haelt die Auslieferung auf, gelb warnt. Ein Werkzeug, das immer rot leuchtet, wird nach zwei Tagen ignoriert.

**Der Schnelllauf verdeckt Fehler.** Zwei eigene Fehler im Werkzeug fielen erst im vollen Lauf auf: `pnpm` liess sich auf Windows ohne `shutil.which` nicht starten, und die Pfaderkennung im Naht-Bericht verlangte einen Punkt im Dateinamen, weshalb `deploy/app/Dockerfile` als unbenannt galt. **Vor dem Ausliefern immer voll fahren.**

Dazu der Augenschein: `pnpm dev:reference` auf **Port 5173**, niemals ausweichen.

Ein gruener Build ohne gruene Tests sagt nichts ueber die Regeln, die wir geaendert haben.

## Wie ein guter Test hier aussieht

Nach Antons Muster: **der Name sagt die Regel**, nicht die Technik.

```ts
it("haengt Landingpage nur an, wenn der Space ein Netzwerk ist", () => {
  expect(spaceConfigSections({ isAdmin: true, canInvite: true, canTheme: true, isNetwork: true })
    .map((s) => s.id))
    .toEqual(["members", "invite", "theme", "modules", "netzwerk", "landing"])
})
```

Drei Dinge daran:

1. **Der Name ist ein Satz ueber die Regel.** Wer ihn liest, versteht die Regel, ohne den Code zu lesen.
2. **Die ganze Liste wird geprueft**, nicht ein einzelner Eintrag. `toEqual` auf das Ganze faengt auch, was faelschlich dazukommt.
3. **Ein Kommentar sagt warum**, wenn die Regel nicht offensichtlich ist. Antons Tests tun das durchgehend.

## Wenn ein Test von Anton fehlschlaegt

Das heisst, wir haben eine seiner Regeln geaendert. Das ist der schwerste Fall einer Naht.

1. **Verstehen, was er wollte.** `git log -p` auf die Testdatei.
2. **Ehrlich fragen:** Ist unsere Regel richtiger, oder haben wir nur erweitert und seine Erwartung mitgezogen? Meist Letzteres.
3. **In `docs/NAEHTE.md` Abschnitt D eintragen**, mit dieser Antwort.
4. **Den Haken suchen**, der zwei getrennte Testdateien erlaubt: seine fuer die Core-Schicht, unsere fuer unsere. Dann kollidiert nichts mehr.

## Die Schema-Pruefung

Vokabulare und Musterdaten werden maschinell geprueft, ohne dass jemand daran denkt:

```bash
cd packages/data-interface && npx vitest run tests/schema-validation.test.ts
```

AJV prueft jedes Beispiel unter `docs/spec/schemas/vocab/*/examples/valid/` gegen sein Schema. **Ein neues Vokabular bekommt mindestens ein gueltiges Beispiel**, sonst prueft die CI nichts.

## Der Durchgang als Test

Die pruefbaren Zeilen aus `docs/TESTPLAN.md` laufen als Playwright-Test:

```bash
cd apps/reference
npx playwright test --config playwright.trustdonation.config.ts
npx playwright test --config playwright.trustdonation.config.ts --headed   # zum Zusehen
```

Zwoelf Erwartungen in achtzehn Sekunden: Ankommen ohne Anmeldung, Ueberschrift, Zoomen, die fuenf Spaces im Umschalter, Netzwerke oben, eigene Bilder, Gliederung nach Arten, ein Space der Netzwerk und Projekt zugleich ist in beiden Abschnitten, die sechs Dialog-Bereiche, Landingpage nur fuer Netzwerke, die Modul-Reiter, die Karte.

**Eigene leichte Konfiguration**, nicht Antons: seine startet Relay, Profilverzeichnis und Vault fuer die Web-of-Trust-Tests. Unser Durchgang laeuft gegen die Musterdaten im Browser und braucht nichts davon. Sie liegt in `apps/reference/`, weil pnpm Abhaengigkeiten strikt ablegt und `@playwright/test` zu dieser App gehoert.

**Zwei Fallen beim Schreiben solcher Tests:**

1. **Die Arten-Abschnitte erscheinen erst, wenn ein Netzwerk aktiv ist.** Die Uebersicht kennt keine Arten. Ein Test, der sie sofort erwartet, meldet zwei Fehler, die keine sind.
2. **Das letzte Zahnrad im Menue zu nehmen ist bequem und falsch.** Es gehoert dem letzten Space. Der Test muss die Zeile ueber den Namen suchen **und den Dialogtitel mitpruefen**, sonst prueft er womoeglich den falschen Space und meldet trotzdem gruen.

Vorher selbst gebaut mit Chrome und CDP, dann verworfen: Playwright liegt im Repo, kann klicken und warten, und ist in jeder Hinsicht besser. Die CDP-Werkzeuge bleiben fuer das, was sie gut koennen (Startlast, Zugang).

## Zugang pruefen

Ob die App fuer alle bedienbar ist, misst ein eigenes Werkzeug:

```bash
pnpm --filter reference exec vite preview --port 4173 &
python td-tools/zugang.py                              # gegen die Vorschau
python td-tools/zugang.py https://trustdonation.org/app/
```

Es laesst **axe-core** ueber die laufende App laufen. axe findet nicht alles, was ein Mensch findet, aber es findet zuverlaessig, was Maschinen finden koennen: fehlende Beschriftungen, zu schwache Kontraste, Bilder ohne Text, eine kaputte Ueberschriften-Ordnung. Rueckgabe 1, wenn ein schwerer Fund dabei ist.

**Der erste Lauf am 17.09.2026 fand drei Verstoesse, zwei davon schwer:**

| Fund | Was er bedeutet |
|---|---|
| `button-name` | Der Hell-Dunkel-Umschalter hatte keinen Namen. Eine Vorlesehilfe las nur "Schaltflaeche". |
| `meta-viewport` | `user-scalable=no` schaltete das Zoomen ab. Das trifft jeden, der vergroessern muss, um zu lesen. |
| `page-has-heading-one` | Keine Ueberschrift erster Ordnung. Wer springt, fand keinen Anfang. |

Alle drei behoben. **Beim Beheben ist ein vierter aufgetaucht**, und das ist die Lehre: Die neue Ueberschrift kam zuerst in einen eigenen `header` und war damit ein zweiter gleichnamiger Bereich. axe meldete `landmark-unique` sofort. Sie gehoert **in** die vorhandene Leiste.

**Live pruefen lohnt getrennt:** Dort ist ein anderer Space aktiv, und Funde haengen an der Space-Farbe. Der aktive Reiter auf hellem Orange faellt lokal nicht auf.

## Die Grenze zum Protokoll pruefen

Das Tor `Grenze` in `pruefen.py` misst es bei jedem Lauf. Von Hand:

```bash
grep -rn "did:key\|Y\.Doc\|applyUpdate\|@web_of_trust" packages/td-* apps/trustdonation 2>/dev/null
```

Muss leer bleiben. Wir sprechen nie direkt mit dem Web of Trust, immer ueber `DataInterface` und Capabilities. Sonst bindet uns eine Protokollversion.

## Selbst-Pruefung

1. Hat jede neue Liste einen Test?
2. Hat jede Regel aus der Definition einen Test?
3. Prueft der Test die **ganze** Liste, nicht einen Eintrag?
4. Sagt der Testname die Regel?
5. Laufen alle sechs Tore? (`python td-tools/pruefen.py`, voll, nicht `--schnell`)

## Verwandt

- `docs/ARCHITEKTUR.md` Teil 7 (die Qualitaetstore)
- `docs/NAEHTE.md` Abschnitt D
- Skills `td-definieren`, `td-ausliefern`, `td-update`
