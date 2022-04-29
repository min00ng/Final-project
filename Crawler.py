#기사 제목/앞 2줄/등록일/추천수/조회수
import requests

from bs4 import BeautifulSoup

for p in range(1, 100):
    req = requests.get("https://www.bobaedream.co.kr/list?code=nnews&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page="+str(p),
                       headers={"User-Agent":"Mozilla/5.0"})
    html = req.content.decode('utf-8','replace')
    
    soup = BeautifulSoup(html, 'html.parser')

    articles = soup.select("td.pl14")
    #date = soup.select("td.date").text
    #recommend = soup.select("td.recomm").text
    #count = soup.select('td.count').text
    
    for b in articles:
        title = b.select_one("a.bsubject").text #기사 제목 추출
        #main = b.select_one('li.board_list_text_02').text #앞 2줄정도
        print(title,main)