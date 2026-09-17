# Zu dritt an trustdonation arbeiten

**Für Timo, Emil und Janosch. Und für Anton und Sebastian, die schon drin sind.**

Timos Frage: *"Wie könnten wir einen Workflow zu dritt aufbauen, dass wir alle an diesem trustdonation weiterarbeiten und parallel Module programmieren, und dass jeder weiß, was der andere auch tut?"*

Drei Menschen an einem Vorhaben brauchen drei Dinge: **jeder sein eigenes Stück**, **ein Ort für den Stand**, und **eine Stelle, an der Entscheidungen fallen**. Hier steht, wo die drei Dinge liegen und was heute schon trägt.

---

## Teil 1: Wo gearbeitet wird

Zwei Repos, und die Trennung ist wichtig.

| Repo | Was drin ist | Wer es anfasst |
|---|---|---|
| **`lichtungooo/real-life-stack`**, Zweig `trustdonation` | Der Code. Antons Stack plus unsere Pakete `td-core` und `td-ui`. | wer programmiert |
| **`lichtungooo/trustdonation`** | Das Fachliche: Konzept, Landingpage, Betrieb, Skills. Kein Anwendungscode. | alle |

**Die Regel dazwischen:** Was eine Stiftung betrifft, gehört ins zweite. Was ein Browser ausführt, ins erste.

### Antons Stack ist geliehen, nicht unser

`real-life-org/real-life-stack` gehört Anton. Unser Zweig ist eine Abzweigung, und wir schreiben dort **nie** hin. Was zu ihm zurück soll, geht als Pull Request, mit dem Anwendungsfall zuerst.

Jede Stelle, an der wir seinen Code ändern, heißt bei uns **Naht** und steht in `docs/NAEHTE.md` des Stack-Repos. Ein Werkzeug prüft, dass keine fehlt:

```bash
python td-tools/pruefen.py
```

Das ist keine Bürokratie. Es ist der Grund, warum wir Antons Verbesserungen weiter einspielen können, ohne dass etwas zerbricht.

---

## Teil 2: Jeder sein eigenes Stück

Drei Menschen, die dieselbe Datei ändern, verbringen ihren Abend mit Konflikten. Drei Menschen, die je eigene Dateien haben, merken voneinander nichts.

### Wie ein Modul aussieht

Ein Modul im Real Life Stack ist **Code**, keine Einstellung. Es steht im Register:

```ts
export const CORE_MODULES = [
  { id: "feed", label: "Feed", icon: Newspaper },
  { id: "kanban", label: "Kanban", icon: Columns3 },
  { id: "map", label: "Karte", icon: MapIcon },
  …
]
```

Eigene Module kommen additiv dazu:

```ts
setModuleRegistry(composeModules([CORE_MODULE_LAYER, UNSERE_MODULE]))
```

**Darin liegt die Arbeitsteilung.** Wer ein Modul baut, legt einen eigenen Ordner an und trägt eine Zeile ins Register ein. Drei Menschen treffen sich dann an genau einer Zeile statt in derselben Datei.

Der Skill `/td-modul` führt durch den Bau.

### Was heute nicht geht

Im Real Life Stack gilt: *"Ein Space ist KEINE Schicht. Das Register steht vor dem ersten Render fest."* Ein Modul entsteht durch Programmieren, Bauen und Ausliefern.

Die **Modulschmiede**, in der ein Mensch ohne Code ein Modul zusammenstellt, gibt es im Real Life Network (`20-repos/rln`), nicht hier. Wer ein Modul ohne Programmieren bauen will, baut es dort.

**Für die drei heißt das:** Programmieren im Stack, Ausprobieren im RLN. Wer eine Idee hat, kann sie im RLN in einer Stunde zeigen, statt sie im Stack in einem Tag zu bauen.

### Was jeder gut übernimmt

| | Stärke | Was dazu passt |
|---|---|---|
| **Timo** | Vision, Ansprache, was Stiftungen brauchen | Landingpage, Inhalte, welche Module es überhaupt geben soll |
| **Janosch** | UX, Pareto, freie-gemeinschaft.org | wie sich etwas anfühlt, Abläufe, Module mit eigener Oberfläche |
| **Emil** | (sagt er selbst) | ein eigenes Modul, das niemandem sonst gehört |

Die Aufteilung ist kein Gesetz. Sie soll nur verhindern, dass zwei dasselbe bauen.

---

## Teil 3: Wo der Stand steht

Die Frage *"was tut der andere gerade?"* hat drei Antworten, und alle drei sind schon da.

### 1. Das Board in der App selbst

**Wir bauen trustdonation mit trustdonation.** Die gemeinsame Gruppe im Web of Trust trägt das Kanban, an dem gearbeitet wird:

- **Was ansteht** · **Wer es macht** · **Was fertig ist**
- Jeder sieht in Sekunden, was die anderen verschoben haben
- Was klemmt, klemmt sichtbar

Das kostet nichts und bringt zweierlei: Ihr wisst voneinander, und ihr merkt als erste, wo die App hakt. Was euch stört, stört auch eine Stiftung.

Der Weg dorthin steht in [10-zusammen-testen.md](10-zusammen-testen.md).

### 2. Die Commit-Meldung

Jeder Commit im Stack-Repo erzählt, **was** sich geändert hat und **warum**, nicht nur wo. Wer nach zwei Wochen zurückkommt, liest die Meldung statt den Code.

Dazu gehört: Was schiefging, steht auch drin. Ein Fehler, den jemand aufgeschrieben hat, macht ein anderer nicht noch einmal.

### 3. Der Stand als Blatt

`memory/stand_trustdonation.md` hält den Faden: **Was steht · Was läuft · Was als Nächstes.** Am Ende jeder Arbeitsrunde gepflegt, mit Datum.

Wer neu dazukommt oder lange weg war, liest dieses eine Blatt.

---

## Teil 4: Wo Entscheidungen fallen

Drei Menschen treffen Entscheidungen, die die anderen betreffen. Dafür gibt es das **RFC-System** (`01-verein/`): ein Vorschlag, eine Frist, Einwände, dann gilt es.

**Wann ein RFC:** Wenn eine Entscheidung schwer zurückzunehmen ist oder alle bindet. Ein neues Modul braucht keinen. Ein anderes Datenmodell schon.

**Wann kein RFC:** Beim Programmieren. Wer im eigenen Modul arbeitet, entscheidet allein.

Für trustdonation gibt es zusätzlich `docs/ENTSCHEIDUNGEN.md` im Stack-Repo: E1 bis E9, jede mit Grund und Datum. Wer wissen will, warum etwas so ist, liest dort nach, statt zu fragen.

---

## Teil 5: Was jeder mitbekommt

### Die Skills

Im Repo liegen **fünfzehn Skills** als Marktplatz, den jeder in sein Claude Code holen kann:

```
/plugin marketplace add lichtungooo/trustdonation
/plugin install trustdonation-tools
/plugin install sprach-tools
```

Damit hat jeder dieselben Werkzeuge: `/td-definieren` bevor etwas Code wird, `/td-naht` bevor Antons Code angefasst wird, `/td-ausliefern` zum Ausliefern, `/klare-sprache` für jeden Text.

**Das ist der wichtigste Baustein für gemeinsames Arbeiten.** Nicht weil Werkzeuge klug sind, sondern weil drei Menschen mit denselben Werkzeugen dieselbe Sprache sprechen.

Wer einen Skill verbessert, verbessert ihn für alle: Änderungen entstehen in `plugins/trustdonation-tools/skills/`, dann `python scripts/skills-spiegeln.py`.

### Der Zugang zu Eli

Eli hat ein gemeinsames Gedächtnis über MCP. Zugang haben heute **Anton, Mathias, Sebastian und Timo**.

Bei **Emil und Janosch** steht der Zugang als eingeplant, ohne Vollzug. **Anton vergibt ihn**, er hat das Auth-System gebaut.

Was der Zugang bringt: In Erinnerungen suchen, neue speichern, Eli in den eigenen Ablauf einbinden. Wer ihn hat, weiß, was die anderen besprochen haben, ohne dass es jemand weitererzählt.

---

## Der Anfang, konkret

Für die erste gemeinsame Runde:

1. **Jeder installiert die Skills** (drei Zeilen, siehe oben)
2. **Jeder legt seine Identität an** und ihr verifiziert euch von Angesicht zu Angesicht
3. **Timo legt die Gruppe an**, lädt ein, importiert die Stiftungen hinein
4. **Das Kanban in dieser Gruppe wird euer Board.** Erste Spalte: was jeder als Nächstes anfasst
5. **Jeder nimmt sich ein eigenes Modul**, damit niemand in fremden Dateien arbeitet
6. **Timo fragt Anton** nach den MCP-Zugängen für Emil und Janosch

---

## Was noch fehlt

Ehrlich benannt, damit es niemanden überrascht:

| Was | Warum es zählt |
|---|---|
| **MCP-Zugänge** für Emil und Janosch | ohne sie bleibt das gemeinsame Gedächtnis bei zweien |
| **Ohne Anmeldung lesen** | eine Stiftung soll die Karte sehen, bevor sie zwölf Wörter aufschreibt. Steht als Frage an Anton in `docs/anwendungsfaelle/01-oeffentlich-lesen.md` |
| **Module ohne Code** | im Stack gibt es die Schmiede nicht. Im RLN schon |
| **Mehrere Relays gleichzeitig** | Antons Adapter nimmt eine Liste (`brokerUrls`), der Stack füllt sie mit einem Eintrag. Eine Frage an ihn, kein Umbau |
