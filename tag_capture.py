import urllib.request
import re
import cookie

userAgent = 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'


def captureTags():
    url = 'https://book.douban.com/tag/'
    header = {'User-Agent': userAgent}
    cookieVal = cookie.getCookie()
    if len(cookieVal) != 0:
        header['Cookie'] = cookieVal
    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request)
    tagHtml = response.read().decode('utf-8')
    regex = '.*name="(.*)" class="tag-title-wrapper">|<a href="(/tag/.*)">(.*)</a>'
    tagElements = re.findall(regex, tagHtml)
    rlt = []
    curCatalogDict = None
    for line in tagElements:
        if len(line[0]) != 0:
            if curCatalogDict != None:
                rlt.append(curCatalogDict)
            curCatalogDict = { 'name': line[0], 'tags': []}
        else:
            curCatalogDict['tags'].append({'tagName': line[2], 'link': line[1]})
    if curCatalogDict != None:
        rlt.append(curCatalogDict)
    return rlt