def testBMI():
    Name,height,weight = input(),int(input()),int(input())
    height /= 100
    BMI = weight/(height**2)
    if(BMI<18.5):
        print("Hi {0}, Your BMI: %.6f too LOW.".format(Name) %BMI)
    elif(BMI>24):
        print("Hi {0}, Your BMI: %.6f too HIGH.".format(Name) %BMI)
    else:
        print("Hi {0}, Your BMI: %.6f.".format(Name) %BMI)
testBMI()