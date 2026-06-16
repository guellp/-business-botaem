# -*- coding: utf-8 -*-
import sys, io, time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

# Chrome 옵션 설정 (Headless 모드로 실행)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

# 브라우저 콘솔 로그 활성화
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
capabilities = DesiredCapabilities.CHROME
capabilities['goog:loggingPrefs'] = {'browser': 'ALL'}

print("Initializing Chrome driver...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # 로컬 index.html의 절대 경로 구하기
    local_path = os.path.abspath("index.html")
    local_url = f"file:///{local_path.replace(os.sep, '/')}"
    print(f"Navigating to local HTML: {local_url}")
    
    driver.get(local_url)
    time.sleep(2)
    
    current_url = driver.current_url
    print(f"Current URL: {current_url}")
    
    # lock.html 로 리다이렉트 되는지 확인
    if "lock.html" in current_url:
        print("Redirected to lock.html. Entering passcode...")
        
        # 비밀번호 입력창 찾기
        pw_input = driver.find_element(By.ID, "pw-input")
        pw_input.send_keys("123459")
        
        # 입장 버튼 클릭
        btn_unlock = driver.find_element(By.ID, "btn-unlock")
        btn_unlock.click()
        
        print("Clicked unlock button. Waiting for redirect...")
        time.sleep(3)
        print(f"URL after unlock click: {driver.current_url}")
        
    # index.html 로드가 완료되었는지 점검
    print("Checking content on local index.html...")
    try:
        total_count = driver.find_element(By.ID, "total-count").text
        current_count = driver.find_element(By.ID, "current-count").text
        status_text = driver.find_element(By.ID, "connection-status").text
        
        print(f"Total count text: {total_count}")
        print(f"Current count text: {current_count}")
        print(f"Connection status text: {status_text}")
        
        # 카드 컨테이너 내부 텍스트 긁기
        cards = driver.find_elements(By.CLASS_NAME, "card-item")
        print(f"Number of card items rendered: {len(cards)}")
        if len(cards) > 0:
            print(f"First card title: {cards[0].find_element(By.CLASS_NAME, 'card-title-text').text}")
    except Exception as inner_e:
        print(f"Failed to read elements: {inner_e}")
        
    # 콘솔 로그 출력
    print("\n=== Browser Console Logs ===")
    for entry in driver.get_log('browser'):
        print(entry)
    print("============================\n")
    
    # 스크린샷 캡처
    screenshot_path = "local_screenshot.png"
    driver.save_screenshot(screenshot_path)
    print(f"Saved screenshot to {screenshot_path}")

finally:
    driver.quit()
