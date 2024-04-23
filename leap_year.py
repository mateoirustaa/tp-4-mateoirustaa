def leap_year():
    año=int(input("Ingrese un año:  "))
if (año%100)==0 and(año%400)==0:
        print("el año es biciesto")
elif (año%4)==0 and (año%100!=0):
    print("el año es biciesto2")
else :
    print("el año no es biciesto")
