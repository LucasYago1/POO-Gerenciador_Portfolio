# -*- coding: utf-8 -*-

# Avaliacao 3 de POO
# Meu gerenciador de portfolio

import requests
import pandas as pd
from abc import ABC, abstractmethod


# REQUISITO: API de terceiros
# funcao pra pegar o preco da cripto na internet (usei a API do CoinGecko)
def obter_preco_cripto(id_da_api):
    # essa eh a url da api
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={id_da_api}&vs_currencies=usd"
    
    # try/except pra nao quebrar o programa se a internet cair ou o id tiver errado
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        # o preco vem dentro de um monte de coisa, tem que pegar assim
        return dados[id_da_api]['usd']
    except Exception as e:
        print(f"Deu erro ao pegar o preco de '{id_da_api}'")
        return 0.0


# REQUISITO: POO (Herança, Classe)
# classe PAI pra todas as outras. tipo um modelo.
# usei esse ABC pra ser uma classe abstrata
class Ativo(ABC):
    def __init__(self, nome, ticker, quantidade):
        self.nome = nome
        self.ticker = ticker
        self.quantidade = quantidade

    # toda classe filha TEM que ter esse metodo aqui
    @abstractmethod
    def obter_preco_atual(self):
        pass

    # aqui calcula o total (qtde * preco)
    def calcular_valor_total(self):
        return self.quantidade * self.obter_preco_atual()


# a classe Acao, que eh filha da classe Ativo
class Acao(Ativo):
    def __init__(self, nome, ticker, quantidade, preco_fixo):
        super().__init__(nome, ticker, quantidade)
        # aqui o preco da acao vai ser fixo, pra nao precisar de outra api
        self.preco_atual_fixo = preco_fixo

    # REQUISITO: Sobreposição (override)
    # esse metodo aqui eh o mesmo da classe Ativo, mas faz uma coisa diferente
    def obter_preco_atual(self):
        # so retorna o valor que eu ja defini antes
        return self.preco_atual_fixo


# classe pra cripto, filha de Ativo tbm
class Criptomoeda(Ativo):
    def __init__(self, nome, ticker, quantidade, id_da_api):
        super().__init__(nome, ticker, quantidade)
        self.id_da_api = id_da_api # id que a api coingecko usa

    # REQUISITO: Sobreposição (override)
    # aqui ele sobrepoe o metodo pra chamar a funcao da api la de cima
    def obter_preco_atual(self):
        return obter_preco_cripto(self.id_da_api)


# Classe que vai cuidar do portfolio todo
class Portfolio:
    # REQUISITO: Sobrecarga (simulada)
    # o construtor. um jeito de fazer a sobrecarga que o professor pediu.
    # pode criar o portfolio so com o nome, ou ja passar a lista de ativos
    def __init__(self, nome, ativos_iniciais=None):
        self.nome = nome
        if ativos_iniciais is None:
            self.lista_de_ativos = []
        else:
            self.lista_de_ativos = ativos_iniciais

    # pra colocar um ativo novo na lista
    def adicionar_ativo(self, ativo):
        self.lista_de_ativos.append(ativo)

    # REQUISITO: Biblioteca OO (Pandas)
    # aqui usa a biblioteca pandas pra fazer a tabela bonitinha
    def exibir_resumo(self):
        print(f"\n--- Resumo do Portfolio: {self.nome} ---")

        if not self.lista_de_ativos:
            print("Portfolio vazio!")
            return

        dados_para_tabela = []
        valor_total_geral = 0.0

        # passa por cada ativo na lista
        for ativo in self.lista_de_ativos:
            # pega o preco de cada um
            preco = ativo.obter_preco_atual()
            # calcula o valor total
            valor_total_do_ativo = ativo.calcular_valor_total()
            valor_total_geral += valor_total_do_ativo
            
            # dicionario com os dados de cada linha da tabela
            dados_para_tabela.append({
                "Ativo": ativo.nome,
                "Ticker": ativo.ticker,
                "Quantidade": ativo.quantidade,
                "Preço (USD)": f"${preco:,.2f}",
                "Valor Total (USD)": f"${valor_total_do_ativo:,.2f}"
            })
        
        # cria a tabela com o pandas
        tabela = pd.DataFrame(dados_para_tabela)
        print(tabela.to_string(index=False)) # to_string pra ficar mais bonito no console
        
        print("-----------------------------------------------------")
        print(f"VALOR TOTAL DA CARTEIRA: ${valor_total_geral:,.2f}")
        print("-----------------------------------------------------\n")


# aqui comeca o programa de verdade
def main():
    # funcao principal, pra testar tudo
    
    # criando o portfolio
    meu_portfolio = Portfolio("Minha Carteira de Testes")

    # criando os objetos
    acao1 = Acao(nome="Empresa Fictícia SA", ticker="Fict1", quantidade=100, preco_fixo=34.50)
    cripto1 = Criptomoeda(nome="Bitcoin", ticker="BTC", quantidade=0.5, id_da_api="bitcoin")
    cripto2 = Criptomoeda(nome="Ethereum", ticker="ETH", quantidade=10, id_da_api="ethereum")

    # adicionando as coisas no portfolio
    meu_portfolio.adicionar_ativo(acao1)
    meu_portfolio.adicionar_ativo(cripto1)
    meu_portfolio.adicionar_ativo(cripto2)

    # chama o metodo pra mostrar a tabela
    meu_portfolio.exibir_resumo()


# isso aqui eh pra rodar a funcao main quando eu executo o arquivo
if __name__ == "__main__":
    main()