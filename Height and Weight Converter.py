#Jamie Hilton
#16/09/14
#Height and Weight Converter V1.1
height_i = int(input("Please enter your height in Inches: "))

height_c = height_i*2.54

print("Your height is {0} Cm".format(height_c))

weight_s = int(input("Please enter your weight in Stone: "))

weight_k = weight_s*6.364

print("your weight is {0:.1f} Kg".format(weight_k))
