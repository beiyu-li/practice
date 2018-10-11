#coding:utf-8
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import requests
import os
import urllib2
from bs4 import BeautifulSoup


# load_html="http://bamboo.calix.local/browse/MBAXOS31-CI1"
html_home_url_yongye='https://www.xxbiquge.com/77_77268/'
html_home_url_yongye='https://www.biqubao.com/book/15040/'
# session=requests.session()
path=r'C:\\Python27\\Scripts\\ftp\\'
filename_chenyuan='yexingzhe.txt'
html_home_url='https://www.xxbiquge.com'
html_home_url_biquege='https://www.biqubao.com/'
html_home_url_chenyuan='https://www.xxbiquge.com/77_77268/'
html_home_url_yuanxue='https://www.biqubao.com/book/17915/'
di=u'第'
zhang=u'章'


##reuquest function
def request_page_content(load_html):
    page = requests.get(load_html)
    # print page.content
    return page
# request_page_content(html_home_url_yongye)
# print url_content
# page_content=request_page_content(html_home_url_yongye)

def get_chapter_list(load_html):
    page = requests.get(load_html)
    page_content=page.content
    soup = BeautifulSoup(page_content)
    chapter_list = []
    # get all chapter list and chapter name
    for string in soup.select('dd'):
        for item in string('a'):
            print (item.get_text())
            print (item.get('href'))
            chapter_list.append((item.get('href'),item.get_text()))
    print (chapter_list)
    return chapter_list

def get_text(html,filename,home_url):
    # page = urllib2.urlopen(home_url+html[0], timeout=10)
    # data = page.read()
    page = requests.get(home_url+html[0])
    data=page.content
    soup = BeautifulSoup(data)
    for title in soup.select('div[id="content"]'):
        print (title.get_text())
        content =title.get_text()
    print ('chapter content is %s' %content)
    if not content:
        print ('no context found')
    else:
        f = open(path + filename, 'ab+')
        my_content = content
        print ("the chapter name is %s" %html[1])
        print ("my_content is %s" %my_content)
        # write chapter name
        # f.write('\n\n'+di+' '+html[1]+" "+zhang+'\n\n')
        f.write('\n\n'+html[1]+'\n\n')
        f.write(my_content)
        f.close()
        return content

def download_all_chapter(html,filename,home_url):
    chapter_list_new=get_chapter_list(html)
    for item in chapter_list_new:
        if item==None:
            print ("chapter not found")
        else :
            print ("current chapter is %s" %item[0])
            # print (unicode("chapter name is %s" %item[1],'gbk'))
            get_text(item,filename,home_url)


# get_chapter_list(html_home_url_yongye)
download_all_chapter(html_home_url_yuanxue,filename_chenyuan,html_home_url_biquege)