---
name: td-komponente
description: "Eine Oberflaechen-Komponente fuer trustdonation bauen. Zuerst pruefen, ob Antons Toolkit sie schon hat, sonst in packages/td-ui nach seinem Slot-Muster. Feld-Register statt Verzweigung, Dichte gehoert der Flaeche, Tests fuer Listen."
---

# Eine Komponente bauen

**Die teuerste Sache, die man hier machen kann, ist eine zweite Fassung von etwas, das schon da ist.** Darum steht die Suche vor dem Bau.

## 1. Gibt es sie schon?

Antons Toolkit ist gross. Nachsehen, in dieser Reihenfolge:

```bash
cat docs/spec/modules/shared-components.md      # die geteilten Bausteine
ls packages/toolkit/src/components/             # was es gibt
grep -rn "export function <Name>" packages/toolkit/src/ | head
```

Geteilte Bausteine, die Anton pflegt: Composer, Detail, Preview, FilterBar, FilterPill, CreateFab, ModulePanel, ModuleToolbar, Editor, AdaptivePanel, dazu die Item-Hooks.

**Gefunden? Benutzen.** Auch wenn sie nicht ganz passt: erst pruefen, ob eine Eigenschaft fehlt, die man ihr beibringen koennte (dann Skill `td-beitragen`), bevor eine zweite entsteht.

## 2. Wo sie hingehoert

| Was | Wohin |
|---|---|
| Etwas, das **jede** RLS-App braucht | Vorschlag an Anton, Skill `td-beitragen` |
| Etwas, das **trustdonation** braucht | `packages/td-ui` |
| Etwas, das **nur eine Flaeche** braucht | neben diese Flaeche, nicht ins Paket |
| Etwas **ohne Oberflaeche** (Regel, Pruefung, Rechnung) | `packages/td-core` |

Ein Baustein wandert erst ins Paket, wenn ihn die **zweite** Stelle braucht. Vorher ist er eine Vermutung.

## 3. Das Muster

Antons Komponenten folgen einem Aufbau, und wer davon abweicht, faellt auf:

1. **Slots statt Karten.** `preview`, `detail`, `footer` liefern **Inhalt** in eine geteilte Huelle. Das Karten-Markup gehoert der Flaeche, nicht dem Typ. Wer eine eigene Karte baut, hat zwei Karten, die auseinanderlaufen.
2. **Der Typ sagt *was*, die Flaeche sagt *wieviel*.** Dichte (`compact` / `comfortable`) und Rahmen (Karte, Panel, Zeile) steuert die Flaeche. Die Komponente entscheidet das nicht.
3. **Keine Verzweigung nach Typ oder Feldnamen.** Was ein Feld anzeigt, sagt das Feld-Register (`docs/DEFINITION.md` Teil 7). Ein `if (feld === "foerderrahmen")` ist der Anfang einer zweiten Liste.
4. **Ein unbekannter Eintrag faellt sichtbar zurueck**, nie leer, nie kaputt. Ein Feld ohne Darstellungs-Eintrag wird nach seiner `shape` gezeigt.
5. **Zwei Schichten.** Was die Komponente *bedeutet*, gehoert nach `td-core`; wie sie *aussieht*, nach `td-ui`.

## 4. Oberflaechen-Regeln aus der Spec

Sie stehen in `docs/spec/01-app-composition.md` und gelten auch fuer uns:

- **Eine Flaeche pro Ebene.** Content-Panel, Dialog, Notification. Gleichartige Flaechen werden nie gestapelt.
- **Das Content-Panel ist persistent** und bleibt beim Modul-Wechsel offen.
- **Dialoge ueberlagern, ersetzen nicht.** Ein Dialog ist nie eine zweite Sidebar.
- **Interrupts stehlen nie den Kontext.**
- **Verschachtelte Flows laufen ueber einen Back-Stack**, nie ueber eine zweite gleichartige Flaeche.
- **Schwebende Bedienelemente** liegen in der gemeinsamen Schutzzone (`PanelSafeArea`), nicht jedes fuer sich.

## 5. Aussehen

Farben, Rundung, Flaechen und Kontraste kommen aus dem **Space-Theme**, nie aus festen Werten. Ein Space setzt seine Primaerfarbe, Toenung, Rundung und Flaechen; die Komponente liest sie.

```ts
import { themeTokens, readRadius, readSurfaces, getSpacePrimaryColor } from "@real-life-stack/toolkit"
```

Eine feste Hex-Farbe in einer Komponente ist ein Fehler: In der naechsten Instanz ist sie falsch.

Hell und dunkel entscheidet der Mensch, nicht der Space.

## 6. Texte

Deutsch, echte Umlaute, keine Gedankenstriche, positiv formuliert. Skill `klare-sprache`.

**Bezeichner bleiben ASCII.** Werte, die in Daten landen (Arten-Ids, Feldnamen, Modul-Ids), tragen nie Umlaute: Alter Code faende alte Daten sonst nicht mehr. Die Umlaute stehen in den Anzeigenamen.

## 7. Tests

Nicht fuer jede Komponente, aber immer fuer:

1. **Listen und Register** (was erscheint, in welcher Reihenfolge, was bei Unbekanntem).
2. **Rueckfall-Verhalten** (kein Eintrag, fehlende Capability, leeres Feld).
3. **Regeln, die in einem Dokument stehen.** Was in `DEFINITION.md` als Regel steht, bekommt einen Test; sonst ist es eine Absichtserklaerung.

Storybook ist die zweite Pruefung: `packages/toolkit/src/**/*.stories.tsx` zeigt Antons Muster.

## 8. Selbst-Pruefung

1. Gesucht, ob es sie schon gibt.
2. Im richtigen Paket (`td-ui` fuer Oberflaeche, `td-core` fuer Regeln).
3. Kein Eingriff in Antons Pakete. Sonst: Skill `td-naht`.
4. Keine Verzweigung nach Typ oder Feldname.
5. Dichte und Rahmen kommen von der Flaeche.
6. Unbekanntes faellt sichtbar zurueck.
7. Farben aus dem Theme, keine festen Werte.
8. Bezeichner ASCII, Anzeigetexte mit Umlauten.
9. Tests fuer Listen und Rueckfaelle.

## Verwandt

- `docs/spec/modules/shared-components.md` die geteilten Bausteine
- `docs/spec/01-app-composition.md` Overlay-Ebenen und Modulflaeche
- `docs/DEFINITION.md` Teil 7 (Feld-Register)
- Skills `td-modul`, `td-definieren`, `td-test`, `klare-sprache`
