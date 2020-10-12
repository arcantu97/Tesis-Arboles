import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

X_AXIS = ('0.15', '0.25', '0.50')
index = pd.Index(X_AXIS, name='Porcentaje de píxeles permitidos')
data = {'Pino': (66.0, 62.0, 67.0),
'Encino': (17.0, 24.0, 15.0), 
'Abies': (17.0, 14.0, 18.0)}
df = pd.DataFrame(data, index=index)
ax = df.plot(kind='bar', stacked=True, figsize=(10, 6))
ax.set_ylabel('Cantidad de especies detectadas')
plt.legend(title='labels', bbox_to_anchor=(1.0, 1), loc='upper left')
plt.savefig('stacked.png')  # if needed
#plt.show()