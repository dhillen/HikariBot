if answ[1] == 'шифр':
	if (answ_text == ''):
		apisay('А с чем работать?',toho,torep)
	else:
		s=answ_text
		out=''
		for ch in s:
			out+=chr(ord(ch)-3)
		apisay(out,toho,torep)
if answ[1] == 'дешифр':
	if (answ_text == ''):
		apisay('А с чем работать?',toho,torep)
	else:
		s=answ_text
		out=''
		for ch in s:
			out+=chr(ord(ch)+3)
		if out.find('#') != -1:
			out = out.replace('#', ' ')
		apisay(out,toho,torep)
