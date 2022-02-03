# Tratamento de Erros e Exceções
import os
os.system('cls')
try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não digitar os dados.')
except Exception as erro:
    print(f'O erro foi {erro.__cause__}')

else:
    print(f'O resultao é {r:.2f}')
finally:
    print('Volte sempre!')