import matplotlib.pyplot as plt 

labels = 'Pino', 'Abies', 'Encino'
sizes = [34439, 7497, 10414]
explode = (0,0,0)
colors=['#004de5', '#26e600', '#fee600']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig('results_2.png', dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=True, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)