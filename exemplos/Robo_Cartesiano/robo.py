"""
Projeto : Robô Cartesiano
Arquivo : robo.py
Descrição : Programa principal da simulação do robô cartesiano.
Autor : Charles Cesar Magno de Freitas
Licença : MIT


* Responsabilidade do módulo

    Este arquivo representa o ponto de entrada da aplicação.

    Sua responsabilidade é apenas coordenar o fluxo principal:

        - leitura da configuração;
        - execução da movimentação;
        - geração do relatório;
        - gravação do resultado.


    O programa principal não contém regras de negócio.


* Fluxo do módulo


                executar()
                    ↓
                lerConfiguracao()
                    ↓
                Configuracao
                    ↓
                executarMovimentos()
                    ↓
                ResultadoExecucao
                    ↓
                gerarRelatorio()
                    ↓
                Relatório
                    ↓
                gravarRelatorio()
                    ↓
                robo_output.txt


* Tratamento de exceções

    - Exceções específicas são tratadas pelos módulos responsáveis.
    - Este arquivo realiza apenas o tratamento global da aplicação.

    Objetivos:

        - impedir encerramento abrupto;
        - apresentar mensagens amigáveis;
        - manter fluxo controlado.


* Decisões arquiteturais


    1. Orquestração centralizada
        - O arquivo robo.py conhece os módulos principais.
        - Os módulos internos não conhecem o programa principal.


    2. Ausência de lógica de negócio
        - Toda regra permanece encapsulada em roboLibrary.


    3. Preparação para futuras interfaces
        - O fluxo principal está isolado na função executar().
        - Permite futuramente integração com:
            - interface gráfica;
            - API;
            - testes automatizados.


* Roadmap

    [V1]
        - Execução via terminal;
        - Leitura de arquivo INI;
        - Simulação cartesiana;
        - Geração de relatório textual.

    [V2]
        - Interface gráfica;
        - Execução interativa;
        - Visualização do plano cartesiano.

    [V3]
        - API;
        - Persistência de simulações;
        - Integração com banco de dados.


* Conclusão

    O módulo robo.py segue os princípios:
        - Responsabilidade Única;
        - Baixo acoplamento;
        - Alta coesão;
        - Separação entre controle e regras de negócio;
        - Facilidade de evolução.
"""


from roboLibrary.funcoesArquivo import (lerConfiguracao, gravarRelatorio)

from roboLibrary.funcoesMovimento import (executarMovimentos)

from roboLibrary.funcoesRelatorio import (gerarRelatorio)

from roboLibrary.excecoes import (RoboCartesianoException)


# --------------------------------------------------------------------------------------------------
# Executa o fluxo principal da aplicação.
def executar() -> None:
    print("\nIniciando simulação do robô cartesiano...")
    configuracao = lerConfiguracao()

    print("Executando movimentação...")
    resultado = executarMovimentos(configuracao)

    print("Gerando relatório...")
    relatorio = gerarRelatorio(resultado)
    gravarRelatorio(relatorio)
    print("Relatório gravado com sucesso.")



# --------------------------------------------------------------------------------------------------
# Ponto de entrada da aplicação.
if __name__ == "__main__":
    try:
        executar()
    except RoboCartesianoException as erro:
        print("\nERRO NA EXECUÇÃO DO ROBÔ:")
        print(erro)
    except Exception as erro:
        print("\nERRO INESPERADO:")
        print(erro)