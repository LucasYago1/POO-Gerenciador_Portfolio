# AVALIAÇÃO 3: Gerenciador de Portfólio de Ativos Financeiros

Este projeto foi desenvolvido como parte da Avaliação 3 da disciplina de Programação Orientada a Objetos.

**Participantes:**
* Lucas Yago Barankievicz
* Gean Rodrigues Duffeck

---

### 1. Contexto do Projeto

O **Gerenciador de Portfólio de Ativos Financeiros** é uma aplicação de console que resolve o problema de acompanhar o valor de diferentes tipos de ativos (como ações e criptomoedas) em um único lugar. A aplicação permite ao usuário criar um portfólio, adicionar ativos a ele e, em seguida, exibe um resumo consolidado, buscando os preços atuais de criptomoedas em tempo real através de uma API externa e apresentando os dados de forma clara e tabular.

### 2. Como Executar e Utilizar o Script

#### Pré-requisitos

Para executar o script, é necessário ter o Python 3 instalado e as seguintes bibliotecas:

* `requests`: Para fazer as chamadas à API da CoinGecko.
* `pandas`: Para criar e exibir a tabela do portfólio.

As dependências podem ser instaladas com o seguinte comando:

```bash
pip install requests pandas
```

#### Execução

Para executar a aplicação, basta rodar o script Python a partir do terminal:

```bash
python gerenciador_portfolio.py
```

### 3. Exemplo de Saída

Abaixo está um exemplo de como a saída do programa aparecerá no terminal. Note que os preços das criptomoedas são consultados em tempo real e, portanto, os valores mudarão a cada execução.

```text
--- Resumo do Portfolio: Minha Carteira de Testes ---
               Ativo Ticker  Quantidade   Preço (USD) Valor Total (USD)
Empresa Fictícia SA  Fict1       100.0        $34.50         $3,450.00
            Bitcoin    BTC         0.5    $65,432.10        $32,716.05
           Ethereum    ETH        10.0     $3,512.50        $35,125.00
-----------------------------------------------------
VALOR TOTAL DA CARTEIRA: $71,291.05
-----------------------------------------------------
```