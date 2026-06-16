# -*- coding: utf-8 -*-
import sys, io, urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

urls = [
    "https://guellp.github.io/-business-botaem/index.html",
    "https://botaem.vercel.app/index.html",
    "https://guellp.github.io/salim-botaem-/index.html"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

for url in urls:
    print(f"\n--- Checking URL: {url} ---")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8')
        print("Successfully fetched!")
        
        # loaderArea 카운트 (정상 상태는 4)
        loader_count = content.count("loaderArea")
        print(f"  'loaderArea' count: {loader_count}")
        
        # 서비스명 카운트 (데이터 건수)
        record_count = content.count("서비스명")
        print(f"  Data record count (서비스명 count): {record_count}")
        
        # JS Syntax Check
        import re, subprocess
        scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
        if scripts:
            with open('temp_check.js', 'w', encoding='utf-8') as f:
                f.write(scripts[-1])
            res = subprocess.run(['node', '-c', 'temp_check.js'], capture_output=True, text=True, encoding='utf-8')
            if res.returncode == 0:
                print("  ✅ JS syntax check: PASSED")
            else:
                print("  ❌ JS syntax check: FAILED")
                print(res.stderr.strip()[:150])
    except Exception as e:
        print(f"  Failed to fetch: {e}")
