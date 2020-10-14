import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

X_AXIS = ('0.75', '0.80', '0.85')
index = pd.Index(X_AXIS, name='Porcentaje de píxeles permitidos')
data = {'Pino': (70.0, 63.0, 66.0),
'Encino': (20.0, 25.0, 22.0), 
'Abies': (10.0, 12.0, 12.0)}
df = pd.DataFrame(data, index=index)
ax = df.plot(kind='bar', stacked=True, figsize=(10, 6))
ax.set_ylabel('foo')
plt.legend(title='labels', bbox_to_anchor=(1.0, 1), loc='upper left')
plt.savefig('stacked.eps')  # if needed
#plt.show()