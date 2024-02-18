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

1. No módulo [Cards Game](./src/cards_game), implemente os métodos `shuffle` e `draw_cards` da classe `Deck`.  
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
