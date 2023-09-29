sb = float(input('informe o salario: '))
optante = input('optante pelo vt? s/n')

if sb <=1320:
    if optante.lower() == 's':
        inss= sb * 0.075
        vt= sb* 0.06
        sl= sb-inss-vt
        print ('INSS:', inss)
        print('VT:', vt)
        print('salario liquido:', sl)

    else:
        inss = sb * 0.075
        vt = 0
        sl = sb - inss
        print('INSS:', inss)
        print('VT:', vt)
        print('salario liquido:', sl)


elif sb >=1320.01 and sb<=2571.29:
      if optante.lower() == 's':
        inss = sb * 0.09
        vt = sb * 0.06
        sl= sb-inss-vt
        print ('INSS:', inss)
        print('VT:', vt)
        print('salario liquido:', sl)

      else:
        inss = sb * 0.09
        vt = 0
        sl = sb - inss
        print('INSS:', inss)
        print('VT:', vt)
        print('salario liquido:', sl)


elif sb >=2571.30 and sb<=3856.94:
      if optante.lower() == 's':
        inss = sb * 0.12
        vt = sb * 0.06
        sl= sb-inss-vt
        print ('INSS:', inss)
        print('VT:', vt)
        print('salario liquido:', sl)


      else:
        inss = sb * 0.12
        vt = 0
        sl = sb - inss
        print('INSS:', inss)
        print('VT:', vt)
        print('salario liquido:', sl)


elif sb >= 3856.95 and sb <= 7507.49:
      if optante.lower() == 's':
        inss = sb * 0.14
        vt = sb * 0.06
        sl = sb - inss-vt
        print('INSS:', inss)
        print('VT:', vt)
        print('salario liquido:', sl)

      else:
        inss = 7507.49 * 0.14
        vt = 0
        sl = sb - inss-vt
        print('INSS:', inss)
        print('VT:', vt)
        print('salario liquido:', sl)