kata = "Python"
def urai(kata):
    #Memisahkan setiap kata kedalam list ['P', 'y', 't', 'h', 'o', 'n'] 
    pisah=list(kata)
    #membuat list baru untuk mengurai kata Python
    new_urai=[]
    #looping untuk setiap index dan isi dari index di variabel pisah (eg : index 0 isi index= P)
    for index,isi_index in enumerate(pisah):
        #mengurai urai kata kedalam list baru (new_rajut)
        # Dengan harapan membuat kata dari slicing bertingkat
        #dari satu huruf(kata), ke dua huruf(kata)... menjadi kata utuh 
        new_urai.append(pisah[0:index+1])
        #looping untuk setiap item di new urai
        for item in new_urai:
            #untuk menggabungkan hasil urai [p py pyt... python]
            a= "".join(item)
        #cetak hasil gabungan (memakai end="" agar hasilnya horizontal (tidak dienter))
        print(a,end="")

urai(kata)