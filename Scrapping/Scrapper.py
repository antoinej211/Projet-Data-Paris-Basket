import pandas as pd
import cloudscraper
from io import StringIO 

url = "https://www.proballers.com/fr/basketball/equipe/13219/paris"

scraper = cloudscraper.create_scraper(browser={'browser': 'chrome', 'platform': 'windows', 'desktop': True})
reponse = scraper.get(url)

print("Code statut :", reponse.status_code)

if reponse.status_code == 200:
    html_io = StringIO(reponse.text)
    
    tableaux = pd.read_html(html_io)
    print(f"{len(tableaux)} tableaux sur la page")
    
    if len(tableaux) > 0:
        df = tableaux[0]
        print(df.head())
        
        df.to_csv("paris_basket_brut.csv", index=False, sep=';', encoding='utf-8-sig')
        print("Fichier sauvegardé")