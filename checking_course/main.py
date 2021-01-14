import requests
from bs4 import BeautifulSoup
import time

class Currency:
    DOLLAR_UAH = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%B0%D1%80+%D0%B2+%D0%B3%D1%80%D0%BD&rlz=1C1SQJL_ruUA924UA924&oq=ljkfh+d+&aqs=chrome.1.69i57j0i10i131i433j0i10j0i10i131i433j0i10l4.8328j1j7&sourceid=chrome&ie=UTF-8'
    headers = {'User-Agen': 'Mozillat/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

    current_convertad_price = 0
    difference = 5

    def __init__(self):
        self.current_convertad_price = float(self.get_currency_price().replace(",", "."))

    def get_currency_price(self):
        full_page = requests.get(self.DOLLAR_UAH, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde SwHCTb", "data-precision": 2})
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_currency_price().replace(",", "."))

        if currency >= self.current_convertad_price + self.difference:
            print("Курс сильно вырос, может пора что-то делать?")
        elif currency <= self.current_convertad_price - self.difference:
            print("Курс сильно упал, может пора что-то делать?")

        print("Сейчас курс: 1 доллар = " + str(currency) + " гривен")
        time.sleep(5)
        self.check_currency()

currency = Currency()
currency.check_currency()