import matplotlib
import matplotlib.pyplot as pt
matplotlib.matplotlib_fname()  # needed for showing the graph

fig = pt.figure()

rect = fig.patch

rect.set_facecolor('green')  # set bg color

subplot = fig.add_subplot(2, 1, 1, facecolor='grey')
subplot.plot([1, 3, 5, 7], [2, 3, 4, 23], 'white', linewidth=8.0)
subplot.plot([1, 5, 7, 9], [2, 3, 4, 23], 'blue', linewidth=4.0)
subplot.plot([1, 11, 14, 23], [2, 3, 4, 23], 'orange', linewidth=2.0)

# defines x,y axis color
subplot.tick_params(axis='x', color='white')
subplot.tick_params(axis='y', color='white')

# sets the color to border of subplot
subplot.spines['top'].set_color('w')
subplot.spines['left'].set_color('w')
subplot.spines['right'].set_color('w')
subplot.spines['bottom'].set_color('w')

subplot.set_title('Graph', color='white')
subplot.set_xlabel("x-axis", color='white')
subplot.set_ylabel("y-axis", color='white')


subplot1 = fig.add_subplot(2, 1, 2, facecolor='grey')
subplot1.plot([1, 3, 5, 7], [2, 3, 4, 23], 'white', linewidth=8.0)
subplot1.plot([1, 5, 7, 9], [2, 3, 4, 23], 'blue', linewidth=4.0)
subplot1.plot([1, 11, 14, 23], [2, 3, 4, 23], 'orange', linewidth=2.0)

# defines x,y axis color
subplot1.tick_params(axis='x', color='white')
subplot1.tick_params(axis='y', color='white')

# sets the color to border of subplot1
subplot1.spines['top'].set_color('w')
subplot1.spines['left'].set_color('w')
subplot1.spines['right'].set_color('w')
subplot1.spines['bottom'].set_color('w')

subplot1.set_title('Graph', color='white')
subplot1.set_xlabel("x-axis", color='white')
subplot1.set_ylabel("y-axis", color='white')

pt.show()
