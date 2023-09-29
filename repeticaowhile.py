 #enquanto i<10 faca
i = 1
resp ='s'
while resp=='s':
   m = int(input('Digite o valor: '))
   while i <=10:
       print(i,' x ', m, '=',i*m)
       i=i+1
   resp = input('Quer continunar? s/n')
   i=1