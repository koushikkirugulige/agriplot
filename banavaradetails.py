import pandas as pd
import json
import codecs
from datetime import datetime
import os
file = 'banavara_weather.json'

with codecs.open(file,encoding='utf-8') as data_file:   
        if os.stat(file).st_size != 0:        
            data = json.load(data_file)       
            df = pd.DataFrame(data=None)      
            df = pd.json_normalize(data, sep = "_")                  

            UVIndex = float(df['UVIndex']) 
            UVIndexText = list(df['UVIndexText'])[0]
            WeatherText =list(df['WeatherText'])[0]
            HasPrecipitation= list(df['HasPrecipitation'])[0]
            RelativeHumidity= int(df['RelativeHumidity'])
            CloudCover = list(df['CloudCover'])[0]
            Temperature_Metric_Value= float(df['Temperature_Metric_Value'])
            RealFeelTemperature_Metric_Value= float(df['RealFeelTemperature_Metric_Value'])  
            RealFeelTemperature_Metric_Phrase= list(df['RealFeelTemperature_Metric_Phrase'])[0]   
            DewPoint_Metric_Value= float(df['DewPoint_Metric_Value'])
            Wind_Direction_Degrees= float(df['Wind_Direction_Degrees'])
            Wind_Direction_Localized = list(df['Wind_Direction_Localized'])[0]
            Wind_Speed_Metric_Value = float(df['Wind_Speed_Metric_Value'])  
            Visibility_Metric_Value = float(df['Visibility_Metric_Value']) 
            Pressure_Metric_Value = float(df['Pressure_Metric_Value'])
            PrecipitationSummary_Past24Hours_Metric_Value= float(df['PrecipitationSummary_Past24Hours_Metric_Value'])
            TemperatureSummary_Past24HourRange_Minimum_Metric_Value= float(df['TemperatureSummary_Past24HourRange_Minimum_Metric_Value'])

            TemperatureSummary_Past24HourRange_Maximum_Metric_Value= float(df['TemperatureSummary_Past24HourRange_Maximum_Metric_Value'])
time_start = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
time_start

UVcsv = 'TempUVinfo.csv'
file1 = open(UVcsv, "a")  # append mode
file1.write('\n' + str(time_start) + ', '+ str(UVIndex) + ', ' + str(UVIndexText) + ', ' + str(WeatherText) + ', '+ str(HasPrecipitation) + ', '+ str(RelativeHumidity) + ', '+ str(CloudCover) + ', ' + str(Temperature_Metric_Value) + ' ,' +  str(RealFeelTemperature_Metric_Value) + ' ,' +  str(RealFeelTemperature_Metric_Phrase) + ' ,' +  str(DewPoint_Metric_Value) + ' ,' +  str(Wind_Direction_Degrees) + ' ,' +  str(Wind_Direction_Localized) + ' ,' +  str(Wind_Speed_Metric_Value) + ' ,' +  str(Visibility_Metric_Value) + ' ,' +  str(Pressure_Metric_Value) + ' ,' +  str(PrecipitationSummary_Past24Hours_Metric_Value) + ' ,' +  str(TemperatureSummary_Past24HourRange_Minimum_Metric_Value) + ' ,' +  str(TemperatureSummary_Past24HourRange_Maximum_Metric_Value))
file1.close()
