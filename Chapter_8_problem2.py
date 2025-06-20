def celsius_to_farehanite(celsius):
    return (((celsius*9)/5)+32)
celsius = float (input("Enter a temprature in Celsius scale: "))
farehanite = celsius_to_farehanite(celsius)
print(round(farehanite,2))