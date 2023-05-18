# Compêndio

import keyboard
import os

def locais():
	os.system('clear')
	m = open("./locais/menu_locais", "r")
	print(m.read())
	val_key = keyboard.read_key()
	if val_key == 'a':
		del val_key
		while True:
			os.system('clear')
			f = open("./locais/locais_iserilha", "r")
			print(f.read())
			val_key = keyboard.read_key()
			if val_key == 'z':
				del val_key
				locais()
	elif val_key == 'x':
		run()
	locais()

def npcs():
	os.system('clear')
	m = open("./npcs/menu_npcs", "r")
	print(m.read())
	val_key = keyboard.read_key()
	if val_key == 'a':
		del val_key
		while True:
			os.system('clear')
			f = open("./npcs/npcs_jena", "r")
			print(f.read())
			val_key = keyboard.read_key()
			if val_key == 'z':
				del val_key
				npcs()
	elif val_key == 'x':
		run()
	npcs()

def itens():
	os.system('clear')
	m = open("./itens/menu_itens", "r")
	print(m.read())
	val_key = keyboard.read_key()
	if val_key == 'a':
		del val_key
		locais_iserilha()
	elif val_key == 'x':
		run()
	itens()

def magias():
	os.system('clear')
	m = open("./magias/menu_magias", "r")
	print(m.read())
	val_key = keyboard.read_key()
	if val_key == 'a':
		del val_key
		locais_iserilha()
	elif val_key == 'x':
		run()
	magias()

def seres():
	os.system('clear')
	m = open("./seres/menu_seres", "r")
	print(m.read())
	val_key = keyboard.read_key()
	if val_key == 'a':
		del val_key
		locais_iserilha()
	elif val_key == 'x':
		run()
	seres()

def run():
	os.system('clear')
	m = open("./menu_compendio", "r")
	print(m.read())
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
				f = open("./regras/regras", "r")
				print(f.read())
				val_key = keyboard.read_key()
				if val_key == 'x':
					del val_key
					run()
	run()

run()
