table duration=2d sys_cpu_logs
| eval CPU=int(kernel+user)
| timechart span=1m avg(CPU) as CPU
| limit 180
| sort _time
| execpipe C:\Users\admin\PycharmProjects\Forecast\venv\Scripts\python C:\Users\admin\PycharmProjects\Forecast\Forecast.py  "forecast target=CPU count=30 change=0.05 logistic=f upper=100 lower=0"
|# eval _time=epoch(ds)
|# sort -time_forecast, -time_total

-------------------------------------------------------------------------------------------------------------------------------------

import sys
import json
import time
import pandas as pd
# import re
from fbprophet import Prophet

start_time_total = time.time()

args = sys.argv[1].split()
stat_argv = args[1:]

data = []
result = []

for line in sys.stdin:
   row = json.loads(line, encoding='UTF-8')
   data.append(dict(row))

df = pd.DataFrame(data)

# default_param = {
#     'count': 10,
#     'target': 'target',
#     'change': 0.05,  # 값이 커지면 민감하게 반응, 값이 작아지면 둔감하게 반응 (디폴트 : 0.05)
#     'logistic': 'f',  # True : t, False : f
#     'upper': 100,
#     'lower': 0,
#     'by': None
# }

delim = '='
result = {}
for arg in stat_argv:
	temp = arg.split(delim)
	result[temp[0]] = temp[1]
# user_param = result

time_col = '_time'
# time_pattern = re.compile('^\d{4}-\d{2}-\d{2}.*')
# for col in list(df.columns):
#     if time_pattern.match(str(df[col].iloc[0])):
#         time_col = col
#         pass

# default_param_key = list(default_param.keys())
# for key, value in user_param.items():
#     default_param[key] = value

freq = str((pd.Timestamp(df[time_col].iloc[1]) - pd.Timestamp(df[time_col].iloc[0])).seconds) + 's'

df_to_prophet = pd.DataFrame()
df_to_prophet['ds'] = df[time_col]
df_to_prophet['y'] = df[result['target']]

# if default_param['logistic'] == 't':
#     pass
    # df_to_prophet['cap'] = float(default_param['upper'])
    # df_to_prophet['floor'] = float(default_param['lower'])
    # m = Prophet(growth='logistic', changepoint_prior_scale=float(default_param['change']))
    # m.fit(df_to_prophet)
    # future = m.make_future_dataframe(periods=int(default_param['count']), freq=freq)
    # future['cap'] = float(default_param['upper'])
    # future['floor'] = float(default_param['lower'])
# else:
start_time_forecast = time.time()

m = Prophet(changepoint_prior_scale=float(result['change']))
m.fit(df_to_prophet)
future = m.make_future_dataframe(periods=int(result['count']), freq=freq)

forecast = m.predict(future)
forecast = pd.concat([df, forecast], axis=1)

end_time_forecast = time.time()

# if 'by' in user_param.keys():
#     forecast[user_param['by']].fillna(method='ffill', inplace=True)

start_time_print = time.time()

df = forecast
for i in range(len(df)):
    print(df.iloc[i].to_json())

end_time_print = time.time()

end_time_total = time.time()

print(json.dumps({'time_forecast':str(end_time_forecast-start_time_forecast)}))
print(json.dumps({'time_print':str(end_time_print-start_time_print)}))
print(json.dumps({'time_total':str(end_time_total-start_time_total)}))
