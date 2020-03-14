import speech_recognition as sr
import pyttsx3
from config import *
from random import choice

reproducao = pyttsx3.init()

def sai_som(reposta):
	reproducao.say(reposta)
	reproducao.runAndWait()

def assistente():
	print("Olá, com quem estou falando?")
	sai_som("Olá, com quem estou falando?")
	while True:
		resposta_erro_aleatoria = choice(lista_erros)
		rec = sr.Recognizer()

		with sr.Microphone() as s:
			rec.adjust_for_ambient_noise(s)

			while True:
				try:
					audio = rec.listen(s)
					user_name = rec.recognize_google(audio, language="pt")
					user_name = verifica_nome(user_name)
					apresentacao = "{}".format(verifica_nome_exist(user_name))
					print(apresentacao)
					sai_som(apresentacao)
		
					brute_user_name = user_name
					user_name = user_name.split(" ")
					user_name = user_name[0]
					break
				except sr.UnknownValueError:
					sai_som(resposta_erro_aleatoria)
			break
	print("Estou ouvindo, pode falar...")

	while True:
		resposta_erro_aleatoria = choice(lista_erros)
		rec = sr.Recognizer()

		with sr.Microphone() as s:
			rec.adjust_for_ambient_noise(s)

			while True:
				try:
					audio = rec.listen(s)
					entrada = rec.recognize_google(audio, language="pt")
					if user_name == "Guilherme" or user_name == "guilherme":
						resposta = conversas1[entrada]
					else:
						resposta = conversas2[entrada]

					print("{}: {}".format(user_name, entrada))
					print("Boris: {}".format(resposta))
					sai_som("{}".format(resposta))

				except sr.UnknownValueError:
					sai_som(resposta_erro_aleatoria)

if __name__ == '__main__':
	intro()
	sai_som("Iniciando")
	assistente()