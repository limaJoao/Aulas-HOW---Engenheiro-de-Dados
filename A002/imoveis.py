#%%
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
import time


# %%

url = 'https://glue-api.vivareal.com/v2/listings?addressCity=Juiz de Fora&addressLocationId=BR>Minas Gerais>NULL>Juiz de Fora&addressNeighborhood&addressState=Minas Gerais&addressCountry=Brasil&addressStreet&addressZone&addressPointLat=-21.762393&addressPointLon=-43.343467&business=RENTAL&facets=amenities&unitTypes&unitSubTypes&unitTypesV3&usageTypes&listingType=USED&parentId=null&categoryPage=RESULT&includeFields=search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount),page,seasonalCampaigns,fullUriFragments,nearby(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount)),expansion(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount)),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,phones),owners(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount))&size=300&from={}&q&developmentsSize=5&levels=CITY&ref&pointRadius&isPOIQuery'

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "x-domain": "www.vivareal.com.br" 
}

payload = ""


#%%

def get_json(url, i, headersList, payload):
    ret = requests.request("GET", url.format(i), data=payload,  headers=headersList)
    soup = bs(ret.text, 'html.parser')
    return json.loads(soup.text)



# %%
df = pd.DataFrame(columns=[
    'tipo',
    'titulo',
    'bairro',
    'endereco',
    'area',
    'quartos',
    'banheiros',
    'vagas',
    'preco',
    'condominio',
    'link'])



# %%
imovel_id = 0
json_data = get_json(url, imovel_id, headersList, payload)
while len(json_data['search']['result']['listings']) > 0:

    qtd = len(json_data['search']['result']['listings'])
    print(f"Quantidade de imóveis: {qtd}  |  total: {imovel_id}")
    
    for i in range(0,qtd):
        try:
            tipo = json_data['search']['result']['listings'][i]['listing']['unitTypes'][0]
        except:
            tipo = float('nan')

        try:
            titulo = json_data['search']['result']['listings'][i]['listing']['title']
        except:
            titulo = float('nan')
            
        try:
            bairro = json_data['search']['result']['listings'][i]['listing']['address']['neighborhood']
        except:
            bairro = float('nan')
            
        try:
            endereco = json_data['search']['result']['listings'][i]['listing']['address']['street']
        except:
            endereco = float('nan')
            
        try:
            area = float(json_data['search']['result']['listings'][i]['listing']['usableAreas'][0])
        except:
            area = float('nan')
            
        try:
            quartos = float(json_data['search']['result']['listings'][i]['listing']['bedrooms'][0])
        except:
            quartos = float('nan')
            
        try:
            banheiros = float(json_data['search']['result']['listings'][i]['listing']['bathrooms'][0])
        except:
            banheiros = float('nan')
            
        try:
            vagas = float(json_data['search']['result']['listings'][i]['listing']['parkingSpaces'][0])
        except:
            vagas = float('nan')
            
        try:
            preco = float(json_data['search']['result']['listings'][i]['listing']['pricingInfos'][-1]['price'])
        except:
            preco = float('nan')
            
        try:
            condominio = float(json_data['search']['result']['listings'][i]['listing']['pricingInfos'][-1]['monthlyCondoFee'])
        except:
            condominio = float('nan')
            
        try:
            wlink = json_data['search']['result']['listings'][i]['link']['href']
        except:
            wlink = float('nan')


        df.loc[df.shape[0]] = [
            tipo,
            titulo,
            bairro,
            endereco,
            area,
            quartos,
            banheiros,
            vagas,
            preco,
            condominio,
            wlink
        ]

    imovel_id = imovel_id + qtd
    time.sleep(1.5)
    json_data = get_json(url, imovel_id, headersList, payload)

