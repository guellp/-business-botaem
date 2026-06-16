# -*- coding: utf-8 -*-
import sys, io, re, subprocess

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# index.html 내의 모든 script 내용을 추출합니다.
# 마지막 script 블록(주요 로직이 들어있는 곳)을 타겟으로 잡습니다.
scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)

if not scripts:
    print("No script tags found!")
    sys.exit(0)

# 마지막 script 블록 검사
js_code = scripts[-1]

# 임시 js 파일에 저장
temp_js = 'temp_test.js'
with open(temp_js, 'w', encoding='utf-8') as f:
    f.write(js_code)

print("Saved script to temp_test.js. Running node syntax check...")
result = subprocess.run(['node', '-c', temp_js], capture_output=True, text=True, encoding='utf-8')

if result.returncode == 0:
    print("✅ Node.js syntax check passed! No syntax errors.")
else:
    print("❌ Node.js syntax check failed:")
    print(result.stderr)
