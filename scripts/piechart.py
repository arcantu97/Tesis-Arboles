import matplotlib.pyplot as plt 
import matplotlib as mpl

mpl.rcParams['font.size'] = 15.0
labels = 'Pino', 'Abies', 'Encino'
sizes = [58.1, 7.7, 34.3]
explode = (0,0,0)
colors=['#004de5', '#26e600', '#fee600']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.xaxis.label.set_size(40)
plt.savefig('exp3.pdf', dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format='pdf',
        transparent=True, bbox_inches=None, pad_inches=0.1, metadata=None)