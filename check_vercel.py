# -*- coding: utf-8 -*-
import sys, io, urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

urls = [
    "https://business-botaem.vercel.app/index.html",
    "https://botaem.vercel.app/index.html",
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

for url in urls:
    print(f"\n--- {url} ---")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8')
        record_count = content.count('"서비스명"')
        loader_count = content.count('loaderArea')
        print(f"  데이터 건수 (서비스명): {record_count}")
        print(f"  loaderArea 개수: {loader_count}")
        
        import re, subprocess
        scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
        if scripts:
            with open('temp_v.js', 'w', encoding='utf-8') as f:
                f.write(scripts[-1])
            res = subprocess.run(['node', '-c', 'temp_v.js'], capture_output=True, text=True, encoding='utf-8')
            print(f"  JS 문법: {'✅ 정상' if res.returncode == 0 else '❌ 에러'}")
    except Exception as e:
        print(f"  접속 실패: {e}")
