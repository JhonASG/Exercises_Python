year = int(input("Año: "))

if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print("Año bisiesto")
else:
    print("Año ordinario")