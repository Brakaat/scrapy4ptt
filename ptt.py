import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/mobile-game/index"
def pages_num(start, end):
    return list(range(start,end+1))
start = int(input("Start Page\n"))
end = int(input("End Page\n"))
pages = pages_num(start, end)

for page in pages:
    urls = url + str(page) + ".html"
    resp = requests.get(urls)
    print("------------------------page:", page, "------------------------")
    if resp.status_code == 200:
        html = resp.text
        # print(html)
        soup = BeautifulSoup(html, "html.parser")
        # print(soup)
        nodes = soup.select("div.title a")
        # print(nodes)
        for node in nodes:
            print(node.text)
            print("https://www.ptt.cc" + node["href"])
    else:
        print(resp)