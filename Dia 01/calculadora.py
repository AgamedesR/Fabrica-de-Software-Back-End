import os

def nome_do_programa():
    print('''
          **********************
          CALCURADORA MATEMÁTICA
          **********************
          ''')

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def exibir_opcoes():
    print('\nEscolha a operação desejada:')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('5 - Sair do programa')

def sair_do_programa():
    os.system('cls')

def voltar_menu_principal():
      input('\nDigite uma tecla para voltar ao menu principal: ')
      main()

def opcao_invalida():
    print('\nOpção inválida!')
    voltar_menu_principal()

def escolher_opcoes():
    opcao_escolhida = int(input('\nDigite a opção desejada: '))
    try:
        if opcao_escolhida == 1:
            operacao_somar()
        elif opcao_escolhida == 2:
            operacao_subtracao()
        elif opcao_escolhida == 3:
            operacao_multiplicacao()
        elif opcao_escolhida == 4:
            operacao_divisao()
        elif opcao_escolhida == 5:
            sair_do_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def solicitar_numeros():
    primeiro_numero = int(input('Digite o primeiro número inteiro: '))
    segundo_numero = int(input('Digite o segundo número inteiro: '))
    return primeiro_numero, segundo_numero

def operacao_somar():
    exibir_subtitulo('Operação de Soma')
    primeiro_numero, segundo_numero = solicitar_numeros()
    soma = primeiro_numero + segundo_numero
    print(f'A soma dos números é: {soma}')
    voltar_menu_principal()

def operacao_subtracao():
    exibir_subtitulo('Operação de Subtração')
    primeiro_numero, segundo_numero = solicitar_numeros()
    subtracao = primeiro_numero - segundo_numero
    print(f'A subtração dos números é: {subtracao}')
    voltar_menu_principal()

def operacao_multiplicacao():
    exibir_subtitulo('Operação de Multiplicação')
    primeiro_numero, segundo_numero = solicitar_numeros()
    multiplicacao = primeiro_numero * segundo_numero
    print(f'A multiplicação dos números é: {multiplicacao}')
    voltar_menu_principal()

def operacao_divisao():
    exibir_subtitulo('Operação de Divisão')
    primeiro_numero, segundo_numero = solicitar_numeros()
    divisao = primeiro_numero / segundo_numero
    print(f'A divisão dos números é: {divisao}')
    voltar_menu_principal()

def main():
    os.system('cls')
    nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == "__main__":
    main()



