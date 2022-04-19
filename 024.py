def testBMI():
    height = []
    weight = []
    while(1):
        w = input()
        if(w=="-1"):
            break
        sp = w.split(" ")
        height.append(float(sp[0]))
        weight.append(float(sp[1]))
    for i in range(len(height)):
        BMI = weight[i]/(height[i]**2)
        if(height[i] < 0.5 or height[i]> 2.5):
            print("Input Error 0.5~2.50")
        elif(weight[i] < 20 or weight[i]> 300):
            print("Input Error 20~300")
        elif(BMI<18.5):
            print("BMI too low")
        elif(BMI>24):
            print("BMI too hight")
        else:
            print("%.2f" %BMI)
testBMI()