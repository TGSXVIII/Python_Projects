#This converts fahrenhit to celsius
faren = int(input("Enter temperature in Fahrenheit: "))

celsius = int((faren - 32) / 1.8)

print(f"{faren} Fahrenheit is equal to {celsius} degrees Celsius")


#This converts celsius to fahrenhit
celsius = int(input("Enter temperature in Celsius: "))

faren2 = int((celsius * 1.8) + 32)

print(f" {celsius} degrees Celsius is equal to {faren2} Fahrenheit")