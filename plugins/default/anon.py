if answ[1] == 'анонимка':
	apisay(open('files/txt/anon','r').read(),toho,'')
if answ[1] == 'анон':
	try:
		if answ_text.find('vk.com') != 0:
			domain = answ[2][15::]
			
			answ_text = answ_text.replace(answ[2], '')
			answ_text+='<br><br>------------<br>Анонимная доставка.<br>С вами бот, '+kb_name[0].capitalize()+'.'
			param = (('v', '5.68'), ('domain', domain),('access_token',token),('message',answ_text),('forward_messages',''))
			result = requests.post('https://api.vk.com/method/messages.send', data=param)
		else:
			answ_text = answ_text.replace(answ[2], '')
			apisay(answ_text+'<br><br>------------<br>Анонимная доставка.<br>С вами бот, '+kb_name[0].capitalize()+'.', answ[2], '')

		apisay('Доставлено',toho,'')
	except:
		apisay('Пользователь '+answ[2][15::]+' не найден!', toho, '')