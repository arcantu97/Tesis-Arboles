import matplotlib.pyplot as plt 

labels = 'Pino', 'Abies', 'Encino'
sizes = [67.4, 14.4, 18.4]
explode = (0,0,0)
colors=['#004de5', '#26e600', '#fee600']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig('results.eps', dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format='eps',
        transparent=True, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)