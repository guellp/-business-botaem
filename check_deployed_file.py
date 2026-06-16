# -*- coding: utf-8 -*-
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

file_path = r"C:\Users\bwj10\.gemini\antigravity\brain\4a43d674-c983-408f-8dd0-25df8ba40f2c\.system_generated\steps\1144\content.md"

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

count = text.count("loaderArea")
print(f"'loaderArea' occurrences in deployed page: {count}")
