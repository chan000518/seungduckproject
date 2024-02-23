import requests
from bs4 import BeautifulSoup as bs

# 웹 페이지에서 데이터를 가져옵니다.
date = '2024-02-23'
urls = []
urls.append(f"https://sports.daum.net/schedule/epl")
urls.append(f"https://sports.daum.net/schedule/primera")
for url in urls:
    page = requests.get(url)

    # BeautifulSoup 객체를 생성하여 HTML을 파싱합니다.
    soup = bs(page.content, "html.parser")
    print(soup)
    # 'num_date' 클래스를 가진 모든 요소를 선택합니다.
    # 이 부분은 실제 웹사이트의 구조에 따라 수정이 필요할 수 있습니다.
    team_elements = soup.select('.tit_team')
    # 선택된 각 요소의 텍스트를 출력합니다.
    for team in team_elements:
        print(team.text)


