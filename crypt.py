import pyAesCrypt,sys,os
for param in sys.argv:
    arg = sys.argv
p = input()
n = arg[1].split('.')
if n[len(n)-1] == 'enc':
	try:
		pyAesCrypt.decryptFile(arg[1], str(arg[1])[:str(arg[1]).rfind('.')], p, 512*1024)
		os.remove(arg[1])
	except ValueError:
		print('Неверный пароль')
else:
	try:
		pyAesCrypt.encryptFile(arg[1], arg[1] + '.enc', p, 512*1024)
		os.remove(arg[1])
	except OSError:
		print('Нет такого файла')