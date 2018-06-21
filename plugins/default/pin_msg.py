if answ[1] == 'закреп':
	try:
		msg = requests.post('https://api.vk.com/method/messages.getConversationsById?access_token='+str(token)+'&v=5.68', params={'peer_ids': str(toho)})		
		torep = msg.json()['response']['items'][0]['chat_settings']['pinned_message']['id']
	
		apisay('Закрепленное сообщение: ', toho, torep)
	except:
		apisay('Нет закрепленных сообщений', toho, torep)