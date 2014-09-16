#Jamie Hilton
#12/09/14
#Temperature Converter V1.1
temperature_f = float(input("Please enter the temperature in Fahrenheit: "))

temperature_c = float((temperature_f-32)*(5/9))
print("The temperature is {0:.1f} degrees centigrade".format(temperature_c))
