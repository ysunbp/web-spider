import urllib2

user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1; Trident/5.0;' #IE 9.0
headers = {'User-Agent':user_agent}
def write_file(file_name, text):
    print 'saving files' + file_name
    f = open(file_name, 'w+')
    f.write(text)
    f.close()
def load_page(url):

    req = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(req)
    html = response.read()
    return html
def tieba_spider(url, begin_page, end_page):


    for i in range(begin_page, end_page+1):
        pn = 50 * (i - 1)
        html = load_page(url+str(pn))
        file_name ='D:\\web_spider\\'+str(i) +'.html'
        print 'downloading' + str(i) + 'th webpage'
        write_file(file_name, html)
if __name__ == '__main__':
    bdurl = str(raw_input('input url:'))
    begin_page = int(raw_input('input begin page'))
    end_page = int(raw_input('input end page'))
    tieba_spider(bdurl, begin_page, end_page)
