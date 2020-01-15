import datetime
from datetime import timedelta, date
from datetime import datetime

a = {
	'id':12,
	'cal_30':1,
	'due_date_30':"06/23/2019",
	'cal_60':1,
	'due_date_60':"07/13/2019",
	'cal_80':0
}  
# initializing search key string 
search_key = 'cal_'
# Using items() + list comprehension 
# Substring Key match in dictionary 
res = [key for key, val in a.items() if search_key in key] 
  
# printing result  
for x in res:	
	# print( x)
	dayss=x[-2:]
	if a['cal_'+dayss] == 1:
		datetime_object = datetime.strptime(a['due_date_'+dayss], '%m/%d/%Y')
		print("cal_"+dayss+ " : " + str(a['cal_'+dayss]))
		print("due_date_"+dayss +" : " + str(datetime_object)) 
		EndDate = datetime_object + timedelta(days=int(dayss))
		print("es_due_date_"+dayss + " : " + str(EndDate))
	
