if answ[1] == 'кик':
	if toho > 2000000000:
		chat_id = str(toho)
		users = requests.get('https://api.vk.com/method/messages.getChat?access_token='+str(token)+'&v=5.68', params={'chat_id':chat_id[1::], 'fields': 'first_name'})
		me = requests.get('https://api.vk.com/method/account.getProfileInfo?access_token='+str(token)+'&v=5.68')
		
		my_name = me.json()['response']['first_name']
		my_secname = me.json()['response']['last_name']
		try:
			for i in range(users.json()['response']['members_count']):
				if (answ[2] == users.json()['response']['users'][i]['first_name']) and (answ[3] == users.json()['response']['users'][i]['last_name']):
					if(answ[2] != my_name and answ[3] != my_secname):
						result = requests.get('https://api.vk.com/method/messages.removeChatUser?access_token='+str(token)+'&v=5.68', params={'chat_id':chat_id[1::], 'user_id':users.json()['response']['users'][i]['id']})
						apisay('Пока-пока', toho, '')
		except:
			apisay('Ошибочка вышла', toho, torep)
	else:
		apisay('Себя кикни!', toho, '')