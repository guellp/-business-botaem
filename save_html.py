# -*- coding: utf-8 -*-
import urllib.request
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

url = 'https://www.koreg.or.kr/haedream/gu/gurt/selectGurtList.do?mi=1124'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as r:
        html = r.read().decode('utf-8')
    with open('haedream_raw.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Saved haedream_raw.html!")
except Exception as e:
    print(f"Error: {e}")
