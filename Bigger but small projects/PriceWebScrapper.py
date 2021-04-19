import requests
from bs4 import BeautifulSoup
import smtplib
import time 

URL="https://www.amazon.in/gp/product/B079S811J3/ref=ox_sc_act_image_1?smid=A14CZOWI0VEHLG&psc=1"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.427'}


def price_check():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    print(title.strip())
    price = soup.find(id='priceblock_ourprice').get_text()

    badchar = ['₹', ',', ' ']
    for i in badchar:
        price=price.replace(i,'')

    converted_price = int(price[1:5])
    #print(converted_price)
    return converted_price

def email_sender():
    sender = 'botmail9000@gmail.com'
    recievers = 'ojas.off2003@gmail.com'
    password = 'BotEmail0402'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(sender, password)

    subject = 'Test Subject'
    body = 'Test Body'

    message = f"Subject: {subject} \n \n{body}"

    server.sendmail(
        sender,
        recievers,
        message
    )

    print("email sent")
    server.quit()

def main():
    print("Programm execution")
    ek_aur_price=price_check()

    if ek_aur_price<1799:
        email_sender()
    else:
        print("price is still high")

while True:
    if __name__ == "__main__":
        main()
        time.sleep(3600)