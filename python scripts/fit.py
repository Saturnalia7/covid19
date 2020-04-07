

import numpy as np
import pandas as pd
import connection as conn
import matplotlib.pyplot as plt

cnxn, crsr, engine = conn.connect()
df = conn.select(engine, 'vw_cases')
conn.disconnect(cnxn, crsr, engine)

df = df[df['name'] == 'Dallas']

delta = df['report_date'].max() - df['report_date'].min()
start = 1
x_data = np.array([i for i in range(start,delta.days+1)])
y_data = df['cases'].tail(delta.days-start+1).to_numpy()

log_x_data = np.log(x_data)
log_y_data = np.log(y_data)

curve_fit = np.polyfit(x_data, log_y_data, 1)
print(curve_fit)

y = np.exp(curve_fit[1]) * np.exp(curve_fit[0]*x_data)
plt.plot(x_data, y_data, 'o')
plt.plot(x_data, y)
plt.show()
