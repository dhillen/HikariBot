#В этом скрипте происходит автоматические триггеры бота на конкретные действия
#Бот реагирует на добавление юзера в чат
if 'source_act' in result[6]:
	if result[6]['source_act'] == 'chat_invite_user':
		if answer_x >= 3:
			answer_time = time.time()
		else:
			param = (('v', '5.68'), ('user_ids',result[6]['source_mid']),('access_token',token))
			name = requests.post('https://api.vk.com/method/users.get', data=param)
			name = json.loads(name.text)
			name = name['response'][0]['first_name']+' '+name['response'][0]['last_name']
			#Приветствие:
			apisay('Привет, '+name+'<br>В беседе есть бот - '+kb_name[0]+'<br>Напиши "'+kb_name[0]+' помощь", чтоб увидеть список команд или "инфо" для того, что бы узнать больше информации о боте.<br>Хочешь в друзья? Заявка обрабатывается автоматически',toho,'')
			answer_x += 1
#На кик/ливание юзера
if 'source_act' in result[6]:
	if result[6]['source_act'] == 'chat_kick_user':
		if answer_x >= 3:
			answer_time = time.time()
		else:
			param = (('v', '5.78'), ('user_ids',result[6]['source_mid']),('access_token',token))
			name = requests.post('https://api.vk.com/method/users.get', data=param)
			name = json.loads(name.text)
			name = name['response'][0]['first_name']+' '+name['response'][0]['last_name']
			msg = ["Надеюсь, он не вернется", "Неееет!", "Не будем поминать", "Помянем его", "Вот и славно","Пишем F","-1","Похуй"]
			apisay('Пользователь '+name+' покинул нас.<br>'+random.choice(msg),toho,'')
			answer_x += 1
#Ебучий гусь
#if result[5].lower().find('гусь') != -1:
    #apisay(open('files/txt/gusi/goose'+str(random.randint(1,12)),'r').read(),toho,'')
#Отправляет луну
if result[5].lower().find('луна') != -1:
	quotes = json.loads(open('files/txt/quotes/moon','r').read())
	apisay(random.choice(quotes), toho, '')