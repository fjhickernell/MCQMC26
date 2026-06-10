from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SLIDES = ROOT / "slides"

slides = SLIDES / "Plenary_MCQMC2026.qmd"
out = SLIDES / "generated_main_messages.qmd"

print(f"Reading: {slides}")
print(f"Writing: {out}")

text = slides.read_text()

messages = re.findall(
    r":::\s*\{[^}]*\.main-message[^}]*\}\s*\n(.*?)\n\s*:::",
    text,
    flags=re.S,
)

print(f"Found {len(messages)} main messages")

for i, msg in enumerate(messages, start=1):
    print(f"{i}: {' '.join(msg.strip().split())}")

# Do not include a heading here if the slide already has one.
content = ""

for msg in messages:
    msg = " ".join(msg.strip().split())
    content += f"- {msg}\n"

# Only rewrite if contents changed, to avoid Quarto watch loops.
if out.exists() and out.read_text() == content:
    print(f"No change: {out}")
else:
    out.write_text(content)
    print(f"Wrote: {out}")

print("Done")