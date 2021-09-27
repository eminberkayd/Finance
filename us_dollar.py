import requests
import xml.etree.ElementTree as ET
from urllib.request import urlopen


url = "http://www.tcmb.gov.tr/kurlar/today.xml"
resp = requests.get(url=url)


tree = ET.parse(urlopen(url))
root = tree.getroot()

mylist = []
mylist.append(root.findall('Currency'))

for i in mylist[0]:
    currencyCode = i.get('Kod')
    buying = i.find("BanknoteBuying").text
    selling = i.find("BanknoteSelling").text

    if currencyCode == "USD":

            print(f"Amerikan Doları alış fiyatı: {buying}")
            print(f"Amerikan Doları satış fiyatı: {selling}")
            print(f"Alış ve satış arasındaki kur farkı: {float(selling)-float(buying)}")
            break

    else:
        print("USD bilgilerine erişilemedi. Lütfen tekrar deneyiniz.")
