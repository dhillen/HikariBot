import subprocess
if answ[1] == '!':
	if (answ_text == ''):
		apisay('Команду, мудень, не написал.',toho,'')
	else:
		cmd = answ_text.split('<br>')
		with open('tmp/cmd.sh', 'w') as cl:
			for i in range(len(cmd)):
				cl.write(cmd[i]+'\n')
		shell = subprocess.Popen('chmod 755 tmp/cmd.sh;bash tmp/cmd.sh',shell=True,stdout=subprocess.PIPE)
		output = shell.communicate()[0]
		apisay(output,toho,'')
