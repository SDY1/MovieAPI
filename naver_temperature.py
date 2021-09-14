import requests
from bs4 import BeautifulSoup

def callTemperature():
        uri = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84%EA%B8%B0%EC%98%A8"
        response = requests.get(uri)

        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        target = soup.select_one(".todaytemp")
        temperature = {"temp":target.text}
        return temperature