allMuusika = [
    {"title": "Shape of You", "artist": "Ed Sheeran"},
    {"title": "Blinding Lights", "artist": "The Weeknd"},
    {"title": "Bad Guy", "artist": "Billie Eilish"},
    {"title": "Believer", "artist": "Imagine Dragons"},
    {"title": "Thunder", "artist": "Imagine Dragons"},
    {"title": "Perfect", "artist": "Ed Sheeran"},
]

def otsi_muusikat(item):
    if not item: 
        print ("sisestus on tühi")

    tulemused= []
    for laul in allMuusika:
        if item in laul["title"] or item in laul["artist"]:
            tulemused.append(laul)

    if tulemused:
        print("Leitud")
        for i in tulemused:
            print (i['artist'], ' - ', i["title"])
    else:
        print("laul ei ole saadaval")

otsi_muusikat("Shape of You")
