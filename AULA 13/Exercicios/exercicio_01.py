celcsius = float(input("Digite uma temperatura em graus Celsius: "))

fahrenheit = (celcsius * 1.8) + 32

if celcsius < 15:
    print(f"{celcsius}°C equivalem a {fahrenheit}°F. O clima está Frio.")
elif celcsius == 15 or fahrenheit <= 25:
    print(f"{celcsius}°C equivalem a {fahrenheit}°F. O clima está Agradável.")
else:
    print(f"{celcsius}°C equivalem a {fahrenheit}°F. O clima está Quente.")