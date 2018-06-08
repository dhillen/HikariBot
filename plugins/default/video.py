if answ[1] == 'видео':
		param = (('v', '5.68'), ('q',answ_text),('count','10'),('access_token',token),('adult','1'),('forward_messages',torep))
		res = requests.post('https://api.vk.com/method/video.search', data=param)
		res = json.loads(res.text)
		info = ''
		if (res['response']['count'] != 0):
			for item in res['response']['items']:
				if item['id'] in (170754590,170631958,170067184,168063882,160911967,140239214,1609119666,166873080,166873080,166873080,166873080,166873080,166873080,166873080,160973038,166088674,166159461,456239165,159490950,169336720):
					continue
				if (item['title'].lower().find('банк') != -1) and (item['title'].lower().find('жоп') != -1):
					continue
				if (item['title'].lower().find('банк') != -1) and (item['title'].lower().find('сел') != -1):
					continue
				if (item['title'].lower().find('банк') != -1) and (item['title'].lower().find('мужик') != -1):
					continue
				if (item['title'].lower().find('мужик') != -1) and (item['title'].lower().find('сел') != -1):
					continue
				if (item['title'].lower().find('guy') != -1) and (item['title'].lower().find('cup') != -1):
					continue
				if (item['title'].lower().find('cup') != -1) and (item['title'].lower().find('guy') != -1):
					continue
				if item['title'].lower().find('theync') != -1:
					continue
				info = info+'video'+str(item['owner_id'])+'_'+str(item['id'])+','
			param = (('v', '5.68'), ('peer_id',toho),('access_token',token),('forward_messages',torep),('message','Видео по вашему запросу'),('attachment',info))
			requests.post('https://api.vk.com/method/messages.send', data=param)
		else:
			apisay('Видео по запросу не найдены.',toho,torep)
