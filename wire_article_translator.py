# para = str(input("Enter the text you want to translate: "))
# lang = str(input("Language code you want to translate to: ")).lower()
           
def translate(paragraph, language):
    from googletrans import Translator, constants
    li = []
    out = ""
    translator = Translator()
    li.append(paragraph.split("."))
    for l in li[0]:
        translation = translator.translate(l,dest = language)
        out += f"{translation.text}" + "। "
    return out

# print("_______________________________________________________________________________________________________________________________")
# print("")
# print(translate(para,lang))


def wire_bengali(url):
    import requests
    from bs4 import BeautifulSoup
    req = requests.get(url).text
    soup = BeautifulSoup(req,features = "html5lib")
    title = soup.find("h1").span.text
    short_desc = soup.find("p",class_="shortDesc").text
    sub = ""
    para  = ""
    for i in soup.find_all("p",class_ ="_yeti_done"):
        sub += i.text
    sub = sub.replace('\xa0',"")
    for i in soup.find_all("p",class_=None):
        para += i.text
    para = para.replace('\xa0',"")
    article = title + short_desc + sub + para
    return translate(article,"bn")

text_file = open("E:/translated_article.txt", "w",encoding='utf8')
n = text_file.write(wire_bengali("https://thewire.in/economy/is-food-inflation-in-india-driven-by-demand-or-supply"))
text_file.close()