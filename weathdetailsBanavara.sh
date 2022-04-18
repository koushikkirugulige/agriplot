#!/bin/sh
cd /home/kirugulige/Desktop/agriplot/

echo -e "GET http://google.com HTTP/1.0\n\n" | nc google.com 80 > /dev/null 2>&1
if [ $? -eq 0 ]; then
	curl -X GET "http://dataservice.accuweather.com/currentconditions/v1/2858823?apikey=WNqFA0Pyr0YRhHILQ3iKeflcPfomqzKw&details=true" > /home/kirugulige/Desktop/agriplot/banavara_weather.json
fi
python3.6 /home/kirugulige/Desktop/agriplot/banavaradetails.py
