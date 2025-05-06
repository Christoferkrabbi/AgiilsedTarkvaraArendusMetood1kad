# ## **Ehita samm-sammult "Mini Kalkulaator" iteratiivse meetodi järgi**
#
# ### **Iteratsioon 1 - Lihtne liitmine**
#
# - Kirjuta programm, mis küsib kasutajalt kaks arvu ja tagastab nende summa.
#
def mySum(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a + b
    else:
        print("vale sisestus!")

print(mySum(1,3))

### **Iteratsioon 2 - rohkem tehteid**

# - Lisa lahutamine, korrutamine ja jagamine.
# - Loo valikumenüü (1.liida, 2.lahuta, 3.korruta, 4. jaga).

def myFinalSum(a,b):
    Sisestus = input("1 on et liida, 2 on et lahuta, 3 on et korrutada, 4 on et jagada: Sissesta siia!")
    if isinstance(Sisestus, int) and Sisestus == 1:
        if isinstance(a,int) and isinstance(b,int):
            return a + b
    elif isinstance(Sisestus, int) and Sisestus == 2:
        if isinstance(a,int) and isinstance(b,int):
            return a - b
    elif isinstance(Sisestus, int) and Sisestus == 3:
        if isinstance(a,int) and isinstance(b,int):
            return a * b
    elif isinstance(Sisestus, int) and Sissestus == 4:
        if isinstance(a,int) and isinstance(b,int):
            return a / b
    else:
        print("vale sisestus!")
        
print(myFinalSum(Sisestus = input("1 on et liita, 2 on et lahuta, 3 on et korrutada, 4 on et jagada: Sissesta siia!"),1,3))

### **Iteratsioon 3 - Sisendi valdieerimine**
#
# - Kontrolli, et kasutaja sisestab numbreid

def main():
    valik = input("Mida Teie Soovite?")
    if isinstance(valik, int) and valik == 1:
        a = input("Sissesta esimene Number:")
        b = input("Sissesta teine Number:")
        if isinstance(a,int) and isinstance(b,int):
            myArr[0] += 1
            result = myEndSum(a,b)
            print("tulemus on: ", result)
    elif isinstance(valik, int) and valik == 2:
        a = input("Sissesta esimene Number:")
        b = input("Sissesta teine Number:")
        if isinstance(a,int) and isinstance(b,int):
            myArr[1] += 1
            result = myEndSum(a,b)
            print("tulemus on: ", result)
            print(myFinalSum(valik,a,b))
    elif isinstance(valik, int) and valik == 3:
        a = input("Sissesta esimene Number:")
        b = input("Sissesta teine Number:")
        if isinstance(a,int) and isinstance(b,int):
            myArr[2] += 1
            result = myEndSum(a,b)
            print("tulemus on: ", result)
            print(myFinalSum(valik,a,b))
    elif isinstance(valik, int) and valik == 4:
        a = input("Sissesta esimene Number:")
        b = input("Sissesta teine Number:")
        if isinstance(a,int) and isinstance(b,int):
            myArr[3] += 1
            result = myEndSum(a,b)
            print("tulemus on: ", result)
            print(myFinalSum(valik,a,b))
    else:
        print("Vabandust aga seda valikud pole olemas!")
main()

# **Iteratsioon 4 - Loogiline Täiendus
def displayInfo():
    print("kokku oli ", sum(myArr))
    print("summerimine töötas: ", myArr[0], "korda")
    print("lahutamine oli ", myArr[1], "korda")
    print("koorutamine oli ", myArr[2], "korda")
    print("jagamine oli ", myArr[3], "korda")

myArr = [0,0,0,0]


# inkrement 1 - Patsientide lisamine ja vaatamine
# inkrement 2 - Arstide lisamine ja vaatamine
# inkrement 3 - kohtumiste haldamine

class Patsient {
    constructor(nimi,vanus){
        this.nimi = nimi;
        this.vanus = vanus;
    }
}

class arst {
    constructor(nimi,vanus, eriala, aeg){
        this.nimi = nimi;
        this.vanus = vanus;
        this.eriala = eriala;
        this.aeg = aeg;
    }
}

class kohtumine{
    constructor(Arstinimi,Patsiendinimi, eriala, aeg){
        this.nimi = nimi;
        this.vanus = vanus;
        this.eriala = eriala;
        this.aeg = aeg;
    }
}

class haigla{
    constructor(){
        this.patsientideList = []
        this.arstideList = []
    }
    
    showAllPatsiendid(){
        for(let i = 0; i < this.patsientideList.length; i++){
            console.log(this.patsientideList[i])
        }
    }
    
    showAllPatsiendid(){
        for(let i = 0; i < this.arstideList.length; i++){
            console.log("Arsti Nimi: ",this.arstideList[i].nimi)
        }
    }
    
    showArstiAeg(){
        let arstiNimi:
        arstinimi = prompt("Milline arst teid huvitab?: "):
        for(let i = 0; i < this.arstideList.length; i++){
            if(this.arstideList[i].nimi = arstiNimi){
                for(let j = 0; j < this.arstideList[i].aeg.length; j++){
                    console.log(this.arstideList[i].aeg[j])
                }
            }
        }
    }
    
    showAllKohtumised(){
        console.log("Haiglas on järgmised kohtumised: ")
        for(let i = 0; i < this.kohtumine.length; i++){
            console.log("Haiglas on järgmised kohtumised: ")
        }
    }
}

patsient1 = new Patsient("Thomas",99);
patsient1 = new Patsient("Thomas",99);
haigla1 = new haigla();
haigla1.patsientideList.push(patsient1)
haigla1.patsientideList.push(patsient1)
haigla1.showAllPatsiendid()
arst1 = new arst("Ahmed",14,"Kiirurg")
haigla1.showAllPatsiendid()


#Iteratiivne/Inkrementaalne lähenemine

#mis see on
#paar pilte
#plussid ja miinused
#erinevused nende vahel
#kus seda kasutatakse

