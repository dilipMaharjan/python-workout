import matplotlib.pyplot as pt

sizes = [40, 23, 7, 15, 5]
labels = ['Android', 'Apple', "Windows", 'Blackberry', 'Xiamoi']
colors = ['yellow', 'orange', 'Cyan', 'Magenta', 'Red']

pt.pie(sizes, colors=colors, startangle=90, labels=labels)
pt.title('Pie Chart')
pt.legend(title='Legend', loc='lower left')
pt.axis('equal')

pt.show()
