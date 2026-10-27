# Counts the problem folders in easy/, medium/ and hard/ and writes the badges into README.md
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")
LEVELS = [("Easy", "easy", "brightgreen"), ("Medium", "medium", "orange"), ("Hard", "hard", "red")]


def count_problems(folder):
    path = os.path.join(ROOT, folder)
    if not os.path.isdir(path):
        return 0
    return sum(os.path.isdir(os.path.join(path, name)) for name in os.listdir(path))


counts = {label: count_problems(folder) for label, folder, _ in LEVELS}
total = sum(counts.values())

badges = [f"![Total](https://img.shields.io/badge/Solved-{total}-blue)"]
for label, _, color in LEVELS:
    badges.append(f"![{label}](https://img.shields.io/badge/{label}-{counts[label]}-{color})")
block = "<!-- counts:start -->\n" + "\n".join(badges) + "\n<!-- counts:end -->"

with open(README, encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(r"<!-- counts:start -->.*?<!-- counts:end -->", block, content, flags=re.S)

if new_content != content:
    with open(README, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_content)
    print("README updated:", counts)
else:
    print("Counts unchanged:", counts)
