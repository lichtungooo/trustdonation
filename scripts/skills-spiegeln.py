# -*- coding: utf-8 -*-
"""Spiegelt die Skills aus diesem Repo in den lokalen Workspace.

Quelle sind alle Plugins unter `plugins/*/skills/`. Wer das Repo klont, hat
die Skills; wer sie benutzen will, spiegelt sie einmal hierher und nach jedem
`git pull`.

Die Richtung ist eine Einbahn: Repo nach lokal. Aenderungen entstehen im Repo,
damit sie versioniert sind und alle sie bekommen. Ein lokal geaenderter Skill
wird beim Spiegeln ueberschrieben.

Ein Skill ist ein ganzer Ordner, nicht nur `SKILL.md`: `sprach-stile` traegt
elf Dateien unter `reference/`. Wer nur die eine Datei kopiert, bekommt einen
Skill, der ins Leere verweist.

Aufruf:
    python scripts/skills-spiegeln.py              # spiegeln
    python scripts/skills-spiegeln.py --pruefen    # nur zeigen, was abweicht
"""
import filecmp
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PLUGINS = REPO / "plugins"

# Der Workspace haelt die Skills projektnah: so wirken sie ohne Marketplace.
WORKSPACE_ZIEL = Path("D:/Workspace/.claude/skills")
HEIM_ZIEL = Path.home() / ".claude" / "skills"


def ziel_ordner():
    return WORKSPACE_ZIEL if WORKSPACE_ZIEL.parent.exists() else HEIM_ZIEL


def dateien(ordner):
    return sorted(p for p in ordner.rglob("*") if p.is_file())


def vergleiche(quelle, ziel):
    """gleich, wenn beide dieselben Dateien mit demselben Inhalt haben."""
    if not ziel.exists():
        return False
    q = {p.relative_to(quelle).as_posix() for p in dateien(quelle)}
    z = {p.relative_to(ziel).as_posix() for p in dateien(ziel)}
    if q != z:
        return False
    return all(filecmp.cmp(quelle / r, ziel / r, shallow=False) for r in q)


def main():
    nur_pruefen = "--pruefen" in sys.argv
    ziel_wurzel = ziel_ordner()

    if not PLUGINS.exists():
        print("Keine Plugins in " + str(PLUGINS), file=sys.stderr)
        return 2
    ziel_wurzel.mkdir(parents=True, exist_ok=True)

    neu, geaendert, gleich = [], [], []
    for plugin in sorted(PLUGINS.iterdir()):
        skills = plugin / "skills"
        if not skills.is_dir():
            continue
        for ordner in sorted(skills.iterdir()):
            if not (ordner / "SKILL.md").is_file():
                continue
            ziel = ziel_wurzel / ordner.name
            if not ziel.exists():
                neu.append(ordner.name)
            elif vergleiche(ordner, ziel):
                gleich.append(ordner.name)
                continue
            else:
                geaendert.append(ordner.name)
            if not nur_pruefen:
                # Ganzen Ordner ersetzen, damit geloeschte Referenzdateien
                # nicht als Leichen zurueckbleiben.
                if ziel.exists():
                    shutil.rmtree(ziel)
                shutil.copytree(ordner, ziel)

    print("Quelle " + str(PLUGINS))
    print("Ziel   " + str(ziel_wurzel))
    print()
    if neu:
        print("neu          " + ", ".join(neu))
    if geaendert:
        print("geaendert    " + ", ".join(geaendert))
    if gleich:
        print("unveraendert " + str(len(gleich)))
    if nur_pruefen and (neu or geaendert):
        print()
        print("Zum Uebernehmen: python scripts/skills-spiegeln.py")
        return 1
    if not (neu or geaendert):
        print()
        print("Alles auf Stand.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
