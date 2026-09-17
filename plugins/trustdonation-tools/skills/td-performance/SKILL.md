---
name: td-performance
description: "Performance in trustdonation: messen statt raten. Bundle-Budget mit echten Zahlen, die teuren Stellen (Karte, WebGL, viele Pins), Antons Werkzeuge (keepMounted, panelFit, Virtualisierung), und woran man eine echte Verbesserung erkennt."
---

# Performance

**Messen, dann aendern, dann wieder messen.** Eine Optimierung ohne Zahl davor und danach ist eine Vermutung.

## Die Zahlen von heute

Gemessen am 17.09.2026, `pnpm build`, Ordner `apps/reference/dist`:

| Datei | Groesse | Was |
|---|---:|---|
| `index-*.js` (gross) | **1758 KB** | die App |
| `maplibre-gl-*.js` | **1029 KB** | die Kartenbibliothek |
| `index-*.js` | 613 KB | Teilstueck |
| `index-*.js` | 237 KB | Teilstueck |
| **gesamt `dist/`** | **5.0 MB** | mit Schriften und Bildern |

Vite meldet beim Bau selbst, dass drei Stuecke ueber der Warnschwelle liegen.

## Das Budget

| Was | Grenze | heute |
|---|---:|---|
| groesstes JavaScript-Stueck | 800 KB | **1758 KB** |
| Karte, nachgeladen statt im Start | ja | nein |
| `dist/` gesamt | 4 MB | 5.0 MB |
| Erstes sichtbares Bild, schnelle Leitung | 2 s | ungemessen |
| Erstes sichtbares Bild, langsame Leitung | 5 s | ungemessen |

**Ein Budget ist erst ein Budget, wenn es gemessen wird.** Die beiden letzten Zeilen sind heute Absicht, keine Zahl.

## Messen

```bash
cd /d/Workspace/20-repos/rls-uebersicht
pnpm build
ls -la apps/reference/dist/assets/*.js | awk '{printf "%8.0f KB  %s\n", $5/1024, $9}' | sort -rn | head
du -sh apps/reference/dist
```

Was in einem Stueck steckt, zeigt die Karte des Bauwerks:

```bash
npx vite-bundle-visualizer --config apps/reference/vite.config.ts
```

Im Browser: die Registerkarte **Netzwerk** mit Drosselung auf langsame Leitung, und **Leistung** fuer die Aufzeichnung.

## Die teuren Stellen

### Die Karte

Sie ist mit Abstand das groesste Stueck (1 MB) und das teuerste beim Aufbau: WebGL-Kontext, Arbeiter, entfernter Stil.

- **`keepMounted: true`** im Registereintrag haelt sie im Baum, statt sie bei jedem Modulwechsel neu aufzubauen. Das hat Anton dafuer gebaut.
- **`panelFit: "overlay"`** verhindert, dass sie beim Oeffnen eines Panels schmaler wird und neu zeichnet.
- **Nachladen statt mitliefern:** Wer nie auf die Karte geht, soll die Bibliothek nicht herunterladen. Ein `import()` an der Registerstelle.

### Viele Pins

Die 280 recherchierten Stiftungen sind der ernste Fall. Einzelne Merkmale zeichnen bei dieser Zahl spuerbar langsamer.

- **Buendeln** (Clustering) statt jeden Punkt einzeln.
- Die Karte des Landing-Prototyps nutzt bereits `markercluster`. Das Muster ist da.
- **Erst messen, dann buendeln.** Unter hundert Punkten lohnt es meist nicht.

### Lange Listen

Feed und Liste wachsen mit den Daten.

- Antons Toolkit bringt **Virtualisierung** mit (`selectionFocusVirtualizer` in `lib/selection-focus`). Benutzen, nicht neu bauen.
- **Bilder als Data-URL** in `Group.data.image` liegen im Datensatz und werden bei jeder Gruppenliste mitgereicht. Bei vielen Spaces gehoeren sie in den Datei-Speicher.

### Der erste Start

- **Musterdaten im Bundle:** Unsere `groups.json` traegt Bilder als base64 und wiegt 33 KB. Bei 280 Stiftungen waere das anders. Dann gehoeren sie in eine Datei, die nachgeladen wird.
- **Schriften** aus dem eigenen Haus statt von fremden Servern, mit `font-display: swap`.

## Antons Werkzeuge

Bevor etwas Eigenes entsteht, nachsehen, was er schon hat:

| Werkzeug | Wofuer |
|---|---|
| `keepMounted` im Registereintrag | teurer Aufbau bleibt erhalten |
| `panelFit: "overlay"` | Flaeche zeichnet beim Panel-Oeffnen nicht neu |
| `fill` und `maxWidth` | Layout ohne Nachmessen im Browser |
| `selection-focus` mit Virtualizer | lange Listen |
| `useModuleContentClass` | Kopf und Inhalt bleiben buendig, ohne zweite Messung |

Er hat im September ausdruecklich an der Geschwindigkeit gearbeitet (PR #372, #376). **Vor einer eigenen Optimierung pruefen, ob sie schon da ist:** Skill `td-anton`.

## Woran man eine echte Verbesserung erkennt

1. **Eine Zahl davor und danach**, mit demselben Befehl gemessen.
2. **Am Gefuehl geprueft**, auf gedrosselter Leitung, nicht nur an der Zahl.
3. **Kein Tor gebrochen:** Typen, Regeln, Augenschein bleiben gruen.
4. **Nichts unlesbarer geworden.** Eine Optimierung, die niemand mehr versteht, ist eine Schuld mit Zinsen.

Was **keine** Verbesserung ist: ein Wert, der sich nur im Bau zeigt, aber nie in der Nutzung. Ein Stueck, das 50 KB kleiner ist und dafuer zweimal geladen wird, ist langsamer.

## Die Reihenfolge

1. **Messen.** Ohne Zahl kein Anfang.
2. **Das groesste Stueck zuerst.** Die Karte ist heute ein Fuenftel von allem.
3. **Nachladen vor Verkleinern.** Was niemand braucht, muss nicht klein sein, es muss fehlen.
4. **Buendeln vor Zeichnen.** Bei vielen Punkten ist die Zahl der Elemente das Problem, nicht ihre Groesse.
5. **Wieder messen.** Und die Zahl in `memory/stand_trustdonation.md` schreiben, damit die naechste Runde weiss, wo sie steht.

## Verwandt

- `docs/ARCHITEKTUR.md` Teil 7 (die Qualitaetstore)
- `docs/spec/01-app-composition.md` (Registereintrag, `keepMounted`, `panelFit`)
- Skills `td-anton`, `td-modul`, `td-test`
