import hashlib
import sqlite3

# Veritabanı bağlama
conn = sqlite3.connect('veritabani.db')
cursor = conn.cursor()

# Veritabanına kaydolacak kullanıcı bilgileri
kullanici_adi1 = input("kullanıcı adı giriniz : ")
sifre1 = input("sifre giriniz : ")

# Kullanıcı adını sha256 ile hash yapma
hash_sifre = hashlib.sha256((sifre1).encode()).hexdigest()
print(hash_sifre)

# Veriyi tabloya ekleme
cursor.execute("INSERT INTO kullanicilar VALUES (?, ?)", (kullanici_adi1, hash_sifre))
conn.commit()

# Veritabanındaki kullanıcı bilgileri ile kıyaslanacak olan kullanıcı bilgileri
kullanici_adi2 = input("kullanıcı adı giriniz : ")
sifre2 = input("şifre giriniz : ")
hash_sifre2 = hashlib.sha256((sifre2).encode()).hexdigest()
print(hash_sifre2)

# Verileri sorgulama
cursor.execute("SELECT * FROM kullanicilar")
veriler = cursor.fetchall()


for veri in veriler:
   if veri[0]==kullanici_adi2:
        if veri[1]==hash_sifre2:
         print("KİMLİK DOĞRULAMANIZ BAŞARILI ŞEKİLDE GERÇEKLEŞTİRİLMİŞTİR")
        # print(veri[0],veri[1])
        else:
             print("GEÇERSİZ KULLANICI ADI VEYA ŞİFRE LÜTFEN TEKRAR DENEYİNİZ...")

conn.close()



