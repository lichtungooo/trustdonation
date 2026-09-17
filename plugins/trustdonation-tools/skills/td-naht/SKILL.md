---
name: td-naht
description: "Bevor du Code von Anton im Real Life Stack aenderst. Prueft, ob ein Erweiterungspunkt (Haken) reicht, zieht den Eingriff klein, traegt ihn in NAEHTE.md ein und formuliert den Wunsch an Anton. Fuer trustdonation und jede Arbeit im Fork lichtungooo/real-life-stack."
---

# Eine Naht setzen

Eine **Naht** ist eine Stelle, an der wir Antons Code aendern, weil kein Haken dafuer da ist. Naehte sind erlaubt. Unbenannte Naehte sind es nicht.

Dieser Skill greift, **bevor** eine Datei von Anton angefasst wird.

## Die vier Fragen, in dieser Reihenfolge

### 1. Gibt es einen Haken?

Meistens ja. Antons Erweiterungspunkte, geprueft am Code:

| Ich will | Haken | Wo |
|---|---|---|
| ein eigenes Modul | `composeModules([CORE, MEINE_SCHICHT])` + `setModuleRegistry` | `toolkit/src/lib/module-register.ts` |
| einen eigenen Item-Typ | `composeTypeManifest([CORE_TYPE_LAYER, MEINE_SCHICHT])` | `data-interface/src/type-manifest.ts` |
| das Aussehen eines Typs | Typ-Darstellung, an Manifest-Ids gehaengt | `toolkit/src/components/preview/type-presentation.tsx` |
| ein eigenes Symbol | `registerIcon` | `toolkit/src/lib/icons.ts` |
| eigene Musterdaten | Seed als Parameter: `new LocalConnector(seed)` | Connector-Konstruktor |
| eigene Space-Felder | `Group.data`, additiv | Spec 04 |
| eigene Item-Felder | eigenes Vokabular im `@context` | Spec 06 |
| kategorisieren ohne neuen Typ | Tags | Spec 07 |
| etwas, das je Instanz anders ist | `config.json`, Branding, `homeSpaceId` | Spec 11 |

Vorbild in seinem eigenen Code: `apps/reference/src/module-register.tsx` und `apps/reference/src/type-register.tsx`. Er hat den Weg vorgemacht.

**Haken gefunden? Dann ist es keine Naht. Fertig.**

### 2. Geht es in unserer App statt in seiner?

Alles, was in `apps/trustdonation` liegt, ist **unsere** Datei. Komposition, Routing, Musterdaten, Connector-Wahl gehoeren dorthin.

Wer etwas in `apps/reference` aendert, aendert Antons Referenz-App. Das ist fast immer der falsche Ort.

**In unserer App moeglich? Dann ist es keine Naht. Fertig.**

### 3. Laesst sich der Eingriff zusammenziehen?

Wenn es doch in seine Datei muss: **so wenig wie moeglich dort, so viel wie moeglich bei uns.**

Schlecht:

```text
383 Zeilen Oberflaeche direkt in seinem Dialog
```

Gut:

```text
ein Aufruf in seinem Dialog, der Inhalt in packages/td-ui
```

Der Unterschied bei einem Konflikt ist der zwischen einer Minute und einem Tag. Faustregel: **Eine Naht sollte unter zwanzig Zeilen bleiben.** Darueber lohnt es fast immer, den Inhalt in ein eigenes Paket zu ziehen.

### 4. Eintragen

In `docs/NAEHTE.md`, nach diesem Raster:

```markdown
### A<n>. <Kurzer Name>

| | |
|---|---|
| **Datei** | <Pfad> |
| **Umfang heute** | +<x> / -<y> |
| **Was wir tun** | <ein bis drei Saetze> |
| **Warum kein Haken** | <was fehlt> |
| **Risiko bei Update** | niedrig / mittel / hoch, mit Begruendung |
| **Wunsch an Anton** | <welcher Haken die Naht aufloest> |
| **Zwischenschritt** | <wie sie kleiner wird, bevor es den Haken gibt> |
```

Dann die Zahlen oben in der Datei nachziehen.

## Der Umfang wird gemessen, nicht geschaetzt

```bash
git diff --numstat <antons-stand>..trustdonation -- <datei>
git diff --numstat <antons-stand>..trustdonation   # alle
```

Antons Stand ist der Commit, auf den unser Branch aufsetzt. Am 17.09.2026: `f9c56fff`.

## Die drei Sonderfaelle

**Naht in einer Datendatei:** immer vermeidbar. Musterdaten gehen als Seed-Parameter an den Connector. Wer `packages/data-interface/data/*.json` aendert, hat den Seed-Weg noch nicht genommen.

**Naht in einer Testdatei:** der schwerste Fall. Er heisst, dass wir eine Regel von Anton geaendert haben. Der Eintrag braucht einen Satz dazu, ob unsere Regel wirklich richtiger ist. Oft lautet die ehrliche Antwort: nein, wir haben nur erweitert und seine Erwartung mitgezogen. Dann gehoert das so hingeschrieben.

**Naht in `docs/spec/`:** Das ist sein normativer Bereich. Dort schreiben wir nur, wenn ein Pull Request an ihn laeuft. Unsere eigenen Festlegungen stehen in `docs/DEFINITION.md`.

## Der Wunsch wird ein Pull Request

Jede Naht traegt einen Wunsch: *welchen Haken braeuchten wir, damit sie verschwindet?*

Der Wunsch wird ein PR an `real-life-org/real-life-stack`, und der beginnt mit dem **Anwendungsfall**, nicht mit der Loesung. Das ist Antons ausdruecklicher Wunsch, siehe `memory/feedback_pr_mit_use_case.md`.

Aufbau:

```markdown
## Warum

<Der Anwendungsfall in zwei bis vier Saetzen. Was ein Mensch tun will,
und was ihn heute daran hindert.>

## Was fehlt

<Der Haken, knapp. Am besten mit Verweis auf ein Muster, das er selbst
schon benutzt: "wie beim Modul-Register".>

## Vorschlag

<Signatur oder Skizze. Kurz.>
```

## Selbst-Pruefung

1. Habe ich alle neun Haken durchgesehen?
2. Waere es in `apps/trustdonation` moeglich?
3. Ist der Eingriff unter zwanzig Zeilen?
4. Steht der Eintrag in `NAEHTE.md`, mit Umfang aus `git diff --numstat`?
5. Steht ein Wunsch dabei?
6. Sind die Zahlen oben in `NAEHTE.md` nachgezogen?

## Verwandt

- `docs/ARCHITEKTUR.md` Teil 2 und Teil 4 im Repo
- `docs/NAEHTE.md` das Register selbst
- Skill `td-update` fuer den Tag, an dem Antons Aenderungen ankommen
- `memory/feedback_pr_mit_use_case.md`
