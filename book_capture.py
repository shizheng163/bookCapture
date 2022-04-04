import urllib.request, urllib.parse
import re
import cookie

userAgent = 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'

def listBooks(taglink, start):
    print(taglink, start)
    url = 'https://book.douban.com'+ urllib.parse.quote(taglink) + '?start='+str(start) + '&type=T'
    header = {'User-Agent': userAgent}
    cookieVal = cookie.getCookie()
    if len(cookieVal) != 0:
        header['Cookie'] = cookieVal
    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request)
    booksHtml = response.read().decode('utf-8')
    regex = '\s*<a href="(https://book.douban.com/subject/.*)/" title="(.*)" '
    booksElements = re.findall(regex, booksHtml)
    rlt = []
    for bookLine in booksElements:
        rlt.append(bookLine[0])
    return rlt

def captureBooksLink(taglink):
    start=0
    incr=20
    books = []
    while True:
        pageBooks = listBooks(taglink, start)
        start+=incr
        if len(pageBooks) == 0:
            break
        books.extend(pageBooks)
    return books

def captureBook(url):
    regex = '\s*<span class="pl">(.*)</span>:?(\s*<a.*href=".*">(.*)</a>|(.*)<br/>)'
    header = {'User-Agent': userAgent}
    cookieVal = cookie.getCookie()
    if len(cookieVal) != 0:
        header['Cookie'] = cookieVal
    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request)
    bookHtml = response.read().decode('utf-8')
    bookElements = re.findall(regex, bookHtml)
    rlt = {}
    for info in bookElements:
        key = info[0]
        value = info[2] if(len(info[2]) != 0)  else info[3]
        rlt[key.strip()] = value.strip()
    return rlt
