import csv
import json
import os
from collections import defaultdict

FILES = [
    'Vatslaw_Lastowski_Dictionary_Letters_A_to_O_.csv',
    'Vatslaw_Lastowski_Dictionary_Letters_P_to_YA.csv'
]

letters = defaultdict(list)
all_entries = []
for fname in FILES:
    with open(fname, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Headword'] == 'Headword':
                continue
            head = row['Headword'].strip()
            defn = row['Definition'].strip()
            if not head:
                continue
            entry = {'headword': head, 'definition': defn}
            all_entries.append(entry)
            letters[head[0]].append(entry)

os.makedirs('site', exist_ok=True)

with open('site/data.json', 'w', encoding='utf-8') as f:
    json.dump(all_entries, f, ensure_ascii=False, indent=2)

letters_sorted = sorted(letters.keys())

nav_links = '\n'.join(f'<li><a href="{letter}.html">{letter}</a></li>' for letter in letters_sorted)

index_html = f"""<!DOCTYPE html>
<html lang=\"be\">
<head>
<meta charset=\"utf-8\">
<title>Lastouski Dictionary</title>
<script src=\"search.js\"></script>
<style>
body {{ font-family: sans-serif; }}
nav ul {{ list-style: none; padding: 0; }}
</style>
</head>
<body>
<h1>Lastouski Dictionary</h1>
<p>Select a letter:</p>
<nav><ul>{nav_links}</ul></nav>
<div>
<input type=\"text\" id=\"search\" placeholder=\"Search...\" oninput=\"search()\">
<div id=\"results\"></div>
</div>
</body>
</html>"""

with open('site/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

for letter in letters_sorted:
    entries = letters[letter]
    items = '\n'.join(f'<li><strong>{e["headword"]}</strong> — {e["definition"]}</li>' for e in entries)
    html = f"""<!DOCTYPE html>
<html lang=\"be\">
<head>
<meta charset=\"utf-8\">
<title>Letter {letter} - Lastouski Dictionary</title>
<script src=\"search.js\"></script>
<style>
body {{ font-family: sans-serif; }}
</style>
</head>
<body>
<nav><a href=\"index.html\">Home</a></nav>
<h1>Letter {letter}</h1>
<div>
<input type=\"text\" id=\"search\" placeholder=\"Search...\" oninput=\"search()\">
<div id=\"results\"></div>
</div>
<ul>{items}</ul>
</body>
</html>"""
    with open(f'site/{letter}.html', 'w', encoding='utf-8') as f:
        f.write(html)
