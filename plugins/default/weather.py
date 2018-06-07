#-*- coding: utf-8 -*-
import datetime
if answ[1] == 'погода':
	weather = requests.get('http://api.openweathermap.org/data/2.5/weather', params={'lang':'ru', 'units': 'metric', 'APPID': 'ef23e5397af13d705cfb244b33d04561', 'q':answ_text}).json()
	try:
		msg=""
		msg+="Погода в " + str(weather['sys']['country']) + "/" + str(weather["name"]) + ":\n"
		msg+='&#8195;•Температура: ' + str(weather["main"]["temp"]) + '°C\n'
		#msg+='&#8195;&#8195;Максимальная температура: ' + str(weather["main"]["temp_max"]) + '°C\n'
		#msg+='&#8195;&#8195;Минимальная температура: ' + str(weather["main"]["temp_min"]) + '°C\n'
		msg+='&#8195;•Скорость ветра: ' + str(weather["wind"]["speed"]) + ' м/с\n'
		msg+='&#8195;•Влажность: ' + str(weather["main"]["humidity"]) + '%\n'
		msg+='&#8195;•Состояние: ' + str(weather["weather"][0]["description"]) + "\n"
		#msg+='&#8195;•Давление: ' + str(weather["main"]["pressure"]) + ' кПа' +"\n"
		msg+='Время обновления: ' + datetime.datetime.fromtimestamp(weather["dt"]).strftime('%I:%M%p');
		apisay(msg,toho,'')
	except:
		apisay('Я не нашла населённый пункт '+answ_text,toho,'')
		#apisay('Если город не в РФ, пиши английское название',toho,'')
