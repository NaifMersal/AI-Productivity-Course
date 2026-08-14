#!/usr/bin/env python3
"""Keep pre-restructure URLs alive.

Before the restructure the site published one folder per workshop:

    office-workshop-ar/index.html          ksu-workshop/index.html
    office-workshop-ar/slides/<deck>.html  ksu-workshop/slides/<deck>.html

Now there is one shared concept library, one lab library, and one page per
workshop:

    office.html  ksu.html  gov5.html  edu5.html  slides/<deck>.html  labs/<deck>.html

GitHub Pages has no server-side redirects, so this script writes a small
meta-refresh stub at each old path. Every old URL of a workshop, its index and
each of its decks, lands on that workshop's new page, which links the whole
deck library. Nothing from the old tree is republished; the stubs are the only
thing living at those paths.

The deck list is PINNED (see LEGACY_DECKS), not read from output/slides/. It
used to be a glob, back when the only decks in slides/ were the nine the old
tree published. slides/ is now one flat library shared by four workshops, so a
glob would mint stubs at office-workshop-ar/slides/<deck> for decks that never
had a URL there. Only these nine ever did.

Runs as a Quarto post-render step; see `project.post-render` in _quarto.yml.
Old paths with no new equivalent (the English office-workshop, the old sample
files) are deliberately not covered.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# old workshop folder -> new workshop page
WORKSHOPS = {
    "office-workshop-ar": "office.html",
    "ksu-workshop": "ksu.html",
}

# The nine decks that were published under the legacy per-workshop paths.
# Pinned, not globbed: see the module docstring. Add a slug here only if it
# genuinely shipped under the old tree and is missing.
LEGACY_DECKS = (
    "overview.html",
    "how_ai_works_and_rice.html",
    "practice_foundations.html",
    "cowork_intro.html",
    "skills_scripts_templates.html",
    "how_far_this_goes.html",
    "recipe.html",
    "notebooklm_grounding_and_slides.html",
    "wrap_up.html",
)

# Where a legacy slug lives *today*, relative to the output dir. Only slugs
# that moved need an entry; the rest default to slides/<slug>. This map exists
# for the liveness check below, not for the stubs: a stub always points at the
# workshop page, which links the whole library. Keep the legacy slug on the
# left even after a rename, because that is the URL on the printed QR codes.
CURRENT_PATH = {
    # concept/lab split: the RICE practice block became a lab
    "practice_foundations.html": "labs/rice_practice.html",
}

STUB = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<title>انتقل الرابط | Page moved</title>
<link rel="canonical" href="{target}">
<meta http-equiv="refresh" content="0; url={target}">
<script>location.replace("{target}");</script>
</head>
<body style="font-family:system-ui,sans-serif;text-align:center;padding:3rem">
<p>انتقلت هذه الصفحة. <a href="{target}">تابع إلى المحتوى الجديد</a>.</p>
<p lang="en" dir="ltr">This page moved. <a href="{target}">Continue to the new content</a>.</p>
</body>
</html>
"""


def write_stub(path: Path, target: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(STUB.format(target=target), encoding="utf-8")


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    out = root / (os.environ.get("QUARTO_PROJECT_OUTPUT_DIR") or "output")
    if not out.is_dir():
        print(f"make_redirects: no output dir at {out}", file=sys.stderr)
        return 1

    # A pinned deck that no longer renders anywhere means a rename just killed
    # a live URL. Warn rather than fail: the stub itself is still worth
    # writing, and a broken build helps nobody at render time. A deck that
    # merely moved is fine as long as CURRENT_PATH says where it went.
    missing = [
        d
        for d in LEGACY_DECKS
        if not (out / CURRENT_PATH.get(d, f"slides/{d}")).is_file()
    ]
    if missing:
        print(
            "make_redirects: WARNING pinned legacy deck(s) no longer render: "
            + ", ".join(missing),
            file=sys.stderr,
        )

    stubs = 0
    for old, page in WORKSHOPS.items():
        write_stub(out / old / "index.html", f"../{page}")
        stubs += 1
        for deck in LEGACY_DECKS:
            write_stub(out / old / "slides" / deck, f"../../{page}")
            stubs += 1

    print(f"make_redirects: {stubs} redirect stubs written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
