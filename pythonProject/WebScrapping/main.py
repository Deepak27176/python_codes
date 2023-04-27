from bs4 import BeautifulSoup
import requests
# with open("web.html") as web:
#     content = web.read()
res = requests.get("https://news.ycombinator.com/")
content = res.text
soup = BeautifulSoup(content, "html.parser")
score_list = soup.select(selector=".subtext .score")
score_text = []
for score in score_list:
    print(score.text)

