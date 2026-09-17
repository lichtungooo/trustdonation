---
name: td-test
description: "Was in trustdonation getestet wird und was nicht. Die Regel: jede Liste und jede Regel aus der Definition bekommt einen Test. Vitest-Befehle, Testarten, die drei Tore, und was ein Test nicht leisten soll."
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

## Die drei Tore

Vor jeder Auslieferung, in dieser Reihenfolge. **Kein Tor wird uebersprungen.**

| Tor | Befehl | Was es sagt |
|---|---|---|
| **1 Typen** | `pnpm build` | die Formen stimmen |
| **2 Regeln** | `pnpm -r test` | die Listen stimmen |
| **3 Augenschein** | `pnpm dev:reference`, Port 5173 | es tut, was es soll |

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

## Die Grenze zum Protokoll pruefen

Ein Test, der noch fehlt und gebaut werden soll:

```bash
grep -rn "did:key\|Y\.Doc\|applyUpdate\|@web_of_trust" packages/td-* apps/trustdonation 2>/dev/null
```

Muss leer bleiben. Wir sprechen nie direkt mit dem Web of Trust, immer ueber `DataInterface` und Capabilities. Sonst bindet uns eine Protokollversion.

## Selbst-Pruefung

1. Hat jede neue Liste einen Test?
2. Hat jede Regel aus der Definition einen Test?
3. Prueft der Test die **ganze** Liste, nicht einen Eintrag?
4. Sagt der Testname die Regel?
5. Laufen alle drei Tore?

## Verwandt

- `docs/ARCHITEKTUR.md` Teil 7 (die sieben Qualitaetstore)
- `docs/NAEHTE.md` Abschnitt D
- Skills `td-definieren`, `td-ausliefern`, `td-update`
