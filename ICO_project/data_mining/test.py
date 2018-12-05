
import urllib.request
import re
import os



def getFile(target_url):
    file_name = 'haha.pdf'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    req = urllib.request.Request(url=target_url, headers=headers)
    u = urllib.request.urlopen(req)

    f = open(file_name, 'wb')

    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        f.write(buffer)
    f.close()
    print ("Sucessful to download" + " " + file_name)

os.mkdir('/users/barry/desktop/pdf_download')
os.chdir(os.path.join(os.getcwd(), '/users/barry/desktop/pdf_download'))

url = 'https://sirinlabs.com/media/SIRINLABS_-_White_Paper.pdf'
getFile(url)
