import requests
from bs4 import BeautifulSoup


from functions import clearConsole, welcome

url = "https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?"

codigos = ['OQ366239704BR']#,'OS474220058BR']
clearConsole()
welcome()

if(len(codigos) == 1):
    print(f'Foi encontrado um objeto:')
else:
    print(f'Foram encontrados {len(codigos)} objetos:')

for i in codigos:
    try:

        req = requests.post(url=url, data={"objetos": i})
        soup = BeautifulSoup(req.text, 'html.parser')

        htmlobjpostagem = soup.find(id='EventoPostagem')
        htmlobjsaiuentrega = soup.find(id='UltimoEvento')
        htmlobjprevisaoentrega = soup.find(id='DataEntrega')

        textopostagem = htmlobjpostagem.strong.text
        textosaiuentrega = htmlobjsaiuentrega.strong.text
        textoprevisaoentrega = htmlobjprevisaoentrega.strong.text

        datapostagem = htmlobjpostagem.text.split()[-1]
        datasaiuentrega = htmlobjsaiuentrega.text.split()[-1]
        dataprevisaoentrega = htmlobjprevisaoentrega.text.split()[-1]


        print('=-------------------------------------------------------------------------=>')
        print(f'\033[1m {i} \033[0m\n')
        print(textopostagem)
        print(datapostagem)

        print(textosaiuentrega)
        print(datasaiuentrega)

        print(textoprevisaoentrega)
        print(dataprevisaoentrega)
        print('<=-------------------------------------------------------------------------=')


        # htmlobj = soup.find(id='EventoPostagem')
        # textoobj = htmlobj.strong.text
        # dataobj = htmlobj.text.split()[-1]
    except Exeption as e:
        print(e)