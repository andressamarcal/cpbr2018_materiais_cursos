from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve
u1 = 'https://www.al.sp.gov.br/alesp/pesquisa-proposicoes/?direction=acima&lastPage=5167&currentPage='
u2 = '&act=detalhe&idDocumento=&rowsPerPage=10&currentPageDetalhe=1&tpDocumento=&method=search&text=&natureId=4005&legislativeNumber=&legislativeYear=&natureIdMainDoc=loa&anoDeExercicio=&legislativeNumberMainDoc=&legislativeYearMainDoc=&strInitialDate=01%2F01%2F2010&strFinalDate=31%2F12%2F2014&author=&supporter=&politicalPartyId=&tipoDocumento=&stageId=&strVotedInitialDate=&strVotedFinalDate='
base = 'https://www.al.sp.gov.br'
def baixa_pdf(u, nome):
    url = base + u
    fim = nome.find('-') - 1
    nome = nome.replace('/', '-')
    nome = nome[16:fim]
    p = urlopen(url)
    s = bs(p.read(), 'html.parser')
    x = s.find('table', class_ = 'tabelaDados')
    if '(não existe documento)' in str(x):
        print ('Sem documento:', nome)
        return
    pdf = x.find('a')['href']
    urlretrieve(pdf, nome+'.pdf')
    
for k in range(5167):
    url = u1+str(k)+u2
    p = urlopen(url)
    print ('Página:', k)
    s = bs(p.read(), 'html.parser')
    x = s.find('table', class_ = 'tabela')
    emendas = x.find_all('tr')
    for e in emendas[1:]:
        baixa_pdf (e.find('a')['href'],
                   e.find('strong').get_text().strip())

    
