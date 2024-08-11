def convertTemp(c):  
   k = c + 273.15
   return k

cel = float(input('Enter temperature in Celsius: '))

kelvin = convertTemp(cel)
print('%0.1f degrees Celsius is equivalent to %0.1f Kelvin' %(cel, kelvin))