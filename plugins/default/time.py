import datetime
if answ[1] == 'время':
	time = requests.get('http://worldclockapi.com/api/json/utc/now', params={'q':answ_text}).json()
	try:
		msg=""
		msg+='Время в ' +answ_text+': ' + str(time["currentFileTime"]);
		apisay(msg,toho,'')
	except:
		apisay('Я не нашла населённый пункт '+answ_text,toho,'')
#! py print net_send('http://worldclockapi.com/api/json/utc/now', {'q':'Иркутск'}, False)
#msg+='Время в: ' + str(time["currentFileTime"]);