import urllib2
from BeautifulSoup import BeautifulSoup

URLS = {
    'PLEX': 'http://www.windowsphone.com/es-es/store/app/plex/5bfafc1b-c9f4-4e85-b89f-3947d650c382',
}

def get_data(url):
    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close()
    return data

def get_price(soup):
    app_data = soup.findAll('div', {'class': 'app'})[0]
    price = app_data.findAll('span', {'itemprop': 'price'})[0].text
    right_price = float((price.split()[0]).replace(',','.')) 
    return right_price 
    

def fetch_urls():
    for name,url in URLS.iteritems():
        data = get_data(url)
        soup = BeautifulSoup(data)
        price = get_price(soup)
        print u"Item: {} - Price: {}".format(name, price)

if __name__ == '__main__':
    fetch_urls()
