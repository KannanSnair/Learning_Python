def ageplan(age):
    if(age < 40):
        print('Spend time for fun after your good savings')
    elif age > 40 and age < 50:
        print('save money for your children education and for your health insurance and for your retirement time')
    elif age < 50 and age > 55:
        print('Save the maximum for the retiral. Detailed plan can be shared')
    else :
        print('Save maximum. Details can be shared')
    return "testing function"


def main():
    yourage = int(input("input your age"))

    if yourage < 35:
        print('you are young')
    else :
        print('You are getting to next phase.. plan accordingly as below!!')
        print(ageplan(int(yourage)))


main()
