
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
    #hääletamise lõppemine kuupäev
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


failinimi = 'proje.txt'
andmed = failist_sõnastikku(failinimi)
hääleta_ja_salvesta(andmed)
