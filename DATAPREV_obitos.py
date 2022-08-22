#### DATAPREV - Óbitos ####

## Bibliotecas
import sys
import requests
import json
import pandas as pd

## Função para gerar novo TOKEN - Autenticação OAuth 2.0
def get_new_token():
    auth_server_url = "https://api.dataprev.gov.br/token"
    client_id = 'V_h32rLjOsvOm2gPGoU3_dQwtoMa'
    client_secret = 'Wumr_sDUCjNuLdlx8rTSy8lU5NAa'
    token_req_payload = {'grant_type': 'client_credentials'}

    token_response = requests.post(auth_server_url,
    data=token_req_payload, verify=False, allow_redirects=False,
    auth=(client_id, client_secret))

    # Verifica o status_code do response
    if token_response.status_code !=200:
        print(" Falha ao obter ain token from the OAuth 2.0 server", file=sys.stderr)
        sys.exit(1)
    else:
        print("Sucesso ao obter novo token")
    
    tokens = json.loads(token_response.text)
    return tokens['access_token']

## Importanto uma lista de CPF para teste    
lista_cpf = pd.read_excel('Dados_exemplo.xlsx')

## Criando dataframe para receber os resultado
Resultado = pd.DataFrame(columns = ['matricula',
                                    'dataLavratura',
                                    'dataInsercao',
                                    'nomeFalecido', 
                                    'dataNascimento', 
                                    'sexoFalecido', 
                                    'dataObito',
                                    'uf_naturalidade',
                                    'municipio_naturalidade',
                                    'codigoIBGE',
                                    'mae',
                                    'pai',
                                    'CPF',
                                    'dataEmissao_cpf',
                                    'outro_doc',
                                    'numero_doc',
                                    'dataEmissao_doc'])

## Parametros do site
payload={'Linha=Regi%E3o%2FUF_de_notifica%E7%E3o&Coluna=--N%E3o-Ativa--&Incremento=Casos_confirmados&Arquivos=sifcbr10.dbf&pesqmes1=Digite+o+texto+e+ache+f%E1cil&SAno_Diagn%F3stico=TODAS_AS_CATEGORIAS__&pesqmes2=Digite+o+texto+e+ache+f%E1cil&SM%EAs_Diagn%F3stico=TODAS_AS_CATEGORIAS__&SRegi%E3o_de_notifica%E7%E3o=TODAS_AS_CATEGORIAS__&pesqmes4=Digite+o+texto+e+ache+f%E1cil&SUF_de_notifica%E7%E3o=TODAS_AS_CATEGORIAS__&pesqmes5=Digite+o+texto+e+ache+f%E1cil&SMunic%EDpio_de_notifica%E7%E3o=TODAS_AS_CATEGORIAS__&pesqmes6=Digite+o+texto+e+ache+f%E1cil&SCapital_de_notifica%E7%E3o=TODAS_AS_CATEGORIAS__&pesqmes7=Digite+o+texto+e+ache+f%E1cil&SRegi%E3o_de_Sa%FAde_%28CIR%29_de_notif=TODAS_AS_CATEGORIAS__&pesqmes8=Digite+o+texto+e+ache+f%E1cil&SMacrorreg.de_Sa%FAde_de_notific=TODAS_AS_CATEGORIAS__&pesqmes9=Digite+o+texto+e+ache+f%E1cil&SMicrorregi%E3o_IBGE_de_notific=TODAS_AS_CATEGORIAS__&pesqmes10=Digite+o+texto+e+ache+f%E1cil&SReg.Metropolit%2FRIDE_de_notific=TODAS_AS_CATEGORIAS__&pesqmes11=Digite+o+texto+e+ache+f%E1cil&STerrit_da_Cidadania_de_notific=TODAS_AS_CATEGORIAS__&pesqmes12=Digite+o+texto+e+ache+f%E1cil&SMesorregi%E3o_PNDR_de_notific=TODAS_AS_CATEGORIAS__&SAmaz%F4nia_Legal_%28notifica%E7%E3o%29=TODAS_AS_CATEGORIAS__&SSemi%E1rido_%28notifica%E7%E3o%29=TODAS_AS_CATEGORIAS__&SFaixa_de_Fronteira_%28notific%29=TODAS_AS_CATEGORIAS__&SZona_de_Fronteira_%28notific%29=TODAS_AS_CATEGORIAS__&SMunic_extrem_pobreza_%28notific%29=TODAS_AS_CATEGORIAS__&SRegi%E3o_de_resid%EAncia=TODAS_AS_CATEGORIAS__&pesqmes19=Digite+o+texto+e+ache+f%E1cil&SUF_de_resid%EAncia=TODAS_AS_CATEGORIAS__&pesqmes20=Digite+o+texto+e+ache+f%E1cil&SMunic%EDpio_de_resid%EAncia=TODAS_AS_CATEGORIAS__&pesqmes21=Digite+o+texto+e+ache+f%E1cil&SCapital_de_resid%EAncia=TODAS_AS_CATEGORIAS__&pesqmes22=Digite+o+texto+e+ache+f%E1cil&SRegi%E3o_de_Sa%FAde_%28CIR%29_de_resid=TODAS_AS_CATEGORIAS__&pesqmes23=Digite+o+texto+e+ache+f%E1cil&SMacrorreg.de_Sa%FAde_de_resid%EAnc=TODAS_AS_CATEGORIAS__&pesqmes24=Digite+o+texto+e+ache+f%E1cil&SMicrorregi%E3o_IBGE_de_resid%EAnc=TODAS_AS_CATEGORIAS__&pesqmes25=Digite+o+texto+e+ache+f%E1cil&SReg.Metropolit%2FRIDE_de_resid=TODAS_AS_CATEGORIAS__&pesqmes26=Digite+o+texto+e+ache+f%E1cil&STerrit_da_Cidadania_de_resid=TODAS_AS_CATEGORIAS__&pesqmes27=Digite+o+texto+e+ache+f%E1cil&SMesorregi%E3o_PNDR_de_resid%EAnc=TODAS_AS_CATEGORIAS__&SAmaz%F4nia_Legal_%28resid%EAncia%29=TODAS_AS_CATEGORIAS__&SSemi%E1rido_%28resid%EAncia%29=TODAS_AS_CATEGORIAS__&SFaixa_de_Fronteira_%28resid%EAnc%29=TODAS_AS_CATEGORIAS__&SZona_de_Fronteira_%28resid%EAnc%29=TODAS_AS_CATEGORIAS__&SMunic_extrem_pobreza_%28resid%29=TODAS_AS_CATEGORIAS__&SFaixa_Et%E1ria=TODAS_AS_CATEGORIAS__&SRa%E7a=TODAS_AS_CATEGORIAS__&SSexo=3&pesqmes36=Digite+o+texto+e+ache+f%E1cil&SFx_Etaria_M%E3e=TODAS_AS_CATEGORIAS__&pesqmes37=Digite+o+texto+e+ache+f%E1cil&SEscolar_m%E3e=TODAS_AS_CATEGORIAS__&SRealizou_Pr%E9-Natal=TODAS_AS_CATEGORIAS__&SS%EDfilis_materna=TODAS_AS_CATEGORIAS__&pesqmes40=Digite+o+texto+e+ache+f%E1cil&SAno_Inic_Trat_M%E3e=TODAS_AS_CATEGORIAS__&pesqmes41=Digite+o+texto+e+ache+f%E1cil&SMes_Inic_Trat_M%E3e=TODAS_AS_CATEGORIAS__&STrat_parceiro=TODAS_AS_CATEGORIAS__&SClassif._Final=TODAS_AS_CATEGORIAS__&SEvolu%E7%E3o=TODAS_AS_CATEGORIAS__&formato=table&mostre=Mostra': ''}
files=[]

## Chama funcao para gerar o token 
token = get_new_token()

## Percorre a lista de CPF's para realizar consulta 
for i in range(len(lista_cpf['CPF'])):
    verifica = True
    while verifica:    
        # URL para consulta com CPF da lista
        test_api_url = "https://api.dataprev.gov.br/registro-civil-degustacao/v1.0.0/obitos?cpf=" + str(lista_cpf['CPF'][i])

        # Gera headers com o token
        api_call_headers = {'Authorization': 'Bearer ' + token}
        
        # Realiza a consulta
        api_call_response = requests.get(test_api_url, headers=api_call_headers, data=payload, files=files, verify=False)

        # Verifica o status_code do request, se for 
        if api_call_response.status_code == 401:
            token = get_new_token()
            
        else:
            dados = json.loads(api_call_response.content)
            matricula = dados['matricula']
            dataLavratura = dados['dataLavratura']
            dataInsercao = dados['dataInsercao']
            nomeFalecido = dados['nomeFalecido']
            dataNascimento = dados['dataNascimento']
            sexoFalecido = dados['sexoFalecido']
            dataObito = dados['dataObito']
            uf_naturalidade = dados['naturalidade']['uf']
            municipio_naturalidade = dados['naturalidade']['municipio']
            codigoIBGE = dados['naturalidade']['codigoIBGE']
            mae = dados['filiacao'][0]['nome']
            pai = dados['filiacao'][1]['nome']
            cpf = dados['documentos'][0]['numero']
            dataEmissao_cpf = dados['documentos'][0]['dataEmissao']
            outro_doc = dados['documentos'][1]['tipo']
            numero_doc = dados['documentos'][1]['numero']
            dataEmissao_doc = dados['documentos'][1]['dataEmissao']
            
			verifica = False
            
			Resultado = Resultado.append({'matricula':matricula,
                                          'dataLavratura':dataLavratura,
                                          'dataInsercao':dataInsercao,
                                          'nomeFalecido':nomeFalecido, 
                                          'dataNascimento':dataNascimento, 
                                          'sexoFalecido':sexoFalecido, 
                                          'dataObito':dataObito,
                                          'uf_naturalidade':uf_naturalidade,
                                          'municipio_naturalidade':municipio_naturalidade,
                                          'codigoIBGE':codigoIBGE,
                                          'mae':mae,
                                          'pai':pai,
                                          'CPF':cpf,
                                          'dataEmissao_cpf':dataEmissao_cpf,
                                          'outro_doc':outro_doc,
                                          'numero_doc':numero_doc,
                                          'dataEmissao_doc:'dataEmissao_doc}, ignore_index=True)

## Exportando resultado para excel
Resultado.to_excel("Resultado.xlsx",
             sheet_name='Resultado')