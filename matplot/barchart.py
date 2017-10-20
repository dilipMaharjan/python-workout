import matplotlib.pyplot as pt
import numpy as np

pos = np.arange(6) + 0.5

pt.barh(pos, (4, 8, 12, 3, 17, 6), align='center', color='red')
pt.xlabel('Height in Inches', color='Red')
pt.ylabel('Students', color='Red')
pt.title('Heights')

pt.tick_params(axis='x', colors='orange')
pt.tick_params(axis='y', colors='orange')

pt.subplots_adjust(left=.11, bottom=.12, right=.94)
pt.yticks(pos, ['Avi', 'Joe', 'John', 'Mathew', 'Moses', 'Aron'])

 pt.show()

