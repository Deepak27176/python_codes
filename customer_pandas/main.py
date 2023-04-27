import pandas as pd
from datetime import datetime as dt
dataframe = pd.read_csv('assignment_python (1).csv')

dataframe['DEPOSIT_DATE'] = pd.to_datetime(dataframe['DEPOSIT_DATE'])
dataframe['REGISTRATION_DATE'] = pd.to_datetime(dataframe['REGISTRATION_DATE'])
dataframe['Customer Life time'] = dataframe['DEPOSIT_DATE']-dataframe['REGISTRATION_DATE']


lifetime = dataframe[dataframe.IDCUSTOMER == 5371454]
print(lifetime['Customer Life time'])

