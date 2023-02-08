print('Masukkan angka :')
  
jumlah = int(input('Masukkan angka : '))
print()
  
for i in range(jumlah):
  for j in range(jumlah-i):
    print(' ',end='')
      
  for k in range(i+1):
    print('* ',end='')
  print()
 
for i in range(1,jumlah):
  for j in range(i+1):
    print(' ',end='')
      
  for k in range(jumlah-i):
    print('* ',end='')
  print()