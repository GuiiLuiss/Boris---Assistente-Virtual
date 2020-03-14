version = "1.0.0"

def intro():
	msg = "Boris - version {} / by: Guilherme Luis Silva".format(version)
	print("-" * len(msg) +  "\n{}\n".format(msg)  +   "-" * len(msg))


lista_erros = [
		"Não escutei direito, pode falar novamente?",
		"Desculpe, não entendi",
		"Repita novamente por favor"
]

conversas1 = {
	"Bom dia Boris": "Bom dia mestre, como o senhor está?",
	"estou bem" or "Estou bem": "Como posso te ajudar hoje?",
    "Qual a previsão do tempo": "Hoje o clima é de sol, recomendo dar uma volta na praia",
    "que voz estranha": "Perdoe-me, ainda estou mexendo nas minhas configurações"
	}
	
conversas2 = {
	"sim": "Tudo bem, aguarde só um minuto",
	"Sim": "Tudo bem, aguarde só um minuto"

}

comandos = {
	"desligar": "desligando",
	"reiniciar": "reiniciando"
}

def verifica_nome(user_name):
	if user_name.startswith("Meu nome é"):
		user_name = user_name.replace("Meu nome é", "")
	if user_name.startswith("Eu me chamo"):
		user_name = user_name.replace("Eu me chamo", "")
	if user_name.startswith("Eu sou o"):
		user_name = user_name.replace("Eu sou o", "")
	if user_name.startswith("Eu sou a"):
		user_name = user_name.replace("Eu sou a", "")

	return user_name 

def  verifica_nome_exist(nome):
	if nome == "Guilherme" or nome == "guilherme":
		return "Bem vindo de volta Mestre!"
	else:
		return "Olá {}, como vai? Quer que eu chame meu mestre?".format(nome)
		