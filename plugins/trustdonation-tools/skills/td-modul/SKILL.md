---
name: td-modul
description: "Ein Space-Modul fuer trustdonation bauen. Ueber Antons Modul-Register als eigene Schicht, ohne Eingriff in seine Pakete. Registereintrag, Feld-Praesenz statt Typ-Verzweigung, Modul-Spec nach seinem Raster, Tests."
---

# Ein Modul bauen

Ein **Space Module** ist eine pro Space aktivierbare Oberflaeche. Es lebt im aktuellen Space, liest ueber Hooks und `DataInterface`, und besitzt keine Backend-Annahmen.

**Der wichtigste Satz vorweg:** Ein Modul wird ueber Antons Register **eingebracht**, nicht in seinen Code geschrieben. Wer beim Modulbau eine Datei in `packages/toolkit` oder `packages/data-interface` anfasst, ist auf dem falschen Weg.

## 1. Erst die Spec

Ein Modul bekommt eine Beschreibung, bevor es Code wird. Antons Raster liegt bereit: `docs/spec/modules/template.md`. Es beantwortet:

- **Zweck**: welches Problem im aktuellen Space?
- **Einordnung**: Space Module oder App-Shell-Flaeche? Welche Bausteine?
- **Datenmodell**: welche Projektionen liest es (Items, Relations, Confirmations, Groups)?
- **Capabilities**: was tut es, wenn eine fehlt?
- **Aktionen**: was kann ein Mensch tun, und was setzt das voraus?
- **Cross-Module**: wie spielt es mit anderen zusammen, ohne sie hart zu koppeln?
- **Nicht-Ziele**: was es ausdruecklich nicht definiert.

Unsere Module liegen als Spec in `docs/spec/modules/` nur dann, wenn sie an Anton gehen. Sonst in `docs/DEFINITION.md` als eigener Teil (Skill `td-definieren`).

## 2. Der Registereintrag

Das Modul-Register beantwortet die Frage *„was folgt daraus, dass ein Space dieses Modul fuehrt?"*, und zwar an **einer** Stelle.

| Feld | Zweck |
|---|---|
| `id` | stabile Identitaet; zugleich URL-Segment und Schluessel in `Group.data.modules` |
| `label` | Anzeigename in Tabs und Space-Dialog |
| `icon` | Modul-Icon |
| `enabledByDefault` | ob ein neuer Space es fuehrt |
| `fill` | `container` (Standard) oder `bleed` (randlos, wie die Karte) |
| `maxWidth` | Breite des Inhalts |
| `keepMounted` | im Baum halten statt abbauen, fuer teuren Aufbau (Karte: WebGL) |
| `panelFit` | `inset` (Standard) oder `overlay`, wenn die Flaeche selbst der Inhalt ist |
| `presents` | **welche Item-Felder das Modul darstellen kann** |
| `view` | die Flaeche selbst, von der App beigesteuert |

`presents` ist das wichtigste Feld und wird gern vergessen: Es sagt, welches Feld in diese Sicht fuehrt. Die Karte nennt `position`, der Kalender `start`. Ohne das bleibt ein Feld im Detail einfach Text.

## 3. Einbringen, nicht einbauen

In unserer App (`apps/trustdonation`), nach Antons Vorbild aus `apps/reference/src/module-register.tsx`:

```ts
import { composeModules, setModuleRegistry, CORE_MODULE_LAYER } from "@real-life-stack/toolkit"

const TD_MODULE_LAYER = {
  id: "trustdonation",
  definitions: [
    {
      id: "bedarfe",
      label: "Bedarfe",
      icon: HandHeart,
      enabledByDefault: false,
      fill: "container",
      presents: ["bis", "umfang"],
      view: BedarfeView,
    },
  ],
}

export const MODULE_REGISTRY = composeModules([CORE_MODULE_LAYER, TD_MODULE_LAYER])
setModuleRegistry(MODULE_REGISTRY)
```

Regeln aus Spec 01, die dabei gelten:

1. **Das Register ist die einzige Quelle.** Jede Flaeche, die Module aufzaehlt, leitet ihre Liste daraus ab. Eine zweite Liste ist ein Fehler.
2. **Eine vergebene `id` ist ein Konflikt** und bricht die Zusammensetzung ab. Kein Shadowing.
3. **Einmal zusammensetzen, dann unveraenderlich.** Vor dem ersten Render, dann eingefroren.
4. **Ein Space ist keine Registerschicht.** `Group.data.modules` ist eine **Auswahl**, kein Beitrag.
5. **Eine unbekannte `id` in `Group.data.modules` bleibt erhalten** und wird nicht dargestellt. Nie stillschweigend entfernen.
6. **Ein Eintrag ohne `view` degradiert sichtbar.** Ein Tab ohne Flaeche ist schlimmer als kein Tab.

## 4. Die Flaeche bauen

Sie liegt in `packages/td-ui` und wird von der App an die `id` gehaengt.

**Die eiserne Regel:** kein `if (type === ...)` im Modul. Ein Modul verzweigt ueber **Felder** und **Capabilities**, nie ueber den Item-Typ. Was ein Item ist, sagt das Typ-Register; was ein Modul zeigt, sagt die Feld-Praesenz.

Was das Modul mitbringt:

- **Die Steuerleiste** gehoert in den Kopf, ueber `ModuleToolbar`. Nicht `sticky` im Modul loesen: dann loest es jedes Modul anders.
- **Fehlende Capabilities** werden sichtbar oder still abgebaut, nie als Fehler.
- **Unbekannte Item-Typen** brechen nichts.
- **Bei `panelFit: "overlay"`** muss die Flaeche ihr eigenes Zentrum korrigieren: Was sie in den Blick nimmt, gehoert in die Mitte des **sichtbaren** Rests.

Geteilte Bausteine stehen in `docs/spec/modules/shared-components.md`: Composer, Detail, Preview, FilterBar, CreateFab, ModulePanel, Editor, Item-Hooks. **Erst dort nachsehen, bevor etwas Neues entsteht.**

## 5. Item-Typen, die das Modul braucht

Braucht das Modul einen eigenen Typ (`need`, `match`, `module`), kommt er ebenfalls als Schicht, nicht als Eingriff:

```ts
import { composeTypeManifest, CORE_TYPE_LAYER } from "@real-life-stack/data-interface"

const TD_TYPE_LAYER = {
  id: "trustdonation",
  definitions: [
    { id: "need", vocab: ["https://real-life-stack.org/vocab/need/v1"], relations: [...] },
  ],
}
export const TYPE_MANIFEST = composeTypeManifest([CORE_TYPE_LAYER, TD_TYPE_LAYER])
```

Manifest in `td-core` (UI-frei), Darstellung in `td-ui`. Zwei Schichten, eine Identitaetsquelle.

## 6. Tests

Mindestens:

1. **Der Registereintrag existiert** und die Zusammensetzung laeuft ohne Konflikt.
2. **Eine doppelte `id` wird abgelehnt.**
3. **Eine unbekannte `id` in `Group.data.modules` bleibt erhalten und wird nicht dargestellt.**
4. **`presents` fuehrt zum Modul**: ein Item mit dem Feld findet die Flaeche.

Die Punkte 1 bis 3 betreffen Listen. Genau dort laufen Dinge auseinander, und genau dafuer sind Tests da.

## 7. Selbst-Pruefung

1. Spec oder Definitions-Abschnitt steht.
2. Kein Eingriff in `packages/toolkit` oder `packages/data-interface`. Sonst: Skill `td-naht`.
3. `presents` gesetzt.
4. Kein `if (type === ...)` im Modul.
5. Fehlende Capability degradiert sichtbar.
6. Steuerleiste ueber `ModuleToolbar`, nicht selbst gebaut.
7. Geteilte Bausteine benutzt statt neu gebaut.
8. Tests fuer die Listen.
9. UI-Texte durch `klare-sprache`.
10. Bezeichner ASCII, Anzeigetexte mit echten Umlauten.

## Verwandt

- `docs/spec/01-app-composition.md` Modul-Register
- `docs/spec/modules/template.md` und `shared-components.md`
- `docs/ARCHITEKTUR.md` Teil 2 und 3
- Skills `td-definieren`, `td-komponente`, `td-test`, `td-naht`
