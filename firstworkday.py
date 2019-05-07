import requests
import datetime
import json
from datetime import timedelta,date

server_url = "http://api.goseek.cn/Tools/holiday?date="

mydate = datetime.datetime.now()  
day = mydate.strftime("%Y%m%d")    
print (day)


dayofmonth = int(mydate.strftime("%d")) 

if dayofmonth == 1:
	flag = True
else:
	flag = False


response = requests.get(server_url + day) 

if not response.raise_for_status():      
	timedata = json.loads(response.text)  
	daytype = int(timedata["data"]) 
	print (daytype)
	
		
if (daytype == 0 or daytype == 2) and flag:            
	print ("Today is first work day of this month")


if (daytype == 0 or daytype == 2) and (not flag):      
	i = 0
	flag1 = False
	beforeday = [0 for i in range(dayofmonth-1)]     
	testresponse = [0 for i in range(dayofmonth-1)]
	testtimedata = [0 for i in range(dayofmonth-1)]
	testdaytype = [0 for i in range(dayofmonth-1)]
	while(i < dayofmonth-1):                           
		beforeday[i] = (mydate - datetime.timedelta(days =i+1)).strftime("%Y%m%d")
		testresponse[i] = requests.get(server_url + beforeday[i])
		if not testresponse[i].raise_for_status():
				testtimedata[i] = json.loads(testresponse[i].text)
				testdaytype[i] = int(testtimedata[i]["data"])
				print (beforeday[i])
				print (testdaytype[i])
				if testdaytype[i] == 0 or testdaytype[i] == 2:  
						flag1 = True
						break
		i = i + 1
	if flag1:
		print ("Today is not first work day of this month")
	else:
		print ("Today is first work day of this month")
else:
	print ("Today is not first work day of this month") 