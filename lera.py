import sys
import threading
import traceback
import psutil
import requests
import json
import os
import random
import time
import untangle
import urllib.parse
import logging
#немного логов бота
logging.basicConfig(filename="tmp/bot_log.log", level=logging.INFO)
logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")
#начало бота
token = open('system/cfg/token','r').read()
token = token.split('\n')[0]
kb_name = json.loads(open('system/cfg/name','r').read())['names']
answer_x = 0
answer_time = time.time()*100000 #заморозка бота при активных действиях
#Запрещенные слова
def inblacklist(answ):
	if answ[0].lower() not in kb_name:
		return False

	word = ' '.join(answ).lower()
	blacklist_words = json.loads(open('system/blacklist_words','r').read())
	
	for i in range(len(blacklist_words)-1):
		if word.find(blacklist_words[i]) != -1:
			return True

	return False
#Лонгполл
def apisay(text,toho,torep):
	time.sleep(random.randint(0,3)) #таймаут ответа бота, защита от капчи
	param = (('v', '5.68'), ('peer_id', toho),('access_token',token),('message',text),('forward_messages',torep))
	result = requests.post('https://api.vk.com/method/messages.send', data=param)
	return result.text
def exitgame():
	print(str(userid)+' покинул игру '+game_module['active_users'][str(userid)])
	del game_module['active_users'][str(userid)]
#Запрос изображения из директории изображений (tmp)
def sendpic(pic,mess,toho,torep):
	ret = requests.get('https://api.vk.com/method/photos.getMessagesUploadServer?access_token={access_token}&v=5.68'.format(access_token=token)).json()
	with open('tmp/'+pic, 'rb') as f:
		ret = requests.post(ret['response']['upload_url'],files={'file1': f}).text
	ret = json.loads(ret)
	ret = requests.get('https://api.vk.com/method/photos.saveMessagesPhoto?v=5.68&album_id=-3&server='+str(ret['server'])+'&photo='+ret['photo']+'&hash='+str(ret['hash'])+'&access_token='+token).text
	ret = json.loads(ret)
	requests.get('https://api.vk.com/method/messages.send?attachment=photo'+str(ret['response'][0]['owner_id'])+'_'+str(ret['response'][0]['id'])+'&message='+mess+'&v=5.68&forward_messages='+str(torep)+'&peer_id='+str(toho)+'&access_token='+str(token))
#Запрос изображения из директории изображений (img)
def pic(pic,mess,toho,torep):
	ret = requests.get('https://api.vk.com/method/photos.getMessagesUploadServer?access_token={access_token}&v=5.68'.format(access_token=token)).json()
	with open('files/img/'+pic, 'rb') as f:
		ret = requests.post(ret['response']['upload_url'],files={'file1': f}).text
	ret = json.loads(ret)
	ret = requests.get('https://api.vk.com/method/photos.saveMessagesPhoto?v=5.68&album_id=-3&server='+str(ret['server'])+'&photo='+ret['photo']+'&hash='+str(ret['hash'])+'&access_token='+token).text
	ret = json.loads(ret)
	requests.get('https://api.vk.com/method/messages.send?attachment=photo'+str(ret['response'][0]['owner_id'])+'_'+str(ret['response'][0]['id'])+'&message='+mess+'&v=5.68&forward_messages='+str(torep)+'&peer_id='+str(toho)+'&access_token='+str(token))
#Заявки в друзья
def friends():
	while True:
		try:
			friendslist = requests.post('https://api.vk.com/method/friends.getRequests',data={"access_token":token,"need_viewed":"1","v":"5.68"}).text
			friendslist = json.loads(friendslist)
			#print(friendslist)
			for frcount in range(len(friendslist['response']['items'])):
				requests.post('https://api.vk.com/method/friends.add',data={"access_token":token,"v":"5.68","user_id":friendslist['response']['items'][frcount]})
				print('Приняла заявку от id'+str(friendslist['response']['items'][frcount]))
			time.sleep(30)
		except Exception as error:
			print(error)
threading.Thread(target=friends).start()
open('tmp/msgs','w').write('')
data = requests.get('https://api.vk.com/method/messages.getLongPollServer?access_token='+str(token)+'&v=5.68&lp_version=2').text
data = json.loads(data)['response']
def evalcmds(directory,toho,torep,answ,answ_text):
	dir = os.listdir(directory)
	#print(dir)
	for plugnum in range(len(dir)):
		exec(open(directory+'/'+str(dir[plugnum]),'r').read())
game_module = open('system/game_module','r').read()
game_module = json.loads(game_module)
print('Лера запущена')
while True:
	if (time.time() - answer_time) > 60:
		answer_x = 0
		answer_time = time.time()*100000
	try:
		response = requests.get('https://{server}?act=a_check&key={key}&ts={ts}&wait=20&mode=2&version=2'.format(server=data['server'], key=data['key'], ts=data['ts'])).json() 
		try: 
			updates = response['updates'];
		except KeyError:
			data = requests.get('https://api.vk.com/method/messages.getLongPollServer?access_token='+str(token)+'&v=5.68&lp_version=2').text
			data = json.loads(data)['response']
			continue
		if updates: 
			for result in updates:
				if result[0] == 4:
					toho = result[3]
					torep = result[1]
					exec(open('system/auto.py','r').read())
					if (result[3] < 2000000000):
						userid = result[3]
					else:
						userid = result[6]['from']
						###game
					if (result[3] > 2000000000):
						if str(userid) in game_module['active_users']:
							answ_text = result[5].lower()
							print(str(userid)+' в игре '+game_module['active_users'][str(userid)])
							#print(game_module['games_info'][game_module['active_users'][userid]])
							def evalgames(answ_text,toho,torep):
								#print(game_module['games_info'][game_module['active_users'][userid]])
								#print(answ_text,toho,torep)
								exec(open(game_module['games_info'][game_module['active_users'][userid]],'r').read())
							thr = threading.Thread(target=evalgames,args=(answ_text,toho,torep))
							thr.start()
					###game
					open('tmp/msgs','a+').write(str(result)+'\n')
					#result[5] = result[5].lower()
					answ = result[5].split(' ')
					kb_cmd = json.loads(open('system/cmds','r').read())
					blacklist = json.loads(open('system/blacklist','r').read())
					#print(kb_cmd['default'])
					if len(answ) > 1:
						if str(userid) in blacklist:
							continue
						if inblacklist(answ) == True:
							apisay('Запрещенное для запроса слово', toho,'')	
							continue
						answ[0] = answ[0].lower()
						if answ[0].find(',') != -1:
							answ[0] = answ[0].replace(',','')
						answ[1] = answ[1].lower()
						if (str(userid) not in game_module['active_users'] and (answ[0] in kb_name) and ((answ[1] in kb_cmd["default"]) or (answ[1] in kb_cmd["vip"]) or (answ[1] in kb_cmd["admin"]))):
							print('[Упоминание Леры в '+str(toho)+']')
							answ_text = result[5].split(' ')
							if len(answ_text) >2:
								answ_text.remove(answ_text[0])
								answ_text.remove(answ_text[0])
							else:
								answ_text = ''
							answ_text = ' '.join(answ_text)
							try:
								thr = threading.Thread(target=evalcmds,args=('plugins/default',toho,torep,answ,answ_text))
								thr.start()
							except KeyError:
								pass
							viplist = json.loads(open('system/vip','r').read())
							adminlist = json.loads(open('system/cfg/admin','r').read())
							if str(userid) in viplist:
								try:
									thr1 = threading.Thread(target=evalcmds,args=('plugins/vip',toho,torep,answ,answ_text))
									thr1.start()
								except KeyError:
									pass
							else:
								if answ[1] in kb_cmd['vip']:
									apisay('Прости, но ты не VIP',toho,torep)
							if str(userid) in adminlist:
								try:
									thr1 = threading.Thread(target=evalcmds,args=('plugins/admin',toho,torep,answ,answ_text))
									thr1.start()
								except KeyError:
									pass
							else:
								if answ[1] in kb_cmd['admin']:
									apisay('Доступ к консоли только у админа, остальные нахуй',toho,torep)
						if ((answ[0] in kb_name) and (answ[1] not in kb_cmd["default"]) and (answ[1] not in kb_cmd["vip"]) and (answ[1] not in kb_cmd["admin"]) and (str(userid) not in game_module['active_users'])):
							blacklistcmds = ['гиф1','преакт1','цитата1','гцитата1']
							if answ[1] not in blacklistcmds:
								answtext = result[5].split(' ')
								answtext.remove(answtext[0])
								answtext = ' '.join(answtext)
								param = (('q',answtext),('adminname','RomkaZVO'))
								ret = requests.post('https://isinkin-bot-api.herokuapp.com/1/talk',data=param).json()
								apisay(ret['text'],result[3],result[1])
	except Exception as error:
		adminlist = json.loads(open('system/cfg/admin','r').read())
		print(error)
		apisay(error,adminlist[0],'')
	data['ts'] = response['ts']