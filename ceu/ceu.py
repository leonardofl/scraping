#coding=utf8

# Copyright (C) 2013:
# léo: leonardofl87@gmail.com
# laura: lauraparente@gmail.com
# ana: caandrada@gmail.com
# maria: mariajzelada@gmail.com
# fernanda: fecarpe@gmail.com
# nina: nweingrill@gmail.com
#
# ceu.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ceu.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ceu.py.  If not, see <http://www.gnu.org/licenses/>.

# instalando dependências (para o Ubuntu):
# sudo apt-get install python-beautifulsoup 

import urllib2
import urllib
from BeautifulSoup import BeautifulSoup

# Etapa 1: pegar os dados

mes = "07"
unidade_ceu = "butanta"
URL = "http://portalsme.prefeitura.sp.gov.br/documentos/programacao/prog%s_%s.htm" % (mes, unidade_ceu)

request = urllib2.Request(URL)
response = urllib2.urlopen(request)
the_page = response.read()
soup = BeautifulSoup (the_page)
table = soup.find("table")
titulo_bloco1 = "PROGR" 
titulo_bloco2 = "CULTURAL"
trs = table.findAll ("tr")
counter = 0
achei_titulo = False
estou_dados = False
branco = "&nbsp;"
dados = []
for tr in trs :
   texto_linha=tr.text
   if titulo_bloco1 in texto_linha and titulo_bloco2 in texto_linha:
      achei_titulo = True
   if achei_titulo : 
      counter = counter + 1
   if counter == 3 : 
      estou_dados = True
   if branco in texto_linha:
      estou_dados = False
   if estou_dados:
      tds = tr.findAll ("td")
      dados_linha = {}
      dados_linha[ "atividade" ] = tds[0].text
      dados_linha[ "data"] = tds[2].text
      dados_linha[ "horario" ] = tds[3].text
      dados_linha[ "tipo" ] = tds[4].text
      dados_linha[ "publico" ] = tds[6].text
      dados.append(dados_linha)
   
# Etapa 2: processar os dados

atividades_por_tipo = {}
for dados_linha in dados :
    tipo = dados_linha ["tipo"]     
    if tipo in atividades_por_tipo :
        quantidade = atividades_por_tipo[tipo]
    else :
        quantidade = 0
    quantidade = quantidade + 1
    atividades_por_tipo[tipo] = quantidade

# Etapa 3: visualizar os dados

for tipo, quantidade in atividades_por_tipo.items():
    print '%s : %d' % (tipo.replace('\r\n',''), quantidade)
  
    

      

   

