# 00 Überblick

**Status:** Normativer Startpunkt

Dieses Dokument beschreibt, was trustdonation ist, worauf es steht und wo seine Grenzen liegen.

## Der Satz

> trustdonation baut eine Infrastruktur, mit der Stiftungen ihre Förderwirkung erhöhen, weil passende Projekte, Menschen, Anstifter und Zustifter leichter zusammenfinden.

Keine Spendenplattform. Eine Verbindungsschicht zwischen Kapital, Menschen, Organisationen und realen Vorhaben.

## Das Problem

- **Gute Projekte** finden die Förderer nicht, die zu ihnen passen.
- **Förderer** sehen die passenden Projekte nicht, und Mittel bleiben liegen.
- **Die Community** weiß nicht, wo sie in ihrer Nähe beitragen kann.
- **Stiftungen** finden keinen Nachwuchs für ihre Gremien.
- **Zustifter** wissen nicht, wo ihr Kapital dauerhaft wirkt.

Die vorhandenen Verzeichnisse lösen einen Teil davon: Sie listen Stiftungen. Was fehlt, ist die Verbindung zwischen Liste und Wirklichkeit. Neun Suchen laufen hier aneinander vorbei, und acht davon über Zufall. Die Aufstellung steht in [01-rollen.md → Wer sucht wen](01-rollen.md).

## Die Lösung

| Baustein | Was er leistet |
|---|---|
| **Karte** | Stiftungen, Projekte und ihre Community an einem Ort, weltweit, mit Quelle und Prüfdatum |
| **Matching** | Vorschläge mit Begründung Zeile für Zeile, nie als Note |
| **Projektseite** | was ein Projekt tut, braucht und schon erreicht hat |
| **Vertrauensschicht** | reale Begegnung, bestätigter Beitrag, gewachsenes Vertrauen |

## Die Kette

```text
Vertrauen → Entdeckung → Matching → Verbindung → Finanzierung → Umsetzung → Wirkung
```

Geld steht nicht am Anfang. Es ist ein Ergebnis einer Beziehung.

## Wo trustdonation steht

```text
┌────────────────────────────────────────────────────────────┐
│  trustdonation                                             │
│  Landingpage · Stiftungsdaten · Matching · Ansprache       │
├────────────────────────────────────────────────────────────┤
│  Real Life Stack (RLS)                                     │
│  App Shell · Karte · Gruppen · Profile · Kalender · Feed   │
├────────────────────────────────────────────────────────────┤
│  Web of Trust (WoT)                                        │
│  Identität · Begegnung · Bestätigung · Sync                │
└────────────────────────────────────────────────────────────┘
```

trustdonation ist eine **Instanz** des Real Life Stack, kein Fork. Die App kommt als fertiges Image, alles hier ist Konfiguration und Inhalt (siehe [Spec 11 des Stacks][spec11]).

[spec11]: https://github.com/real-life-org/real-life-stack/blob/master/docs/spec/11-runtime-config-und-branding.md

## Abgrenzung der Namen

Drei Dinge werden leicht verwechselt. Diese Zuordnung folgt den Dokumenten des Stacks.

| Name | Was es ist | Wer besitzt die Semantik |
|---|---|---|
| **Real Life Stack (RLS)** | App- und UI-Baukasten, backend-agnostisch | [real-life-stack][rls] |
| **Web of Trust (WoT)** | Protokoll für dezentrale Identität und Vertrauensbeziehungen: `did:key`, JWS, E2EE-Sync | [web-of-trust][wot] |
| **Real Life Network Protocol (RLNP)** | Soziale Semantik: Begegnungen, Ressourcen, Bedürfnisse, Quests, Evidence, Attestation Policies | RLNP-Konzept im Stack-Repo |
| **trustdonation** | Ein Anwendungsfall darauf: Förderung zwischen Stiftungen, Projekten und ihrer Community | dieses Repo |

[rls]: https://github.com/real-life-org/real-life-stack
[wot]: https://github.com/antontranelis/web-of-trust

Die drei Vertrauensstufen in [02-vertrauen.md](02-vertrauen.md) sind unsere Sicht auf das, was RLNP und WoT bereitstellen. Wir definieren sie für unseren Anwendungsfall, wir besitzen sie nicht.

## Geltungsbereich

Diese Dokumente beschreiben:

- die vier Rollen, die Community und ihren Kreislauf,
- wer hier wen sucht,
- die drei Stufen des Vertrauens,
- das Datenmodell für Stiftungen und Projekte,
- die rechtlichen Leitplanken,
- Matching mit Begründung,
- die Ansprache von Stiftungen,
- den Pilot und die Reihenfolge der Umsetzung.

Diese Dokumente beschreiben nicht:

- Kryptografie, DIDs oder Signaturformate (das ist WoT),
- die Architektur des Baukastens (das ist RLS),
- die Rechtsform und Satzung des Vereins.

## Die vier Grundsätze

1. **Geld kauft keine Vertrauensbewertung.** Partner bekommen Status und Mitsprache, keine bessere Platzierung im Matching.
2. **Fakten statt Noten.** Kriterien, Quelle, Prüfdatum. Keine Sterne, keine Ampeln, keine Bewertung von Organisationen.
3. **Vertrauen entsteht im Netz, nicht bei uns.** Wir stellen kein Zertifikat aus.
4. **Die Identität bleibt beim Menschen.** Schlüssel auf dem Gerät, Profil wandert mit.

Diese vier Sätze sind normativ. Wenn ein Vorschlag einen davon verletzt, wird der Vorschlag geändert, nicht der Satz.
