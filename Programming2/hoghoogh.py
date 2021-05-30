
saat = float(input("chand saat dar hafte ? "))

dastmozd_saati = int (input("har saat chand tooman ? "))

kol_daryafti = saat *  4 * dastmozd_saati 

vat = 0.1 * kol_daryafti

khales_daryafti = kol_daryafti -  vat

print ("kol_daryafti = ", kol_daryafti)

print ("maliat = ", vat)

print ("khales_daryafti = ", khales_daryafti)
