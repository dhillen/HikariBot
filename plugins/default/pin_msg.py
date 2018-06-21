if answ[1] == 'закреп':
	try:
		msg = requests.post('https://api.vk.com/method/messages.getConversationsById?access_token='+str(token)+'&v=5.68', params={'peer_ids': str(toho)})
		
		print(msg.json())
	
		apisay(msg.json()['response']['items'][0]['chat_settings']['pinned_message']['text'], toho, torep)
	except:
		apisay('Нет закрепленных сообщений', toho, torep)
		