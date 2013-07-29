#sudo apt-get install python-beautifulsoup 

import urllib2
from BeautifulSoup import BeautifulSoup

url = 'http://www.spotcrime.com/crime/'

data_file = open('cods.txt')
dados = {}

for cod in data_file:
    request = urllib2.Request(url + cod)
    site = urllib2.urlopen(request)
    soup = BeautifulSoup(site)
    line = soup.find(id="main_content").find('h2').text
    print '%s -> %s' % (cod, line)






