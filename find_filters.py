# -*- coding: utf-8 -*-
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = list(re.finditer(r'\bloaderArea\b', html))
print(f"Total matches found: {len(matches)}")

for i, m in enumerate(matches):
    start = max(0, m.start() - 150)
    end = min(len(html), m.end() + 250)
    print(f"--- Match #{i+1} at index {m.start()} ---")
    print(html[start:end])
    print("---------------------------------------")
