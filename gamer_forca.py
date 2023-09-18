# Jogo em Python 1 

# Import
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():
	# Windows
	if name == 'nt':
		_=system('cls')
	# Mac ou Linux
else:
	_=system('clear')

# função
def gamer():
	limpa_tela()
	print("\nBem-Vindo(a) ao jogo da forca!")
	print("Adivinhe a palavra abaixo:\n")

	# Lista de palavras para o jogo
	palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

	# Escolher randomicamente uma palavracls
	palavra = random.choice(palavras)

	# List comprehension
	letras_descobertas = ['_' for letra in palavra]

	# Número de chances
	chances = 6

	# Lista para as letras erradas
	letras_erradas = []

	# Loop enquantonúmero de chances for maior do que zero
	while chances > 0:
		#Prints
		print(" ".join(letras_descobertas))
		print("\nLetras erradas:", " ".join(letras_erradas))
		#Tentativas
		tentativa = input("\nDigite uma letra: ").lower()

		#Condicional
		if tentativa in palavra:
			index = 0
			for letra in palavra:
				if tentativa == letra:
					letras_descobertas[index] = letra
				index += 1
		else:
			chances -= 1
			letras_erradas.append(tentativa)

		# Codincional
		if "_" not in letras_descobertas:
			print("\nVocê venceu, a palavra era:", palavra)
			break

	# Condicional
	if "_" in letras_descobertas:
		print("\nVocê perdeu, a palavra era:", palavra)

# Bloco main
if __name__ == "__main__":
	gamer()
	print("\nParabéns. Você está aprendendo programação em Python\n")