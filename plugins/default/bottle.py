if (answ[1]=='бутылка'):	
					if (toho < 2000000000):
						apisay('Тут на бутылку посадят только тебя',toho,'')
					else:
						resapi = toho-2000000000;
						text = answ
						param = (('v', '5.68'), ('chat_id',resapi),('access_token',token))
						res = requests.post('https://api.vk.com/method/messages.getChatUsers', data=param)
						res = json.loads(res.text)
						rand = random.randint(0,len(res['response'])-1)
						param = (('v', '5.68'), ('user_ids',res['response'][rand]),('access_token',token))
						name = requests.post('https://api.vk.com/method/users.get', data=param)
						name = json.loads(name.text)
						id = str(name['response'][0]['id'])
						name = name['response'][0]['first_name']+' '+name['response'][0]['last_name']
						msg = ["Разминай анус","Присаживайся","Хорошего сидеть","Обутылен","Надеюсь, это приятно","Главное, что я не присяду","Тебе норм... Наверное","Теперь ты точно Россиянин","Оххх я не завидуют тебе"]
						n = random.randint(0,5)
						if n == 0:
							pic('but.jpg','Присядет на бутылочку у нас '+'[id'+id+'|'+name+']'+'<br>'+random.choice(msg), toho,'')
						elif n == 1:
							pic('but.jpg','Я уверена, на бутылке у нас '+'[id'+id+'|'+name+']'+'<br>'+random.choice(msg),toho,'')
						elif n == 2:
							pic('but.jpg','На бутылке - '+'[id'+id+'|'+name+']'+'<br>'+random.choice(msg),toho,'')
						elif n == 3:
							pic('but1.jpg','Бинго! Изысканная бутылка достается - '+'[id'+id+'|'+name+']'+'<br>'+random.choice(msg),toho,'')
						elif n == 4:
							pic('but.jpg','Я уверена, на бутылке у нас '+'[id'+id+'|'+name+']'+'<br>'+random.choice(msg),toho,'')
						else:
							pic('bank.jpg','Ууупс<br>Бутылки кончились, остались банки<br>Следовательно, на банку у нас сядет '+'[id'+id+'|'+name+']'+'<br>'+random.choice(msg),toho,'')