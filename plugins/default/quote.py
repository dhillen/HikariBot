import textwrap
from PIL import Image, ImageDraw, ImageFont
if answ[1] == 'цитата':
	#####
	resnew = requests.get('https://api.vk.com/method/messages.getById?access_token='+token+'&v=5.68&message_ids='+str(torep)).text
	#print(resnew)
	resnew = json.loads(resnew)
	#print(resnew)
	id = resnew['response']['items'][0]['fwd_messages'][0]['user_id']
	ret = requests.post('https://api.vk.com/method/users.get',data={'v':'5.68','user_ids':id,'access_token':token,'fields':'photo_max'}).json()
	text = ''
	for k in range(len(resnew['response']['items'][0]['fwd_messages'])):
		text += resnew['response']['items'][0]['fwd_messages'][k]['body']+'\n'
	text = text.replace('\n','<br>')
	url = ret['response'][0]['photo_max']
	name = ret['response'][0]['first_name']+' '+ret['response'][0]['last_name'] + ':'
	avatar = requests.get(url, stream=True).raw
	#####
	avatar = Image.open(avatar)
	avatar = avatar.resize([180,180],resample=Image.BILINEAR)
	data = textwrap.wrap(text, 50)
	data = '<br>'.join(data)
	data = data.split('<br>')
	y = 270+(40*len(data))
	fnt = ImageFont.truetype('/home/pid/lera_bot/files/fonts/font.ttf', 37)
	title = ImageFont.truetype('/home/pid/lera_bot/files/fonts/font1.ttf', 60)
	img = Image.new('RGB', (1050, y), color = (255,255,255))
	d = ImageDraw.Draw(img)
	d.rectangle([0,0,750,150],outline=None,fill=(255,255,255))
	img.paste(avatar,[0,0,180,180])
	#d.text((0,50), '\n'.join(data), font=fnt, fill=(0, 0, 0))
	offset = 210
	for line in range(len(data)):
		#print(str(line)+':'+data[line])
		d.text((40,offset),data[line],font=fnt,fill=(0,0,0))
		offset += 50
		#print(offset)
	d.text((350, 60), name, font=title, fill=(0, 0, 0))
	img.save('tmp/quote.jpg')
	sendpic('quote.jpg','',toho,'')
