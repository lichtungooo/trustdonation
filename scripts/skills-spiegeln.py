# -*- coding: utf-8 -*-
"""Spiegelt die Skills aus diesem Repo in den lokalen Workspace.

Die Quelle ist `plugins/trustdonation-tools/skills/`. Wer das Repo klont, hat
die Skills; wer sie benutzen will, spiegelt sie einmal hierher und nach jedem
`git pull`.

Die Richtung ist eine Einbahn: Repo nach lokal. Aenderungen entstehen im Repo,
damit sie versioniert sind und alle sie bekommen. Ein lokal geaenderter Skill
wird beim Spiegeln ueberschrieben und vorher gemeldet.

Aufruf:
    python scripts/skills-spiegeln.py              # spiegeln
    python scripts/skills-spiegeln.py --pruefen    # nur zeigen, was abweicht
"""
import filecmp
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
QUELLE = REPO / "plugins" / "trustdonation-tools" / "skills"
ZIEL = Path.home().parent / "hucke" / ".claude" / "skills"

# Der Workspace kann die Skills auch projektnah halten. Liegt dort ein
# skills-Ordner, gilt er: so wirken sie ohne Neustart und ohne Marketplace.
WORKSPACE_ZIEL = Path("D:/Workspace/.claude/skills")


def ziel_ordner():
    if WORKSPACE_ZIEL.parent.exists():
        return WORKSPACE_ZIEL
    return ZIEL


def main():
    nur_pruefen = "--pruefen" in sys.argv
    ziel = ziel_ordner()

    if not QUELLE.exists():
        print("Keine Skills in " + str(QUELLE), file=sys.stderr)
        return 2
    ziel.mkdir(parents=True, exist_ok=True)

    neu, geaendert, gleich = [], [], []
    for ordner in sorted(QUELLE.iterdir()):
        datei = ordner / "SKILL.md"
        if not datei.is_file():
            continue
        zieldatei = ziel / ordner.name / "SKILL.md"
        if not zieldatei.exists():
            neu.append(ordner.name)
        elif filecmp.cmp(datei, zieldatei, shallow=False):
            gleich.append(ordner.name)
            continue
        else:
            geaendert.append(ordner.name)
        if not nur_pruefen:
            zieldatei.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(datei, zieldatei)

    print("Quelle " + str(QUELLE))
    print("Ziel   " + str(ziel))
    print()
    if neu:
        print("neu        " + ", ".join(neu))
    if geaendert:
        print("geaendert  " + ", ".join(geaendert))
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
