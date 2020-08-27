kata1 = "PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika"
def rajut(kata1):
    #memecah kata1 kedalam list
    kata2 = list(kata1)
    #mengambil huruf awal dari kata 1 untuk memecahnya di split (kata3)
    find=kata1[0]
    #Memecah kata dari awalan huruf kalimat
    kata3 = kata1.split(find)
    # Mengambil element awal huruf dari list kata2 ("C")
    a= kata2[0]
    # Mengambil element akir dari hasil split pada kata 3
    b= kata3[-1]
    # Membuat list kosong untuk menggabungkan a (C) dan b(ode)
    fill=[]
    #Cara menggabungkannya
    fill.append(a)
    fill.append(b)
    #Join element (C dan ode) menjadi string pada variabel akhir
    akhir=''.join(fill)
    print(akhir)

rajut(kata1)