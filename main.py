import os
import requests
import shutil
import tabula
import zipfile as zip

#exercicio1
dirname = os.path.dirname(__file__)
def baixarArquivos (link, anexo =''):
    req = requests.get(link)
    try:
        if anexo:
            pass
        else:
            anexo = req.url[link.rfind('/') + 1:]

        with requests.get(link) as req:
            with open(dirname + '/downloads' '/' + anexo, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return anexo
    except Exception as e:
        print(e)
        return None

print('Baixando anexos...')
anexo1 = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf'
baixarArquivos(anexo1, 'anexoI.pdf')
anexo2 = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536.pdf'
baixarArquivos(anexo2, 'anexoII.pdf')
anexo3 = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_III_DC_2021_RN_465.2021.v2.pdf'
baixarArquivos(anexo3, 'anexoIII.pdf')
anexo4 = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf'
baixarArquivos(anexo4, 'anexoIV.pdf')
print('Anexos baixados. (Local: webScrapingGov/downloads)')

#zippando arquivos
print('Compactando...')
try:
    shutil.make_archive('anexos', 'zip', 'downloads')
except Exception as e:
    print(e)
else:
    print('Arquivos compactados. (Local: webScrapingGov/anexos.zip)')

#Extraindo tabelas usando tabula
print('Extraindo tabelas do anexoI.pdf')
tabula.convert_into('.//downloads/anexoI.pdf', 'tabelaAnexoI.csv', output_format='csv', pages='all')
print('Tabelas extraídas (Local: webScrapingGov/tabelaAnexoI.csv)')
print('Compactando arquivo tabelaAnexoI.csv')
#Compactando .csv
csvCompactado = zip.ZipFile("Teste_Rafael Campos de Souza_.zip", 'w')
csvCompactado.write('tabelaAnexoI.csv')
csvCompactado.close()
print('tabelaAnexoI.csv compactado para Teste_Rafael Campos de Souza_.zip (Local: webScrapingGov/Teste_Rafael Campos de Souza_.zip)')
