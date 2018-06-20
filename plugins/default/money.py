import datetime
if answ[1] == 'курс':
	money = requests.get('https://www.cbr-xml-daily.ru/daily_json.js', params={'q':answ_text}).json()
	btc = requests.get('https://blockchain.info/ru/ticker', params={'q':answ_text}).json()
	msg=""
	msg+="Актуальные курсы валют:\n"
	msg+='&#8195;•Доллар: ' + str(money["Valute"]["USD"]["Value"]) + ' RUB\n'
	msg+='&#8195;•Евро: ' + str(money["Valute"]["EUR"]["Value"]) + ' RUB\n'
	msg+='&#8195;•Белорусский рубль: ' + str(money["Valute"]["BYN"]["Value"]) + ' RUB\n'
	msg+='&#8195;•10 Гривен: ' + str(money["Valute"]["UAH"]["Value"]) + ' RUB\n'
	msg+='&#8195;•100 Тенге: ' + str(money["Valute"]["KZT"]["Value"]) + ' RUB\n'
	msg+="Курсы по отношению к рублю\n"
	msg+="\n"
	msg+="Курс BTC:\n"
	msg+='&#8195;•В долларах: ' + str(btc["USD"]["sell"]) + "\n"
	msg+='&#8195;•В рублях: ' + str(btc["RUB"]["sell"]) + "\n"
	#msg+='Время обновления: ' +datetime.datetime.utcfromtimestamp(["Date"]).strptime('%I:%M%p');
	apisay(msg,toho,'')