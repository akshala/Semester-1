#Akshala Bhatnagar
#Roll number - 2018012
# Section - A
#Group - 4

"""This program interacts with the openweathermap website to get weather data from which the desired results are extracted."""

import pprint
import datetime
from urllib.request import urlopen

API_key = 'b33af9e41291a17c9dcef37879d0db19'

# function to get weather response
def weather_response(location, API_key):
	""" Return the weather string
	Returns : a JSON string that is a response to a weather query 
	Parameter location: city name
	Parameter API key : a valid key of weather service"""
	url = 'http://api.openweathermap.org/data/2.5/forecast?'
	urlStr = url + 'q=' + location + '&APPID=' + API_key
	with urlopen(urlStr) as conn:
		jsonStr = conn.read().decode('utf-8')
		# print (jsonStr)
		return jsonStr

# function to check for valid response 
def get_epochTime(n=0, t='3:00:00'):
	""" Return epoch time corresponding to input day and time"""
	today = datetime.datetime.now()
	day = today.day
	month = today.month
	year = today.year
	timeElts = t.split(':')
	hours = int(timeElts[0].strip(' '))
	epochTimeStr = (datetime.datetime(year, month, day) + datetime.timedelta(days = n, hours = hours) + datetime.timedelta(hours=5, minutes =30)).strftime('%s')
	epochTime = int(epochTimeStr)
	return epochTime

# function to get attributes on nth day
def parse_string(json, paramStr, epochTime):
	dateLoc = json.find('"dt":'+str(epochTime))
	if dateLoc == -1:
		return 0
	paramLoc = json.find(paramStr, dateLoc)
	if paramLoc == -1:
		return 0
	commaLoc = json.find(',', paramLoc+len(paramStr))
	if commaLoc == -1:
		return 0
	return float(json[paramLoc+len(paramStr):commaLoc])


def get_temperature(json, n=0, t='3:00:00'):
	"""Return the temperature of the nth day from current date
	Parameter: json is a json string to parse
	n: Day from current day, values 0-4
	t : time , valid values are 3:00, 6:00, 9:00, 12:00, 15:00, 18:00, 21:00"""
	if n>=0 and n<=4:
		epochTime = get_epochTime(n,t)
		paramStr = '"temp":'
		return parse_string(json, paramStr, epochTime)
	else:
		return 0



def get_humidity(json, n=0, t='3:00:00'):
	"""Return the humidity of the nth day from current date
	Parameter: json is a json string to parse
	n: Day from current day, values 0-4
	t : time , valid values are 3:00, 6:00, 9:00, 12:00, 15:00, 18:00, 21:00"""
	if n>=0 and n<=4:
		epochTime = get_epochTime(n,t)
		paramStr = '"humidity":'
		return parse_string(json, paramStr, epochTime)
	else:
		return 0


def get_pressure(json, n=0, t='3:00:00'):
	"""Return the pressure of the nth day from current date
	Parameter: json is a json string to parse
	n: Day from current day, values 0-4
	t : time , valid values are 3:00, 6:00, 9:00, 12:00, 15:00, 18:00, 21:00"""
	if n>=0 and n<=4:
		epochTime = get_epochTime(n,t)
		paramStr = '"pressure":'
		return parse_string(json, paramStr, epochTime)
	else:
		return 0


def get_sealevel(json, n=0, t='3:00:00'):
	"""Return the sea_level of the nth day from current date
	Parameter: json is a json string to parse
	n: Day from current day, values 0-4
	t : time , valid values are 3:00, 6:00, 9:00, 12:00, 15:00, 18:00, 21:00"""
	if n>=0 and n<=4:
		epochTime = get_epochTime(n,t)
		paramStr = '"sea_level":'
		return parse_string(json, paramStr, epochTime)
	else:
		return 0

def get_wind(json, n=0, t='3:00:00'):
	"""Return the wind of the nth day from current date
	Parameter: json is a json string to parse
	n: Day from current day, values 0-4
	t : time , valid values are 3:00, 6:00, 9:00, 12:00, 15:00, 18:00, 21:00"""
	if n>=0 and n<=4:
		epochTime = get_epochTime(n,t)
		paramStr = '"wind":{"speed":'
		return parse_string(json, paramStr, epochTime)
	else:
		return 0


def has_error(location, json):
	"""Returns : True if the input location and response city name is not matched
	Parameter: json is a json string to parse
	location: location"""
	cityLoc = json.find('"city":')
	paramStr = '"name":"'
	paramLoc = json.find(paramStr, cityLoc)
	quoteLoc = json.find('"', paramLoc+len(paramStr)+1)
	cityName = json[paramLoc+len(paramStr):quoteLoc]
	if cityName != location:
		return True
	return False

# location = input()
# jsonStr = weather_response(location, API_key)
# # print(jsonStr)
# print (has_error(location, jsonStr))
# print (get_temperature(jsonStr, 1, '15:00:00'))
# print (get_pressure(jsonStr, 1, '15:00:00'))
# print (get_humidity(jsonStr, 1, '15:00:00'))
# print (get_sealevel(jsonStr, 1, '15:00:00'))
# print (get_wind(jsonStr, 1, '15:00:00'))


