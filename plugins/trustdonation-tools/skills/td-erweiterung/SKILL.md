---
name: td-erweiterung
description: "Eine Komponente der Erweiterungen bauen: eine fertige Darstellung für einen Typ (Project Profile, Stiftungsprofil, später Widgets und HUD), wählbar je Space. Definieren, Kern in td-core, Verzeichnis, Darstellung mit eigenem Einstieg, eigene Schicht im Typ-Register ohne Naht, Musterdaten, ansehen auf Rechner/Handy/dunkel und live, Tore. Mit der Designsprache aus einem Guss."
---

# Eine Komponente der Erweiterungen bauen

Timo am 01.10.2026: *"Wir halten uns an Antons definierte Vorgaben, damit es super integriert werden kann. Wir entwickeln jedoch ganz neue und unterschiedliche UX, die sich ähnlich anfühlen, jedoch vom Aufbau her verschieden sind, und wie aus einem Guss funktionieren."*

**Die Quelle ist das Werkstattbuch** `docs/KOMPONENTEN.md` im Stack-Fork (`20-repos/rls-uebersicht`, Branch `trustdonation`). Dieser Skill ist die Kurzfassung und die Reihenfolge. Was dort dazukommt, gilt.

**Abgrenzung:**

| Skill | Wofür |
|---|---|
| `/td-erweiterung` | eine **ganze Darstellung**, die ein Space in den Erweiterungen wählt (Komponente, später Widget, Theme) |
| `/td-komponente` | ein kleiner **Oberflächen-Baustein** in td-ui (Knopf, Feld, Karte) |
| `/td-modul` | eine **Fläche** im Space (Feed, Karte, Circeling) |
| `/td-profil` | **welche Felder** ein Profil trägt und wie man sie erfragt |

---

## Was eine Komponente ist

Eine fertige Darstellung für einen Typ. Sie greift, wenn der aktuelle Space sie in `Group.data.komponenten` gewählt hat **und** der Eintrag ihre Felder trägt. Sonst bleibt Antons Darstellung aus dem Feld-Register. Definition: `DEFINITION.md` Teil 8, „Was eine Komponente ist“.

**Keine Naht.** Sie dockt als eigene Schicht im Typ-Register an (Slot `detail`). Wer dafür Antons Pakete öffnet, ist auf dem falschen Weg.

---

## Die neun Schritte

| # | Schritt | Wo | Prüfen |
|---|---|---|---|
| 1 | **Definieren:** Timos Satz, Tabelle *Abschnitt · Frage · Felder*, Regeln für Fehlendes und Beispiele | `docs/DEFINITION.md` Teil 8 | `/td-definieren` |
| 2 | **Kern:** rohe `data` hinein, fertige Ansicht heraus; Fehlendes fällt weg, Zahlen gerechnet, Adressen geprüft; dazu `traegt<Name>()` | `packages/td-core/src/<name>.ts` | Tests in `packages/td-core/tests/<name>.test.ts` |
| 3 | **Verzeichnis:** `{ id, art: "komponente", name, fuerTyp, erbauer, reife: "beta", beschreibung }`, Id als Konstante | `packages/td-core/src/erweiterungen.ts` | Test: Name, Typ, keine Kollision mit Modul-Ids |
| 4 | **Darstellung:** Karte für die Leiste plus ganze Ansicht im `Dialog`; Standard-Export nimmt rohe Daten | `packages/td-ui/src/<name>.tsx` mit **eigenem Einstieg** in `package.json`, **nicht** im Index | |
| 5 | **Bindung:** Rückfall vorher holen (`resolveTypePresentation(typ).detail`), `lazy` + `Suspense`, `useCurrentGroup` + `komponenteAktiv`, eigene Schicht `trustdonation-<id>` | `apps/reference/src/type-register.tsx` | |
| 6 | **Reiter:** läuft von selbst über `komponentenAus()`; nur ein eigenes Symbol braucht eine Zeile | `apps/reference/src/views/erweiterungen-abschnitt.tsx` | `apps/reference/src/erweiterungen.test.tsx` |
| 7 | **Musterdaten:** Eintrag mit `muster: true`, sichtbar erfundene Angaben (`example.org`), im Demo-Space; Komponente in `groups.json` → `komponenten`; **`SEED_VERSION` und `MUSTERDATEN_VERSION` gleich hochzählen**; gezeichnete SVG-Bilder | `packages/td-core/daten/`, `apps/reference/public/muster/` | |
| 8 | **Ansehen**, lokal und nach dem Ausliefern live; **jedes Bild anschauen** | `node td-tools/komponente-ansehen.mjs <space>/<modul>/<item>` (Pfad ohne führenden Schrägstrich) | Rechner, Handy, dunkel, 0 Seitenfehler |
| 9 | **Tore**, alle acht, nach **jeder** Änderung; ausliefern; festhalten | `python td-tools/pruefen.py`, `/td-ausliefern`, `docs/AUSLIEFERUNGEN.md`, `docs/KOMPONENTEN.md` (neue Fallen) | |

---

## Aus einem Guss: die Designsprache

Jede Komponente bekommt **ihren eigenen Aufbau**, passend zu ihrem Zweck. Was sie verbindet:

- **Zwei Ansichten:** eine Karte in Antons schmaler Detail-Leiste (nie Text über ein Bild legen) und die ganze Ansicht über den Bildschirm (`showCloseButton={false}`, eigener Schließen-Knopf).
- **Flächen statt Rahmen:** `rounded-3xl`/`rounded-2xl`, `bg-<farbe>-50/60`, dunkel `dark:bg-<farbe>-950/40`.
- **Schwebende Karten mit Schatten:** `bg-card shadow-xl shadow-black/5`.
- **Abschnitts-Überschrift:** Symbol plus `text-xs font-semibold uppercase tracking-wider text-muted-foreground`.
- **Kopf:** Bild über die volle Breite mit Verlauf, Kennzahlen mit `-mt-10` halb darüber.
- **Bento-Raster** `sm:grid-cols-6`, mitlaufende Seitenspalte `lg:sticky`, auf dem Handy feste Leiste unten.
- **Farben nach Bedeutung:**

  | Farbe | Bedeutung |
  |---|---|
  | Smaragd | Geben und Handlung |
  | Bernstein | was fehlt |
  | Grün | Wirkung |
  | Orange | Geld |
  | Himmelblau | Zeit |
  | Violett | Kontakt |

- **Ehrlich:** „Musterprojekt“, „Beispielzahlen“. Ein Knopf ohne Ziel steht still und nennt den Grund.

Vor einer neuen Komponente: kurz im Netz nachsehen, was für diese Art Seite gerade gut funktioniert (Timo: *"dafür dürfen wir uns aus dem Netz Inspiration holen"*), und die Quellen im Werkstattbuch nennen.

---

## Die Fallen, kurz

1. **Budget:** Alles über den Index von td-ui landet im Hauptteil. Eigener Einstieg, und auch der Kern läuft im nachgeladenen Stück.
2. **`BASE_URL` heißt live `/app`** ohne Schrägstrich: den Schrägstrich selbst setzen. Lokal fällt das nicht auf, darum **live ansehen**.
3. **Tests ändern sich mit der Funktion**, etwa Platzhalter-Texte und die Regel „jeder Eintrag ist ein Modul“.
4. **Nachgeladenes im Test:** warten, bis ein Knopf steht.
5. **Radix im Radix:** ein eigener `Dialog`, Radix stapelt ihn.

Die ganze Liste mit Ursachen steht im Werkstattbuch, Abschnitt 4.

---

## Was als Nächstes kommt

- **Stiftungsprofil** (zweite Komponente; die vier Verbesserungen sind entschieden)
- **Open Collective live** über die öffentliche GraphQL-Schnittstelle
- **Bearbeiten** über Antons `fields`
- **Widgets und HUD** als vierte Art, siehe Gedächtnis `project_gamification_komponenten.md`

## Verwandt

- `docs/KOMPONENTEN.md`, `docs/DEFINITION.md` Teil 8
- Skills `/td-definieren`, `/td-profil`, `/td-performance`, `/td-test`, `/td-ausliefern`
