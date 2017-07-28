from bs4 import BeautifulSoup
import requests
import lxml
import re


# http://www.yes24.com/24/Category/More/001001003?ElemNo=3&ElemSeq=1
# 제목 : category_layout > tbody > tr:nth-child(1) > td.goodsTxtInfo > p:nth-child(1) > a:nth-child(1)
# 저자 : category_layout > tbody > tr:nth-child(1) > td.goodsTxtInfo > div > a:nth-child(1)
# 출판사 : category_layout > tbody > tr:nth-child(1) > td.goodsTxtInfo > div > a:nth-child(2)
# 출시일 : category_layout > tbody > tr:nth-child(1) > td.goodsTxtInfo > div 어떻게 뽑지요
# 가격 : category_layout > tbody > tr:nth-child(1) > td.goodsTxtInfo > p:nth-child(3) > span.priceB

# 리스트 contents : 제목, 저자, 출판사, 출시일, 가격


def main():
    book_list = []
    date_re = re.compile(r'\d{4}년 \d{2}월')  # 정규식

    res = requests.get('http://www.yes24.com/24/Category/More/001001003?ElemNo=3&ElemSeq=1')

    soup = BeautifulSoup(res.text, 'lxml')

    tag = soup.find(attrs={'id': 'category_layout'}).find_all('tr')[0] \
        .find('td', attrs={'class': 'goodsTxtInfo'})

    # # 제목 : category_layout > tbody > tr:nth-child(1) > td.goodsTxtInfo > p:nth-child(1) > a:nth-child(1)
    # title_elem_cat = tag.find_all('p')[0].find_all('a')[0].text
    # # print("제목 : ", title_elem_cat)
    #
    # # 저자 : category_layout > tbody > tr:nth-child(1) > td.goodsTxtInfo > div > a:nth-child(1)
    # writer_ele_cat = tag.find('div').find_all('a')[0].text
    # # print("저자 : ", writer_ele_cat)
    #
    # # 출판사 : category_layout > tbody > tr:nth-child(1) > td.goodsTxtInfo > div > a:nth-child(2)
    # publisher_ele_cat = tag.find('div').find_all('a')[1].text
    # # print("출판사 : ", publisher_ele_cat)
    #
    # # 출시일 TODO : 정규식으로 search
    # public_date_ele_cat = tag.find('div').text
    # pub_date = date_re.findall(public_date_ele_cat)  #정규식 적용
    # # print(pub_date)
    #
    # # 가격 : category_layout > tbody > tr:nth-child(1) > td.goodsTxtInfo > p:nth-child(3) > span.priceB
    # cost_ele_cat = tag.find_all('p')[1].find('span', attrs={'class': 'priceB'}).text
    # # print("가격 : ", cost_ele_cat)
    #
    # book_list.append(title_elem_cat)
    # book_list.append(writer_ele_cat)
    # book_list.append(publisher_ele_cat)
    # book_list.append(pub_date[0])
    # book_list.append(cost_ele_cat)
    #
    # print(book_list)

    elem_tr_list = soup.find(attrs={'id': 'category_layout'}).find_all('tr')
    public_date_ele_cat = tag.find('div').text

    for tr in elem_tr_list:

        if tr.find('td', attrs={'class': 'goodsTxtInfo'}):
            title_elem_cat = tr.find('td', attrs={'class': 'goodsTxtInfo'}).find_all('p')[0].find_all('a')[0].text
            writer_ele_cat = tr.find('td', attrs={'class': 'goodsTxtInfo'}).find('div').find_all('a')[0].text
            publisher_ele_cat = tr.find('td', attrs={'class': 'goodsTxtInfo'}).find('div').find_all('a')[1].text

            pub_date = date_re.findall(public_date_ele_cat)  # 정규식 적용
            cost_ele_cat = tr.find('td', attrs={'class': 'goodsTxtInfo'}).find_all('p')[1].find('span', attrs={
                'class': 'priceB'}).text
            print(title_elem_cat, writer_ele_cat, publisher_ele_cat, pub_date, cost_ele_cat)

        else:
            continue


if __name__ == '__main__':
    main()

