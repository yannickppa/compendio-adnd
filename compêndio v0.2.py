# Compêndio 0.2

import keyboard
import os

# locais

def title_locais():
	os.system('clear')
	print('-------------------------------')
	print(' $ Buscar ________ em "locais"')
	print(' ')
	print(' #x para voltar')
	print('-------------------------------')
	print(' ')
	print(' #a Iserilha')
	print(' ')

def locais():
	title_locais()
	val_key = keyboard.read_key()
	if val_key == 'a':
		del val_key
		while True:
			os.system('clear')
			f = open("/home/yannick/compêndio/v0.2/locais/locais_iserilha", "r")
			print(f.read())
			val_key = keyboard.read_key()
			if val_key == 'z':
				del val_key
				locais()
	elif val_key == 'x':
		title_adnd2e()
		run()
	locais()

# npcs

def title_npcs():
	os.system('clear')
	print('-------------------------------')
	print(' $ Buscar ________ em "npcs"')
	print(' ')
	print(' #x para voltar')
	print('-------------------------------')
	print(' ')
	print(' #a Jena, de Água Ruim')
	print(' ')

def npcs():
	title_npcs()
	val_key = keyboard.read_key()
	if val_key == 'a':
		del val_key
		while True:
			os.system('clear')
			f = open("/home/yannick/compêndio/v0.2/npcs/npcs_jena", "r")
			print(f.read())
			val_key = keyboard.read_key()
			if val_key == 'z':
				del val_key
				npcs()
	elif val_key == 'x':
		title_adnd2e()
		run()
	npcs()

# itens

def title_itens():
	os.system('clear')
	print('-------------------------------')
	print(' $ Buscar ________ em "itens"')
	print(' ')
	print(' #x para voltar')
	print('-------------------------------')
	print(' ')
	print(' #a Opção "a"')
	print(' ')

def itens():
	title_itens()
	val_key = keyboard.read_key()
	if val_key == 'a':
		del val_key
		locais_iserilha()
	elif val_key == 'x':
		title_adnd2e()
		run()
	itens()

# magias

def title_magias():
	os.system('clear')
	print('-------------------------------')
	print(' $ Buscar ________ em "magias"')
	print(' ')
	print(' #x para voltar')
	print('-------------------------------')
	print(' ')
	print(' #a Opção "a"')
	print(' ')

def magias():
	title_magias()
	val_key = keyboard.read_key()
	if val_key == 'a':
		del val_key
		locais_iserilha()
	elif val_key == 'x':
		title_adnd2e()
		run()
	magias()

# seres

def title_seres():
	os.system('clear')
	print('-------------------------------')
	print(' $ Buscar ________ em "seres"')
	print(' ')
	print(' #x para voltar')
	print('-------------------------------')
	print(' ')
	print(' #a Opção "a"')
	print(' ')

def seres():
	title_seres()
	val_key = keyboard.read_key()
	if val_key == 'a':
		del val_key
		locais_iserilha()
	elif val_key == 'x':
		title_adnd2e()
		run()
	seres()

# menu

def title_adnd2e():
	os.system('clear')
	print('-------------------------------')
	print(' $ Buscar _______ em "ad&d 2e"')
	print(' ')
	print('           -> compêndio  v0.1 ')
	print('-------------------------------')
	print(' ')
	print(' #1 locais')
	print(' #2 npcs')
	print(' #3 itens')
	print(' #4 magias')
	print(' #5 seres')
	print(' #6 regras')
	print('')

def run():
	if True:
		val_key = keyboard.read_key()
		if val_key == '1':
			del val_key
			locais()
		elif val_key == '2':
			del val_key
			npcs()
		elif val_key == '3':
			del val_key
			itens()
		elif val_key == '4':
			del val_key
			magias()
		elif val_key == '5':
			del val_key
			seres()
		elif val_key == '6':
			del val_key
			while True:
				os.system('clear')
				f = open("/home/yannick/compêndio/v0.2/regras/regras", "r")
				print(f.read())
				val_key = keyboard.read_key()
				if val_key == 'x':
					del val_key
					run()
	title_adnd2e()
	run()

# run

title_adnd2e()
run()
