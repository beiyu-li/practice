#coding=utf-8
import re
# import urllib
import os
import urllib2



path='C:\\Python27\\Scripts\\ftp\\'
filename_qiusuo='qiusuo.txt'
filename_yongye='guzhenren1.txt'
html_home_url='https://www.xxbiquge.com'
html_home_url_yongye='https://www.xbiquge6.com/0_866/'
'https://www.xbiquge6.com/0_866/'
#reg, first group used to find the chapter html
reg_biquge=r'<dd><a href="(.*?)">(.*?)</a></dd>'
reg_content=r'<div id="content">([\s+\S+]+?)</div>'

def get_text(html,filename,home_url):
    # content_reg = r'<div id="content">([\s+\S+]+?)</div>'
    page = urllib2.urlopen(home_url+html[0], timeout=30)
    data = page.read()
    # print data
    # html_contend=urllib.urlopen(home_url+html[0]).read()
    content = re.findall(reg_content, data)
    print 'chapter content is %s' %content
    if not content:
        print 'no context found'
    else:
        f = open(path + filename, 'ab+')
        my_content = content[0].replace("<br />","\r\n")
        print "my_content is %s" %my_content
        # my_content =my_content .replace("<br />","\r\n")
        my_content = my_content.replace("&nbsp;"," ")
        my_content = my_content.replace("< br / >", "\r\n")
        my_content = my_content.replace("<br/><br/>", "\r\n")
        my_content = my_content.replace(" "," ")
        f.write('\n\n'+html[1]+'\n\n')
        f.write(my_content)
        f.close()
        return content

#
# soup=BeautifulSoup(context)
# content=soup.find_all('title',context)
# print content

# get_text(html_yongye_chapter_1)

def get_chapter_list(html):
    page = urllib2.urlopen(html, timeout=10)
    data = page.read()
    chapter_list=re.findall(reg_biquge,data)
    print chapter_list
    return chapter_list

def get_slice_of_new_list(origin_list,chapter_want2_start):
    list = origin_list
    for item in list:
        for element in item:
            if chapter_want2_start in element:
                print element
                print 'chapter want2 start found'
                print list.index(item)
                index = list.index(item)
    new_list = list[index::]
    return new_list


def download_all_chapter(html, filename, home_url, new_chapter=None):
    chapter_list_new=get_chapter_list(html)
    if new_chapter: ###download from new chapter, not from the chapter 1
        chapter_list_new = get_slice_of_new_list(chapter_list_new,new_chapter)
    else:
        pass
    for item in chapter_list_new:
        if item==None:
            print "chapter not found"
        else :
            print "current chapter is %s" %item[0]
            # print unicode("chapter name is %s" %item[1],'gbk')
            get_text(item,filename,home_url)


download_all_chapter(html_home_url_yongye,filename_yongye,html_home_url,new_chapter='8795701.html')
# get_chapter_list(html_home_url_yongye)
# get_text('/1_1797/1159432.html',filename_yongye,html_home_url)
