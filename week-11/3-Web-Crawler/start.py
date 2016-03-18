from bs4 import BeautifulSoup
import requests
from multiprocessing import Queue


def is_status_ok(status):
    return str(status) == '200'

que = Queue()

start = 'http://register.start.bg/'
que.put(start)

def craw():
    base = que.get()

    r = requests.get(base)
 
    print ('start with {}'.format(r.url))
    print ('links --------------------')
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
 
    all_websites = soup.find_all('a', href=True)
    for x in all_websites:
       
        #print ('href = {}'.format(x['href']))
        uri = x['href']
        #print (uri)
        if 'http' not in uri:
           url = base + uri
        else:
            url = uri

        try:
            print (url)
            req = requests.get(url)
            isActive = is_status_ok(req.status_code)
            if isActive:
               
                # print ('-------')
                # print ('uri: {}'.format(url))
                # print ('domain: {}'.format(req.url))
                # print ('-------')
                if base not in req.url:
                    que.put(req.url)
        except requests.exceptions.ConnectionError:
                # print ('bad url: {}'.format(url))
                # bad += 1
                continue
        except requests.exceptions.TooManyRedirects:
                # print ('{} looped, skip it'.format(req.url))
                continue

        # print ("status: {} ".format(req.status_code))
        print (que.qsize())
        if que.qsize() > 15:
            break
    if que.qsize():
        craw()

def main():
    craw()

if __name__ == '__main__':
    main()
