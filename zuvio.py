import matplotlib.pyplot as plt
coord = [[1,1], [2,1], [2,2], [1,2], [0.5,1.5]]
coord.append(coord[0]) #repeat the first point
# to create a 'closed loop'
print(coord)
xs, ys = zip(*coord) #create lists of x and y values
print(xs)
print(ys)
plt.figure()
plt.plot(xs,ys)
plt.show() # if you need..