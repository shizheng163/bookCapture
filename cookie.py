import sys

cookie = None

def getCookie():
    global cookie
    if cookie != None:
        return cookie
    try:
        with open('.cookie', 'r', encoding='utf-8') as f:
            cookie = f.read()
    except:
        cookie = ''
        print("Unexpected error:", sys.exc_info()[0])
    return cookie
