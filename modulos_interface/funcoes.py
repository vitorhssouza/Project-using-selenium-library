from robo_bovespa.objeto import Empresa, Uol, B3
from time import sleep

try:
    def linha(tamanho: int = 90) -> None:
        print(tamanho * '=')


    def menu() -> None:
        """Interface gráfica do usuário """
        linha()
        print('PROJETO SELENIUM'.center(90))
        print('RASPAGEM DA BOLSA DE VALORES DO SITE UOL'.center(90))
        linha()
        print('1  - CÓDIGOS DE AÇÕES NO SITE DA B3\n'
              '2  - INFORME O CÓDIGO DAS AÇÕES QUE DESEJA VERIFICAR SEU VALOR\n'
              '3  - SAIR DO SISTEMA')

        opcao: int = int(input('Informe sua opção: '))
        escolha_opcao(opcao)


    def escolha_opcao(opcao: int) -> None:
        """Função que recebe a escolha do usuário e interage com o sistema"""
        if opcao == 1:
            linha()
            print('Abrindo o site da B3 para visualizar códigos das ações ')
            sleep(3)
            empresa = B3('https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br')
            print(empresa.site)
            print('Retornando ao menu')
            sleep(2)
            menu()
        elif opcao == 2:
            nome_empresa()
            linha()
            print('Retornando ao menu')
            sleep(3)
            menu()
        elif opcao == 3:
            print('Saindo do sistema')
            sleep(2)
            exit()
        else:
            print('Opção inválida. Tente novamente.')
            sleep(2)
            menu()


    def nome_empresa() -> list:
        """Essa função cria uma lista com os códigos das empresas que seram buscada no site uol para visulização
           dos valores atual de suas ações"""
        empresas = list()
        while True:
            empresas.append(str(input('Informe o nome das empresas: ')).upper().replace(' ', ''))
            while True:
                opcao = int(input('Deseja informa mais alguma empresa? 1-Sim ou 2-Não '))
                if opcao < 1 or opcao > 2:
                    print('Informe apenas 1-Sim ou 2-Não ')
                elif opcao == 1:
                    break
                elif opcao == 2:

                    break
            if opcao == 2:
                linha()
                break
        codigos_empresas = Empresa(empresas)
        sleep(2)
        print('Imprimindo as cotações das empresas ')
        uol = Uol(empresas, 'https://economia.uol.com.br/cotacoes/bolsas/')
        print(uol.uol)
except:
    print('Ocorreu algum erro')






