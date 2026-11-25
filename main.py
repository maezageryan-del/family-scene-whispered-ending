"""Make the AI Judge Feel Proud: A Family Scene.

One short family scene, one line, 167 characters (limit 280). The program
writes the scene to /output/entry.txt (or MAKEFUN_OUTPUT_DIR when set).

The scene: a dad dozes off halfway through the bedtime story he was reading,
so the kids tuck the blanket around him instead, turn the page for him, and
whisper the ending so he will not miss it. Warmth first, heartfelt second,
a light wry turn third -- exactly the order the judge brief weighs.
"""

import os

ENTRY = (
    "Dad dozed off halfway through the bedtime story, so the kids tucked "
    "the blanket around him, turned the page for him, and whispered the "
    "ending \u2014 so he wouldn't miss it."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 280, f"entry is {len(ENTRY)} chars, must be 1-280"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars ({len(ENTRY.encode('utf-8'))} bytes) to {path}")
    with open(path, encoding="utf-8") as f:
        assert f.read() == ENTRY, "round-trip check failed"


if __name__ == "__main__":
    main()
