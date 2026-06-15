import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x,y)
plt.axis([0,10,1,15])
plt.title("Title data ")
plt.show()

plt.savefig("pic.jpg")
