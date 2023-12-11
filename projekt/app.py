
from flask import Flask, render_template, request
import random

from datetime import datetime
#Funktsioon võitja leidmiseks
def voitja(fnimi):
    return max(failist_sõnastikku(fnimi))

#Funktsioon failist osalejate lugemiseks ja sõnastikku kirjutamiseks.
def failist_sõnastikku(fnimi):
    sonastik = {}
    with open(fnimi, 'r', encoding='utf-8') as fail:
        for e in fail:
          andmed = e.strip().split(',')
          if len(andmed) >= 2:
              osaleja, arv = andmed
              sonastik[osaleja] = int(arv) 
    return sonastik
 
def hääleta_ja_salvesta(andmed, lõpp_kuupäev):
    #Et inimesed ei saaks peale lõppkuupäeva hääletada
    if datetime.now() >= lõpp_kuupäev:
        print("Hääletamine on lõppenud.")
        return
    
    print("Hääleta oma lemmiku poolt:")
    for i, (osaleja, arv) in enumerate(andmed.items(), start=1):
        print(str(i) + '. ' + osaleja)

    valik = int(input("Vali number: "))

    if 1 <= valik <= len(andmed):
        valitud_osaleja = list(andmed.keys())[valik - 1]
        andmed[valitud_osaleja] += 1
        print('Sina hääletasid ' + valitud_osaleja + ' poolt.')

        # Salvesta tulemused
        with open('proje.txt', 'w', encoding='utf-8') as fail:
            for osaleja, arv in andmed.items():
                fail.write(osaleja + ',' + str(arv) + '\n')
    else:
        print("Vigane valik.")
        
        
        
def sõnastikust_järjendi(andmed):
    jar = []
    for i in andmed: 
        jar.append(i)
    return jar




 
failinimi = 'nimed.txt'
andmed = failist_sõnastikku(failinimi)
lõpp_kuupäev = datetime(2024, 12, 14)
hääleta_ja_salvesta(andmed, lõpp_kuupäev)

app = Flask(__name__)
 
@app.route("/")
def index():
    järjend = sõnastikust_järjendi(andmed)
    return render_template("index.html", osaleja=järjend)
@app.route('/handle_button_click', methods=['POST'])
def handle_button_click():
    clicked_button = request.form['clicked_button']
    print(f"Nupp {clicked_button} on vajutatud!")
    return "Olete hääletanud2"

@app.route("/teine")
def teine():
    materjal = failist_sõnastikku(failinimi)
    return materjal
 
if __name__ == "__main__":
    app.run(debug=True)
    
