
from flask import Flask, render_template, request
import random

from datetime import datetime



#Funktsioon failist osalejate lugemiseks ja sõnastikku kirjutamiseks.
def failist_sõnastikku(fnimi):
    sonastik = {}
    with open(fnimi, 'r', encoding='utf-8') as fail:
        for rida in fail:
            andmed = rida.strip().split(',')
            if len(andmed) >= 2:
                osaleja, arv = andmed
                # Teisenda 'arv' stringist int-iks
                sonastik[osaleja] = int(arv)
    return sonastik

def voitja(fnimi):
    sonastik = failist_sõnastikku(fnimi)
    # Tagasta maksimaalne võitja nimi, kasutades sõnastiku väärtust
    return max(sonastik, key=sonastik.get)



        
def sõnastikust_järjendi(sonastik):
    jar = []
    for i in sonastik: 
        jar.append(i)
    return jar

def hääleta_ja_salvesta(fnimi, kasutaja_hääl):
    sonastik = failist_sõnastikku(fnimi)
    print(kasutaja_hääl) 
    for osaleja, tulemus in sonastik.items():
        if osaleja == kasutaja_hääl:
            sonastik[osaleja] += 1
    # Salvesta tulemused
    with open(fnimi, 'w', encoding='utf-8') as fail:
        for osaleja, tulemus in sonastik.items():
            fail.write(osaleja + ',' + str(tulemus) + '\n') 


app = Flask(__name__)
 
@app.route("/")
def index():
    sonastik = failist_sõnastikku('nimed.txt')
    järjend = sõnastikust_järjendi(sonastik)
    return render_template("index.html", osaleja=järjend)
@app.route('/handle_button_click', methods=['POST'])
def handle_button_click():
    clicked_button = request.form['clicked_button']
    print(f"Nupp {clicked_button} on vajutatud!")
    
    #saa kasutaja vastus paremale kujule
    kasutaja_hääl = request.form.get('clicked_button')
    hääleta_ja_salvesta('nimed.txt', kasutaja_hääl)
    return render_template("clicked_button.html", valik=kasutaja_hääl)

@app.route("/tulemus")
def tulemus():
    esimene = voitja("nimed.txt")
    return esimene
 
if __name__ == "__main__":
    app.run(debug=True)
    
