import requests
from bs4 import BeautifulSoup


from functions import clearConsole, welcome

url = "https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?"

codigos = ['OQ366239704BR','OS474220058BR']
clearConsole()
welcome()

print(f'Foram encontrados {len(codigos)} objetos!')

for i in codigos:
    try:

        req = requests.post(url=url, data={"objetos": i})
        soup = BeautifulSoup(req.text, 'html.parser')
        htmlobj = soup.find(id='UltimoEvento')
        textoobj = htmlobj.strong.text
        dataobj = htmlobj.text.split()[-1]

        print('=-------------------------------------------------------------------------=>')
        print(f'|\033[1m {i} \033[0m                                                           |')
        print(f'| {textoobj} no dia {dataobj}               |')
        print('<=-------------------------------------------------------------------------=')
    except Exeption as e:
        print(e)