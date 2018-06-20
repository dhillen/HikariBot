if answ[1] == 'беседа' and answ[2] == 'имя':
	title = answ_text.replace(answ[2], '')
	title = title.lstrip()
	chat_id = str(toho)
	result = requests.get('https://api.vk.com/method/messages.editChat?access_token='+str(token)+'&v=5.68', params={'chat_id':chat_id[1::], 'title':title})
	
	if result == 1:
		apisay('Готово', toho, '')