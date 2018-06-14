resps={401:'Неправильный API-ключ', 402:'API-ключ заблокирован', 404:'Превышено суточное ограничение на объем переведенного текста', 413:'Превышен максимально допустимый размер текста', 422:'Текст не может быть переведен',501:'Заданное направление перевода не поддерживается'}
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
		msg+=resps.setdefault(translate["code"],'')
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
		msg+=resps.setdefault(translate["code"],'')
		apisay(msg,toho,'')
if answ[1] == 'перевод' and (answ[2] != 'языки' and answ[2] != 'помощь'):
	try:
		answ_text = answ_text.replace(answ[2], '')
		translate = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params={'key':'trnsl.1.1.20180614T000503Z.110edfa3eb89b4e1.0d17d98ca1ed35072e053e25e8ce00d5ada31afa', 'lang':answ[2], 'text':answ_text}).json()
		msg=""
		msg+="Перевод "+answ[2]+":\n"
		msg+=str(translate["text"])
		msg = msg.replace("['", '')
		msg = msg.replace("']", '')
		msg+=resps.setdefault(translate["code"],'')
		apisay(msg,toho,'')
	except:
		apisay("Язык не найден!", toho, torep)
if answ[1] == 'перевод' and answ[2] == 'языки':
	apisay(open('files/txt/langs','r').read(),toho,torep)
if answ[1] == 'перевод' and answ[2] == 'помощь':
	apisay('язык с которого переводят-язык на который переводят<br>(пример: ru-en - русско-английский перевод)', toho, torep)