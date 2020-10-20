import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

X_AXIS = ('0.75', '0.80', '0.85')
index = pd.Index(X_AXIS, name='Porcentaje de píxeles permitidos')
colors=['#004de5',  '#fee600', '#26e600']
data = {'Pino': (70.0, 63.0, 66.0),
'Encino': (20.0, 25.0, 22.0), 
'Abies': (10.0, 12.0, 12.0)}
df = pd.DataFrame(data, index=index)

ax = df.plot(kind='bar', stacked=True, color=colors, figsize=(11, 7))
ax.xaxis.label.set_size(12)
for rect in ax.patches:
    # Find where everything is located
    height = rect.get_height()
    width = rect.get_width()
    x = rect.get_x()
    y = rect.get_y()
    
    # The height of the bar is the data value and can be used as the label
    label_text = f'{height:.0f}'  # f'{height:.2f}' to format decimal values
    
    # ax.text(x, y, text)
    label_x = x + width / 2
    label_y = y + height / 2

    # plot only when height is greater than specified value
    if height > 0:
        ax.text(label_x, label_y, label_text, ha='center', va='center', fontsize=10, fontweight='bold')
ax.set_ylabel('Cantidad de especies detectadas', fontsize=12)
plt.xticks(rotation=0)
plt.legend(title='Especie', bbox_to_anchor=(1.0, 1), loc='upper left')
plt.savefig('resultado_pixelesausentes.eps')  # if needed
#plt.show()