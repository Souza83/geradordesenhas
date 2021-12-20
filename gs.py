import random
import string

# tamanho = 16
tamanho = int(input('Digite o tamanho da senha: '))  # Variável que recebe o tamanho de caracteres para gerar senha.

chars = string.ascii_letters + string.digits + '!@#$%&*()_-+=,.:/\|?Ç^~{}º[]ª'  # Variável que recebe letras, numeros e caracteres

rnd = random.SystemRandom()  #  Variável que recebe módulo randômico

print(''.join(rnd.choice(chars) for i in range(tamanho)))  #  Imprime a senha.
