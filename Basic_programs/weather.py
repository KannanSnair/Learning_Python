temperature = int(input("what's the weather outside?"))
print("Temperate you entered is " + str(temperature) + " degree")

if temperature < 40 and temperature > 20:
    print("enjoy outdoor whether")
elif temperature > 40:
    print("hot day, be careful!!")
elif temperature < 20:
    print("cold day, take sweaters!!")
else:
    print("enjoy your day")

covid_patient = True
if covid_patient:
    print("You are a covid patient, Stay inside!!!!")