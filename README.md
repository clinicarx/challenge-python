# Avaliação de conhecimentos em Python

Este projeto busca avaliar conhecimentos de candidatos à vagas para trabalhar no
clinicarx.

O desafio é fazer com que todos os testes do unittest sejam bem sucedidos.

## Instalação via `docker`

Pré-requisitos:

* [git](https://git-scm.com/)
* [docker](https://docs.docker.com/install/#server)
* [docker-compose](https://docs.docker.com/compose/install/)


O candidato deverá clonar o repositório e, na pasta do projeto, gerar a build do docker:

```shell
git clone https://git.clinicarx.dev/challenge/python.git challenge-python
cd challenge-python
```

## Executando os testes

Na pasta do projeto, execute o comando:

```shell
docker-compose run unittest
```

## Tarefas

Lista de correções e melhorias necessárias.

> **Atenção:**  
> Apenas os arquivos na pasta [`src`](./src) devem ser modificados.  
> Os arquivos de testes nas pastas [`test`](./tests) e [`lib`](./lib) NÃO devem ser alterados.    

### Módulo [Cards Game](./src/cards_game)

O módulo `cards_game` contém as classes `Card` (carta) e `Deck` (baralho).
Apenas a classe `Deck` precisa ser modificada.

1. Implementar o método `shuffle` para embaralhar as cartas, 
   sem causar erro de memória.
2. Implementar o método `draw_cards` para sacar as cartas do baralho, até que as cartas acabem.

A tarefa está concluída quando os testes unitários estiverem sendo aceitos.

### Módulo [Tabnet](./src/tabnet)

[Tabnet](https://datasus.saude.gov.br/informacoes-de-saude-tabnet/) é o portal de dados de saúde do Datasus. 

O módulo `tabnet` contém uma classe `TabFile`, que lê o arquivo [`lib/idb2012.tab`](./lib/idb2012.tab), 
com os dados da população das capitais entre 1990 e 2012.

1. Implementar o método estático `parse` para ler o arquivo e gerar uma instância da classe com os dados corretamente. 
2. Implementar o método `sumByYear`, que agrupa os dados por Ano, filtra o ano de acordo com o parâmetro especificado 
   e retorna o total do ano desejado.  

A tarefa está concluída quando os testes unitários estiverem sendo aceitos.

## Conclusão

Durante a realização das tarefas, as alterações devem ser confirmadas (via commit), 
para criar uma linha do tempo compreensível no histórico do git.

Quando todos os testes estiverem passando pelo unittest, o repositório deve
ser encapsulado num arquivo bundle.

```shell
# Altere "nome_sobrenome" para seu nome e sobrenome, separado por _ 
git bundle create nome_sobrenome.bundle master
```

O arquivo gerado (`nome_sobrenome.bundle`) deve ser enviado para o email: 
[alysson@clinicarx.com.br](mailto:alysson@clinicarx.com.br)
