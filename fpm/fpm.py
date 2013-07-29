# coding=utf8

#coding=utf8

# Copyright (C) 2013:
# Leonardo Leite, leonardofl87@gmail.com
#
# fpm.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# fpm.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ceu.py.  If not, see <http://www.gnu.org/licenses/>.

# dependências:
# sudo apt-get install python-beautifulsoup 

import urllib2
import urllib
from BeautifulSoup import BeautifulSoup
from django.utils.encoding import smart_str

URL = 'http://www3.tesouro.gov.br/estados_municipios/municipios_novosite.asp'

ESTADOS = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

ANOS = ["2000", "2001", "2002", "2003", "2004", "2005", "2006"]

MESES = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

f = open('fpm.csv', 'w')

def process_page(estado, ano, mes):
    values = {'P_UF' : estado, 'P_ANO' : ano, 'P_MES' : mes, 'P_FUNDOS' : 'FPM', 'ORMATO' : 'TELA', 'ente' : '%'}
    data = urllib.urlencode(values)
    request = urllib2.Request(URL, data)
    response = urllib2.urlopen(request)
    the_page = response.read()
    the_page = the_page.replace('</tr>', '</tr><tr>').replace('ID="Table5">', 'ID="Table5"><tr>')
    soup = BeautifulSoup(the_page)
    table = soup.find(id='Table5')
    rows = table.findAll('tr')
    for row in rows[1:len(rows)-2]:
        municipio = row.find('p').text
        fpm = row.findAll('td')[1].text.strip()
        line = '%s; %s; %s; %s; %s;\n' % (municipio, estado, fpm, ano, mes)
        line = smart_str(line)
        f.write(line)

f.write('Município; Estado; FPM; Ano; Mês;\n')

for estado in ESTADOS:
    print estado
    if estado != "DF":
        for ano in ANOS:
            for mes in MESES:
                process_page(estado, ano, mes)

f.close()

