# Wikipedia Random Article

**Wikipedia Random Article** - a program that can give out random articles from **Wikipedia**. (without using module "wikipedia")

## 🛠Links

[BeautifulSoup4 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) \
[Webbrouser documentation](https://docs.python.org/3/library/webbrowser.html) \
[Requests documentation](https://docs.python.org/3/library/webbrowser.html)

## 📂Some examples of code

```
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
```

## 💾Example
![photo](https://github.com/vstyoma/basicwikipediarandomarticle/blob/main/wikipediarandomarticle/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-10-25%20225734.png)

*[See full code](https://github.com/vstyoma/basicwikipediarandomarticle/blob/main/wikipediarandomarticle/wikipediaradomarticle/WikipediaRandomArticle.py)*
