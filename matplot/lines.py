import matplotlib
import matplotlib.pyplot as pt
matplotlib.matplotlib_fname()  # needed for showing the graph
# first array is x-axis's and second array is for y-axis's
pt.plot([1, 2, 3, 4], [20, 30, 4, 15])
pt.title("Line Graph")
pt.xlabel("x-axis")
pt.ylabel('y-axis')
pt.show()


# reading coordinates from file
# don't know why it requires absolute path
fileRef = open(
    "/mnt/6CEA162B5D79288A/Back-End/python/udemy/matplot/coordinates.txt", "r")
file = fileRef.read()
xy = file.split('\n')
x = []
y = []
for i in xy:
    val = i.split(',')
    x.append(int(val[0]))
    y.append(int(val[1]))

pt.plot(x, y)
pt.show()
