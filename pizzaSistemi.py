import csv #Burada csv kitaplığını import ediyoruz
import datetime #Burada date time kitaplığını import ediyoruz

class Pizza: #Buraya Pizza class tanımlıyoruz
    def __init__(self, description='Pizza', cost=0):# init methodu ile alt sınıfların description ve cost olmak üzere 2 parametre alacağını belirtiyoruz.
        self.description = description #Alt sınıflarda eğer bir description girilirse bu değeri alır girilmezse varsayılan olarak pizza değerini alır.
        self.cost = cost #Alt sınıflarda eğer bir cost girilirse bu değeri alır girilmezse varsayılan olarak 0 değerini alır.

    def get_description(self): #Bir pizza alt sınıfı oluşturulduğunda get description fonksiyonunu bu alt sınıfta kullanarak alt sınıfın descriptionunu elde edebiliriz.
        return self.description 

    def get_cost(self): #Bir pizza alt sınıfı oluşturulduğunda get cost fonksiyonunu bu alt sınıfta kullanarak alt sınıfın costunu elde edebiliriz.
        return self.cost
    

class KlasikPizza(Pizza): #Pizzanın alt sınıflarını oluşturduk Super fonksiyonu ile üst pizza sınıfının init fonksiyonuna erişip
    def __init__(self):
        super().__init__('Klasik Pizza', 30) # description kısmına klasik pizza cost kısmına 30 değerini atadık, böylece alt sınıflar oluşturulurken değerleri otomatik olarak atamış olduk.


class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__('Margarita Pizza', 40)


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__('Turk Pizza', 45)


class SadePizza(Pizza):
    def __init__(self):
        super().__init__('Sade Pizza', 50)


class Decorator(Pizza): # Bir decorator üst sınıfı oluşturduk.
    def __init__(self, component, description, cost): # Alt sınıfların alacağı parametreler olarak component, description ve cost'u belirledik
        self.component = component # Component burada Pizza alt sınıflarını temsil ediyor
        self.description = description # Description Decorator alt sınıflarının açıklamasını temsil ediyor
        self.cost = cost # Cost Decorator alt sınıflarının fiyatını temsil ediyor
    
    def get_cost(self): # Bu kısımda Component olarak verilen Pizzanın fiyatıyla Sosun fiyatını topluyoruz
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self): # Bu kısımda Component olarak verilen Pizzanın açıklamasıyla Sosun açıklamasını birleştiriyoruz
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class Zeytin(Decorator): # Tüm Decorator alt sınıflarının açıklamaları ve fiyatlarının tanımlanması
    def __init__(self, component):
        super().__init__(component, ' ile birlikte Zeytinli Sos', 2)


class Mantar(Decorator):
    def __init__(self, component):
        super().__init__(component, 'ile birlikte Mantarli Sos', 2)


class KeciPeyniri(Decorator):
    def __init__(self, component):
        super().__init__(component, 'ile birlikte Keci Peynirli Sos', 3)


class Et(Decorator):
    def __init__(self, component):
        super().__init__(component, 'ile birlikte Etli Sos', 4)


class Sogan(Decorator):
    def __init__(self, component):
        super().__init__(component, 'ile birlikte Soganli Sos', 2)


class Misir(Decorator):
    def __init__(self, component):
        super().__init__(component, 'ile birlikte Misirli Sos', 1)

def csv_yaz(name, id_number, cc_number, pizza, sauce, price, cc_password): # Csv dosyasına alınan verileri yazacak olan fonksiyon
    date_time = datetime.datetime.now() # Datetime gömülü fonksiyonuyla güncel tarihi ve zamanı date_time değişkenine atıyoruz.
    with open('Orders_Database.csv', mode='a', newline='') as file: # Orders_Database.csv dosyasını append modunda açıyoruz, append modu var olan verinin üzerine yazmayı sağlar
        writer = csv.writer(file) # writer değişkenine csv kütüphanesindeki writer fonksiyonunu atadık.
        writer.writerow([f"ADI= {name}, KULLANICI ADI= {id_number}, KART NUMARASI= {cc_number}, PIZZASI= {pizza}, SOSU= {sauce}, UCRETI= {price}, TARIHI= {date_time.strftime('%Y-%m-%d %H:%M:%S')}, KART SIFRESI= {cc_password}"])
        # writer değişkeninin içerisindeki writerow fonksiyonuna ulaşarak her seferinde bir satır yazdırmasını sağlıyoruz. fstring kullanarak stringin içerisinde değişken kullanıyoruz böylece değişkenin değerlerini dosyaya yazabiliyoruz.

def main():
      
    isOrderFinished=False
    summarizeOrder=[]
    print('Pizza Sistemine Hosgeldiniz!\n\nMenumuz:\n') #Hoşgeldin mesajı
    print(open('Menu.txt', 'r').read()) #Menu.txt dosyasının okuma modunda açılması
    while(not isOrderFinished): # Musteri birden fazla siparis verebilir olmasi icin döngü
        pizza_choice = int(input('\nLutfen pizzanizi seciniz: ')) #Kullanıcıdan alınan input'u pizza_choice değerine atıyoruz
        while pizza_choice not in range(1, 5): # Kullanıcının yanlış değer girip girmemesini kontrol ediyoruz
            pizza_choice = int(input('Gecersiz secim. Lutfen 1-5 arasinda bir sayi girin: '))

        pizza = None # Pizza değişkeni oluşturuyoruz

        
        if pizza_choice == 1: # Kullanıcının girdiği değere göre alt sınıfları çalıştırıyoruz.
            pizza = KlasikPizza()
        elif pizza_choice == 2:
            pizza = MargaritaPizza()
        elif pizza_choice == 3:
            pizza = TurkPizza()
        elif pizza_choice == 4:
            pizza = SadePizza()
    
        sauce_choice = int(input('\nLutfen sosunuzu seciniz: ')) # Kullanıcının sos seçmesini istiyoruz.
        while sauce_choice not in range(11, 17): # Kullanıcının yanlış değer girip girmediğinin kontrolü
            sauce_choice = int(input('Gecersiz secim. Lutfen 11-16 arasinda bir sayi girin: '))
        if sauce_choice == 11:
            pizza = Zeytin(pizza)
        elif sauce_choice == 12:
            pizza = Mantar(pizza)
        elif sauce_choice == 13:
            pizza = KeciPeyniri(pizza)
        elif sauce_choice == 14:
            pizza = Et(pizza)
        elif sauce_choice == 15:
            pizza = Sogan(pizza)
        elif sauce_choice == 16:
            pizza = Misir(pizza)
    
    
        summarizeOrder.append(pizza)#Siparişlerin bir array'e siparis özeti olarak atanması
        while(True):#Kullanıcının baska siparis verip vermemek istemesi durumunu kontrol etme
            orderDone=input('\nBaska bir siparis daha vermek istiyorsaniz Y istemiyorsaniz N yazin.')
            if(orderDone.capitalize()=="N"):
                isOrderFinished=True #N ise siparis sonlandırmak için True yapılır
                break
            elif(orderDone.capitalize()=="Y"):
                isOrderFinished=False#Y ise siparis devam ettirmek için False yazılır baştaki while döngüsü devam eder
                break
            else:
                print('\nGecersiz cevap. Lutfen Y ya da N yazin.')

        
    print('\nSiparis Ozetiniz: ')
    toplamTutar=0
    siparisOzeti=""
    for i in range(len(summarizeOrder)): #array e eklenen değerleri for döngüsüyle dönüp özet ve toplam tutar bulma
        siparisOzeti=siparisOzeti+summarizeOrder[i].get_description()+" + "
        toplamTutar+=summarizeOrder[i].get_cost()
    siparisOzeti=siparisOzeti[:-2]
    print('\n\nPizza seciminiz: {}\nTutar: {} TL '.format(siparisOzeti, toplamTutar)) # Sipariş özeti
        
    # Kullancı Bilgilerinin Csv Dosyasına yazacağı yer 
    
    name =(input('\nLutfen isminizi girin: ')) # Kullanıcıdan isim istenmesi
    while not name.isalpha(): # Kullanıcın alfabetik harf kullanmaması durumunda hata vermesi
        print('Gecersiz giris yaptiniz Lutfen sadece harfler kullanin.')  
        name = (input('\nLutfen isminizi girin: '))    
    while True: # Kullanıcın id'si, cc numarası ve cc şifresinin istenmesi, hata olması durumunda kullanıcı tekrardan en baştan bilgilerini girmek zorunda
        try: # try except bloğu öncelikle try kod bloğunu dener başarısız olması durumunda except kısmındaki hata mesajını yazdırır, sonsuz döngü olduğu için kullanıcı doğru şekilde bilgi girene kadar program kapanmaz
            id_number = int(input(('Lutfen kullanici numaranızi girin: ')))
            cc_number = int(input('Lutfen kart numaranizi girin: '))
            cc_password = int(input('Lutfen kredi karti sifrenizi girin: '))
            break
        
        except ValueError:
            print("Geçersiz sadece sayi giriniz")

    now = datetime.datetime.now() # Zamanın bir değişkene atanması
    formatted_time = now.strftime('%Y-%m-%d %H:%M') # Zamanın strftime fonksiyonuyla formatlanması, %Y yıl %m ay %d gün %H saat %M dakikayı temsil eder
    
    csv_yaz(name, id_number, cc_number, siparisOzeti, toplamTutar, formatted_time, cc_password) # Yazdığımız csv_yaz fonksiyonunun çağrılarak verilen bilgilerin database'e işlenmesi
    
    print("Tebrikler siparisiniz basari ile olusturuldu.", formatted_time) # Sipariş mesajı ve tarihin yazdırılması.

main() # Programın çalışması