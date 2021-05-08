from bs4 import BeautifulSoup
import requests

URL = 'https://diachidoanhnghiep.org'
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'lxml')
table = soup.find_all('ul', {'class':'collapse in'})[0]

a_tags = table.find_all('a')
import sys

def get_content(url):
    try:
        ans = []
        while True:
            res = requests.get(url) 
            domain = url.split('?')[0].split('/')[-1]
            s = BeautifulSoup(res.text, 'lxml')
            pagination = s.find_all('ul', {'class':'pagination'})[0]
            max_query_page = int(pagination.find_all('li')[-2].text)
            cur_query_page = int(url.split('?page=')[-1])
            main_tags = s.find_all('div', {'class':'news-v3 bg-color-white'})
            for tag in main_tags:
                strong_tag = tag.find_all('strong')[2]
                ans.append(strong_tag.text)
                print("{}/{}. {}".format(cur_query_page, max_query_page,strong_tag.text))
            if max_query_page == cur_query_page or int(cur_query_page) == 600:
                f = open('address_crawl/' + domain + '.txt', 'w')
                for line in ans:
                    f.writelines(line + '\n')
                f.close
                break
            else:
                url = url.split('=')[0] + '=' + str(cur_query_page+1)
    except:
        print("no pagination")        

url = sys.argv[1] + '?page=1' 
print(url) 
get_content(url)
