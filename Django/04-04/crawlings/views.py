from django.shortcuts import render
from django.http import HttpResponse
import time
from bs4 import BeautifulSoup
from .models import Comment
from django.utils import timezone
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create your views here.
def index(request):
    return render(request, 'crawlings/index.html')

def delete_comment(request):
    pass

def search(request):
    keyword = request.GET.get('keyword')
    if not keyword:
        return HttpResponse("검색어를 입력하세요.")
    
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("disable-blink-features=AutomationControlled")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)


    # 1. tossinvest 접속
    driver.get("https://tossinvest.com/")
    time.sleep(2)

    # 2. 검색창에 키워드 입력
    webdriver.ActionChains(driver).send_keys('/').perform()
    webdriver.ActionChains(driver).send_keys(keyword).perform()
    webdriver.ActionChains(driver).send_keys(Keys.RETURN).perform()
    time.sleep(2)

    # 현재 URL에서 종목 코드 추출
    current_url = driver.current_url
    stock_code = current_url.split('/')[-2]  # 'A005930' 같은 코드만 추출

    # 커뮤니티 탭 URL 구성
    community_url = f"https://tossinvest.com/stocks/{stock_code}/community"

    # 해당 URL로 이동
    driver.get(community_url)

    # 댓글 요소 추출 (Selenium만 사용)
    comment_elements = driver.find_elements(By.CSS_SELECTOR, 'div.ho2myi0 div.ho2myi1 main.ho2myi2 div._2ozzgc6 div._2ozzgcd _2ozzgc8 div._2x64iu1 div._2x64iu0 div._1gr0g6c0 _1gr0g6c2 div.wy26a73 div.wy26a75 section.wy26a76 div._1p19xcx1 article.comment xdogm41 div.xdogm45 span.tw-1r5dc8g0._1sihfl60')

    comments = []
    for elem in comment_elements:
        content = elem.text.strip()
        if content:
            # DB에 저장 (필요한 경우)
            Comment.objects.create(
                company=keyword,
                code=stock_code,
                content=content,
                created_at=timezone.now()
            )
            comments.append(content)

    driver.quit()

    return render(request, 'crawlings/index.html', {
        'company': keyword,
        'code': stock_code,
        'comments': comments
    })