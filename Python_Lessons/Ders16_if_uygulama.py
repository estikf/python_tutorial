sinav_sonuclari = { 'ahmet' : 58, 
                    'mehmet' : 43, 
                    'süleyman' : 98, 
                    'mehmet' : 23, 
                    'ayşe' : 34, 
                    'furkan' : 87,
                    'rıza'  : 50,
                    'Mahmut': 100,
                
                    }

for key, value in sinav_sonuclari.items():
    if value >= 50:
        print(f'{key}, aldığı not {value} : GEÇTİ' )
    else:
        print(f'{key}, aldığı not {value} : KALDI' )