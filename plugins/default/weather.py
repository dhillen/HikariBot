#-*- coding: utf-8 -*-
if answ[1] == 'погода':
	weather = requests.get('http://api.openweathermap.org/data/2.5/weather', params={'lang':'ru', 'units': 'metric', 'APPID': 'ef23e5397af13d705cfb244b33d04561', 'q':answ_text}).json()
	try:
		msg=""
		msg+="погода в " + str(weather['sys']['country']) + "/" + str(weather["name"]) + ":\n"
		msg+='•температура: ' + str(weather["main"]["temp"]) + '°C\n'
		msg+='•скорость ветра: ' + str(weather["wind"]["speed"]) + 'м/с\n'
		msg+='•влажность: ' + str(weather["main"]["humidity"]) + '%\n'
		#msg+='•описание: ' + weather["weather"][0]["description"].encode('utf-8') + "\n";
		apisay(msg,toho,torep)
	except:
		apisay('Я не нашла этот населённый пункт',toho,torep)