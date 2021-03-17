jumlah_mhs = int(input('Masukkan jumlah mahasiswa: '))
data_total = list()
for i in range(jumlah_mhs):
    data_mhs = input('Silahkan masukkan (Nama/NIM/Alamat/Asal Sekolah/Kode Prodi/Nilai IPK Awal/Nilai UTS/UAS/TM) :').split('/')
    data_total.append(data_mhs)

'''ips = (0.3*data[6]) + (0.3*data[8]) + (0.4*data[7])
ipk = ips + data[5]'''

print('+------------------+-----------+------------------+-----------------+--------------------+-----------+------+------+------+----------+----------+----------+')
print('| Nama             | NIM       | Alamat           | Asal Sekolah    | Kode Prodi         | IPK Awal  | UTS  | UAS  | TM   | IPS      | IPK      | Beasiswa |')
print('+------------------+-----------+------------------+-----------------+--------------------+-----------+------+------+------+----------+----------+----------+')
    
for i in range(len(data_total)):
    ips = round((0.3*int(data_total[i][6])) + (0.3*int(data_total[i][8])) + (0.4*int(data_total[i][7])),2)
    ipk = round((ips + int(data_total[i][5]))/2,2)
    if data_total[i][4] == 'TI' or data_total[i][4] == 'SI':
        if 75 < ipk < 85:
            beasiswa = '20%'
        elif 85 < ipk < 100:
            beasiswa = '30%'

    elif data_total[i][4] == 'DKV' or data_total[i][4] == 'Teknik Industri':
        if 75 < ipk < 85:
            beasiswa = '25%'
        elif 85 < ipk < 100:
            beasiswa = '35%'
    else:
        beasiswa = 'TIDAK'
    
    print('|',data_total[i][0],' '*(15-len(data_total[i][0])), #Nama
          '|',data_total[i][1],' '*(8-len(data_total[i][1])),  #NIM
          '|',data_total[i][2],' '*(15-len(data_total[i][2])), #Alamat
          '|',data_total[i][3],' '*(14-len(data_total[i][3])), #Asal Sekolah
          '|',data_total[i][4],' '*(17-len(data_total[i][4])), #Kode Prodi
          '|',data_total[i][5],' '*(8-len(data_total[i][5])),  #IPK Awal
          '|',data_total[i][6],' '*(3-len(data_total[i][6])),  #UTS
          '|',data_total[i][7],' '*(3-len(data_total[i][7])),  #UAS
          '|',data_total[i][8],' '*(3-len(data_total[i][8])),  #TM
          '|',ips,' '*(7-len(str(ips))),                       #IPS
          '|',ipk,' '*(7-len(str(ipk))),                       #IPK
          '|',beasiswa,' '*(7-len(str(beasiswa))),'|')         #Beasiswa   
    
print('+----------------------------------------------------------------------------------------------------------------------------------------------------------+')

'''
input data mahasiswa: 
Daniel Bernard/1230001/Kota A1/SMAN 123/TI/87/85/79/90
Bernard Budiman/1230004/Kabupaten ABC/SMA XYZ/SI/100/99/75/80
Farhan Arduino/1230025/Kota Lambda/Tidak SMA/DKV/88/99/10/100
Navier Stokes/1230009/Desa Indah/SMA Besar/Teknik Industri/85/95/60/15
Alan Turing/1230099/Kecamatan ABC/SMA 999/TI/100/15/25/35
Tony Stark/1230005/Kelurahan Stark/SMA Permata/EL/65/20/100/100
Rudolf Diesel/1230010/Kota Bekasi/SMA Otto/DKV/100/100/100/100
Stephen Hawking/1230008/Dewa Big Bang/SMA Radiation/Astrofisika/90/100/50/70
'''

