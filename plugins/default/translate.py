if answ[1] == 'переводчик':
	apisay(open('files/txt/translate','r').read(),toho,'')
if answ[1] == 'рус':
	if (answ_text == ''):
		apisay('А что мне переводить?<br>Нужен английский текст',toho,'')
	else:
		translate = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params={'key':'trnsl.1.1.20180614T000503Z.110edfa3eb89b4e1.0d17d98ca1ed35072e053e25e8ce00d5ada31afa', 'lang':'en-ru', 'text':answ_text}).json()
		msg=""
		msg+="Англо-русский перевод:\n"
		msg+=str(translate["text"])
		msg = msg.replace("['", '')
		msg = msg.replace("']", '')
		apisay(msg,toho,'')
if answ[1] == 'анг':
	if (answ_text == ''):
		apisay('А что мне переводить?<br>Нужен русский текст',toho,'')
	else:
		translate = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params={'key':'trnsl.1.1.20180614T000503Z.110edfa3eb89b4e1.0d17d98ca1ed35072e053e25e8ce00d5ada31afa', 'lang':'ru-en', 'text':answ_text}).json()
		msg=""
		msg+="Русско-английский перевод:\n"
		msg+=str(translate["text"])
		msg = msg.replace("['", '')
		msg = msg.replace("']", '')
		apisay(msg,toho,'')