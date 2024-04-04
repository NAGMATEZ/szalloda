from abc import abstractmethod
class Szoba:

    foglalt=False
    def __init__(self, ar:int, szobaszam:int):
        self.ar=ar
        self.szobaszam=szobaszam

    
class EgyAgyasSzoba(Szoba):

    def __init__(self, ar: int, szobaszam: int):
        super().__init__(ar, szobaszam)

class KetAgyasSzoba(Szoba):

    def __init__(self, ar: int, szobaszam: int):
        super().__init__(ar, szobaszam)

class Szalloda:
    szobak=[]
    def __init__(self, nev):
        self.nev=nev

    def szobahozzaadas(self, szoba):
        self.szobak.append(szoba)


class Foglalas:
    def __init__(self, ev:int, honap:int, nap:int, agyszam:int, szobaszam:int, ugyfelnev:str):
        self.ev=ev
        self.honap=honap
        self.nap=nap
        self.agyszam=agyszam
        self.szobaszam=szobaszam
        self.ugyfelnev=ugyfelnev



def foglal():           
    agyszam=int(input("Hány ágyas szobát szeretne? (1 vagy 2): "))
    print("Kérem a dátumokat ne kezdje 0-val ; pl:01 -> 1")
    while True:
        ev=int(input("Kérem adja meg a foglalás évét: "))
        if ev<=2024:
            break
    while True:
        honap=int(input("Kérem adja meg a foglalás hónapját: "))
        if 1<=honap<=12:
            break
    while True:
        nap=int(input("Kérem adja meg a foglalás napját: "))
        if honap==1 or honap==3 or honap==5 or honap==7 or honap==8 or honap==10 or honap==12: 
            if 1<=nap<=31:
                break
        elif honap==4 or honap==6 or honap==9 or honap==11:
            if 1<=nap<=30:
                break
        else:
            if ev-2024%4==0:
                if 1<=nap<=29:
                    break
            else:
                if 1<=nap<=28:
                    break
    while True:
        ugyfelnev=input("Milyen névre lesz a foglalás?: ")
        if ugyfelnev!="":
            break

    if agyszam==1:
        for szoba in Szalloda.szobak:
            if isinstance(szoba, EgyAgyasSzoba) and szoba.foglalt==False:
                szobaszam=szoba.szobaszam
                szoba.foglalt=True
                foglalasok.append(Foglalas(ev, honap, nap, 1, szobaszam, ugyfelnev))
                return szoba.ar
    elif agyszam==2:
        for szoba in Szalloda.szobak:
            if isinstance(szoba, EgyAgyasSzoba) and szoba.foglalt==False:
                szobaszam=szoba.szobaszam
                szoba.foglalt=True
                foglalasok.append(Foglalas(ev, honap, nap, 2, szobaszam, ugyfelnev))
                return szoba.ar
    else:
        print("A szállodában nincs szabad szoba a kért feltételekkel")


def lemondas():
    ugyfelnev=input("Milyen névre volt a lemondani kívánt foglalás?: ")
    ev=int(input("Kérem adja meg a lemondani kívánt foglalás évét: "))
    honap=int(input("Kérem adja meg a lemondani kívánt foglalás hónapját: "))
    nap=int(input("Kérem adja meg a lemondani kívánt foglalás napját: "))
    szobaszam=int(input("Kérem adja meg a lemondani kívánt foglaláshoz kapcsolt szobaszámot: "))
    agyszam=int(input("Hány ágyas szobára foglalt?: "))

    for foglalas in foglalasok:
        if foglalas.ev==ev and foglalas.honap==honap and foglalas.nap==nap and foglalas.agyszam==agyszam and foglalas.szobaszam==szobaszam and foglalas.ugyfelnev==ugyfelnev:
             del(foglalas)
             print("A lemondás sikeres volt! Reméljük, legközelebb találkozunk")
             break
        else:
            print("A foglalás nem létezik a rendszerünkben, amennyiben mégis foglalt volna, kérem kérje le az összes foglalás menüpontban")

def foglalaslistazas(foglalasok):
    print("Az összes foglalás: \n")
    for foglalas in foglalasok:
        print("Dátum: " + str(foglalas.ev) + ". " + str(foglalas.honap) + ". " + str(foglalas.nap) +  "; Név: " + str(foglalas.ugyfelnev) + " ; Szobaszám: " + str(foglalas.szobaszam) +" ; Ágyak száma a szobában: " + str(foglalas.agyszam) + "\n")

class Menuinterfesz:
    @abstractmethod
    def opciok():
         #Megjeleníti a menü opcióit
         pass
    @abstractmethod
    def getAnswer():
        #Megszerzi a felhasználótól a választ, és aszerint megy tovább
        pass
class Menu:

    def opciok():
        print("Üdvözöljük a " + TestSzallo.nev + " szállodában! \n Készüléke nyomógombjai segítségével kérem válasszon az alábbi menüpontok közül: ")
        print("Foglalás kezdeményezése      - 1-es gomb")
        print("Meglévő foglalás lemondása   - 2-es gomb")
        print("Az összes foglalás listázása - 3-as gomb")

    def getAnswer():
        while True:
            try:
                valasz=int(input("\n Kérem írja be választását! (1,2,3): "))
                if 1<=valasz<=3:
                    return valasz
                else: print("Helytelen sorszám, kérem a fenti opciók megfelelő számát beütni")
            except ValueError:
                print("A bevitel formátuma nem megfelelő!! Kérem számmal válasszon a menüből")



foglalasok=[
Foglalas(2024,12,24,2,21,"Nagy Máté"),
Foglalas(2026,1,20,1,11,"Kelemen Ármin"),
Foglalas(2024,6,6,1,12,"Szilágyi Judit"),
Foglalas(2028,2,26,1,11,"Kocsis Szilárd"),
Foglalas(2030,7,15,2,21,"Nagy Johanna")
]


TestSzallo=Szalloda(nev="Tesztellek")

TestSzallo.szobahozzaadas(EgyAgyasSzoba(12000,11))

TestSzallo.szobahozzaadas(EgyAgyasSzoba(15000,12))

TestSzallo.szobahozzaadas(KetAgyasSzoba(20000,21))
while True:
    Menu.opciok()

    val=Menu.getAnswer()

    if val==1:
        foglal()
    elif val==2:
        lemondas()
    elif val==3:
        foglalaslistazas(foglalasok)
    else: 
        print("Ismeretlen hiba")

