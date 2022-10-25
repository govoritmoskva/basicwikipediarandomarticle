import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    url = requests.get("https://ru.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text
    
    print(f"{title} \nВы хотите прочитать статью? (Y/N)")
    answer = input("").lower()

    if answer == "y":
        url = "https://ru.wikipedia.org/wiki/%s" % title
        webbrowser.open(url)
        break
    elif answer == "n":
        print("Ищем новую статью!")
        continue
    else:
        print("Команда ненайдена!")
        break