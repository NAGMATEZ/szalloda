from abc import ABC,abstractmethod


class Szoba(ABC):

    foglalt = False

    def __init__(self, ar: int, szobaszam: int):
        self.ar = ar
        self.szobaszam = szobaszam

    
class EgyAgyasSzoba(Szoba):

    def __init__(self, ar: int, szobaszam: int):
        super().__init__(ar, szobaszam)


class KetAgyasSzoba(Szoba):

    def __init__(self, ar: int, szobaszam: int):
        super().__init__(ar, szobaszam)


class Szalloda:


    def __init__(self, nev):
        self.nev = nev
        self.szobak=[]

    def szobahozzaadas(self, szoba):
        self.szobak.append(szoba)


class Foglalas:
    def __init__(self,szalloda:Szalloda, ev: int, honap: int, nap: int, agyszam: int, szobaszam: int, ugyfelnev: str):
        self.szalloda=szalloda
        self.ev = ev
        self.honap = honap
        self.nap = nap
        self.agyszam = agyszam
        self.szobaszam = szobaszam
        self.ugyfelnev = ugyfelnev


def foglal(szalloda):
    agyszam = int(input("Hány ágyas szobát szeretne? (1 vagy 2): "))
    print("Kérem a dátumokat ne kezdje 0-val ; pl:01 -> 1")
    while True:
        ev = int(input("Kérem adja meg a foglalás évét: "))
        if ev <= 2024:
            break
    while True:
        honap = int(input("Kérem adja meg a foglalás hónapját: "))
        if 1 <= honap <= 12:
            break
    while True:
        nap = int(input("Kérem adja meg a foglalás napját: "))
        if honap == 1 or honap == 3 or honap == 5 or honap == 7 or honap == 8 or honap == 10 or honap == 12:
            if 1 <= nap <= 31:
                break
        elif honap == 4 or honap == 6 or honap == 9 or honap == 11:
            if 1 <= nap <= 30:
                break
        else:
            if ev-2024 % 4 == 0:
                if 1 <= nap <= 29:
                    break
            else:
                if 1 <= nap <= 28:
                    break
    while True:
        ugyfelnev = input("Milyen névre lesz a foglalás?: ")
        if ugyfelnev != "":
            break

    if agyszam == 1:
        for szoba in szalloda.szobak:
            if isinstance(szoba, EgyAgyasSzoba) and not szoba.foglalt:
                szobaszam = szoba.szobaszam
                szoba.foglalt = True
                foglalasok.append(Foglalas(szalloda, ev, honap, nap, 1, szobaszam, ugyfelnev))
                print("Köszönjük foglalását!\n")
                return szoba.ar
    elif agyszam == 2:
        for szoba in szalloda.szobak:
            if isinstance(szoba, KetAgyasSzoba) and not szoba.foglalt:
                szobaszam = szoba.szobaszam
                szoba.foglalt = True
                foglalasok.append(Foglalas(szalloda,ev, honap, nap, 2, szobaszam, ugyfelnev))
                print("Köszönjük foglalását!\n")
                return szoba.ar
    else:
        print("A szállodában nincs szabad szoba a kért feltételekkel")



def lemondas():
    sikeres=False
    ugyfelnev = input("Milyen névre volt a lemondani kívánt foglalás?: ")
    ev = int(input("Kérem adja meg a lemondani kívánt foglalás évét: "))
    honap = int(input("Kérem adja meg a lemondani kívánt foglalás hónapját: "))
    nap = int(input("Kérem adja meg a lemondani kívánt foglalás napját: "))
    szobaszam = int(input("Kérem adja meg a lemondani kívánt foglaláshoz kapcsolt szobaszámot: "))
    agyszam = int(input("Hány ágyas szobára foglalt?: "))

    for foglalas in foglalasok:
        if (foglalas.ev == ev and foglalas.honap == honap and foglalas.nap == nap and foglalas.agyszam == agyszam and
                foglalas.szobaszam == szobaszam and foglalas.ugyfelnev == ugyfelnev):
             del(foglalas)
             print("A lemondás sikeres volt! Reméljük, legközelebb találkozunk")
             sikeres=True
             break
    if not sikeres:
            print("A foglalás nem létezik a rendszerünkben, amennyiben mégis foglalt volna, kérem kérje le az összes foglalás menüpontban")

def foglalaslistazas(foglalasok):
    print("Az összes foglalás: \n")
    for foglalas in foglalasok:
        print("Dátum: " + str(foglalas.ev) + ". " + str(foglalas.honap) + ". " + str(foglalas.nap) + "; Név: " + str(foglalas.ugyfelnev) + " ; Szobaszám: " + str(foglalas.szobaszam) + " ; Ágyak száma a szobában: " + str(foglalas.agyszam) + "\n")


class Menuinterfesz:

    @abstractmethod
    def szallodavalasztas(self):
        #választunk a rendelkezésre álló szállodákból egyet a program fennmaradó részére
        pass
    @abstractmethod
    def opciok(self):
         #Megjeleníti a menü opcióit
         pass
    @abstractmethod
    def getAnswer(self):
        #Megszerzi a felhasználótól a választ, és aszerint megy tovább
        pass
class Menu:

    def szallodavalasztas(self, szallodalista):
        print("Válassz szállodát az alábbiak közül: ")
        index=0
        for szallo in szallodak:
            print(str(index) + ". szálloda " + szallo.nev)
        return int(input("A választásod: "))

    def opciok(self):
        print("\nÜdvözöljük a " + TesztSzallo.nev + " szállodában!\nKészüléke nyomógombjai segítségével kérem válasszon az alábbi menüpontok közül: ")
        print("Foglalás kezdeményezése      - 1-es gomb")
        print("Meglévő foglalás lemondása   - 2-es gomb")
        print("Meglévő foglalás lemondása   - 2-es gomb")
        print("Az összes foglalás listázása - 3-as gomb")
        print("Kilépés a programból         - 0-ás gomb")

    def getAnswer(self):
        while True:
            try:
                valasz=int(input("\n Kérem írja be választását! (1,2,3): "))
                if 0<=valasz<=3:
                    return valasz
                else: print("Helytelen sorszám, kérem a fenti opciók megfelelő számát beütni")
            except ValueError:
                print("A bevitel formátuma nem megfelelő!! Kérem számmal válasszon a menüből")

M = Menu()
szallodak=[]
TesztSzallo = Szalloda(nev="TesztSzallo")
szallodak.append(TesztSzallo)

TesztSzallo.szobahozzaadas(EgyAgyasSzoba(12000, 11))

TesztSzallo.szobahozzaadas(EgyAgyasSzoba(15000, 12))

TesztSzallo.szobahozzaadas(KetAgyasSzoba(20000, 21))
hanyadik = M.szallodavalasztas(szallodak)
foglalasok = [
Foglalas(TesztSzallo,2024, 12, 24, 2, 21, "Nagy Máté"),
Foglalas(TesztSzallo,2026, 1, 20, 1, 11, "Kelemen Ármin"),
Foglalas(TesztSzallo,2024, 6, 6, 1, 12, "Szilágyi Judit"),
Foglalas(TesztSzallo,2028, 2, 26, 1, 11, "Kocsis Szilárd"),
Foglalas(TesztSzallo,2030, 7, 15, 2, 21, "Nagy Johanna")
]


while True:
    Menu.opciok(M)
    val = Menu.getAnswer(M)

    if val == 1:
        foglal(TesztSzallo)
    elif val == 2:
        lemondas()
    elif val == 3:
        foglalaslistazas(foglalasok)
    elif val == 0:
        break
    else: 
        print("Ismeretlen hiba")
