import requests
import re
from bs4 import BeautifulSoup
import IPython # debug: IPython.embed()

URL = 'https://olavodecarvalho.org/page/%s/'

ARQUIVO_SAIDA = 'olavo.txt'

def main():

    file_saida = open(ARQUIVO_SAIDA, "w")
    for page_number in range(2, 243):

        url = URL % page_number
        print('Baixando página', url)
        page = requests.get(url)
        html = BeautifulSoup(page.content, 'html.parser')
        divs = html.findAll("div", {"class": "post-top"}) 
        links = []
        for div in divs:
            link = div.find_all("a")[0]['href']
            links.append(link)

        print('tamanho de links', len(links))
        for link in links:
            print('Baixando texto de', link)
            pagina_com_conteudo = requests.get(link)
            html_com_conteudo = BeautifulSoup(pagina_com_conteudo.content, 'html.parser')
            h1 = html_com_conteudo.findAll("h1", {"class": "single-pagetitle"})[0]
            title = h1.decode_contents()
            file_saida.write("\n\n" + title + "\n")
            div_entry = html_com_conteudo.findAll("div", {"class": "entry"})[0]
            p = div_entry.find_all("p")[0].decode_contents()
            file_saida.write(p)

    file_saida.close()

if __name__ == "__main__":
    main()

