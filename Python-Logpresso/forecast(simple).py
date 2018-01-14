table duration=2d sys_cpu_logs
| eval CPU=int(kernel+user)
| timechart span=1m avg(CPU) as CPU
| limit 180
| sort _time
| execpipe C:\Users\admin\PycharmProjects\Forecast\venv\Scripts\python C:\Users\admin\PycharmProjects\Forecast\Forecast.py  "forecast target=CPU count=30 change=0.05 logistic=f upper=100 lower=0"
|# eval _time=epoch(ds)
|# sort -time_forecast, -time_total

----------------------------------------------------------------------------------------------------------------------------------

import sys
import json
import pandas as pd
from fbprophet import Prophet

args = sys.argv[1].split()
stat_argv = args[1:]

data = []
result = []

for line in sys.stdin:
   row = json.loads(line, encoding='UTF-8')
   data.append(dict(row))

df = pd.DataFrame(data)

delim = '='
result = {}
for arg in stat_argv:
	temp = arg.split(delim)
	result[temp[0]] = temp[1]

time_col = '_time'

freq = str((pd.Timestamp(df[time_col].iloc[1]) - pd.Timestamp(df[time_col].iloc[0])).seconds) + 's'

df_to_prophet = pd.DataFrame()
df_to_prophet['ds'] = df[time_col]
df_to_prophet['y'] = df[result['target']]

m = Prophet(changepoint_prior_scale=float(result['change']))
m.fit(df_to_prophet)
future = m.make_future_dataframe(periods=int(result['count']), freq=freq)

forecast = m.predict(future)
forecast = pd.concat([df, forecast], axis=1)

for i in range(len(forecast)):
    print(forecast.iloc[i].to_json())
