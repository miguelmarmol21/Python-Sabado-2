#Represa hidrohituango

#Entrada

nivelAgual=float(input('Digite el nivel del agua: '))

#Proceso

if(nivelAgual>=0 and nivelAgual<=250):
    print(f'Nivel del agua {nivelAgual}, muy bajo...')

elif(nivelAgual>250 and nivelAgual<=400):
    print(f'Nivel del agua {nivelAgual}, estable...')

else:
    print(f'Nivel del agua {nivelAgual}, muy alto PELIGRO')