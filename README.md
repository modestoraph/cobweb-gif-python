# 🕸️ Análise de Iterações Discretas via Cobweb Plot em Python

Este repositório é dedicado ao projeto cobweb feito em Python.

## Sobre o Projeto

O projeto **Análise de Iterações Discretas via Cobweb Plot** consiste em uma ferramenta desenvolvida em Python para visualização e análise de **Sistemas Dinâmicos Discretos**. A análise é realizada por meio do **Cobweb Plot** (Gráfico Teia de Aranha), um modelo gráfico que permite estudar o comportamento de funções iteradas $f(x_{n}) =x_{n+1}$  para identificar rapidamente pontos fixos, pontos periódicos e o início de comportamentos caóticos.

Este trabalho foi idealizado através da intenção de fazer uma **conexão direta com minha pesquisa de Iniciação Científica** na universidade, aplicando a teoria de Sistemas Dinâmicos com programação prática.

## Tecnologias e Habilidades Aplicadas

| Habilidade Técnica | Ferramenta/Conceito | Aplicação no Projeto |
| :--- | :--- | :--- |
| **Linguagem** | Python | Linguagem principal para desenvolvimento dos módulos. |
| **Visualização** | Matplotlib, Numpy | Geração de gráficos estáticos e animações (GIFs) dinâmicas do Cobweb Plot. |
| **Estrutura** | Programação Orientada a Objetos (POO) | Implementação da classe `Funcao` para modularizar as funções matemáticas. |
| **Robustez** | Tratamento de Erros | Garantia de que a interface de menu lida com entradas inválidas (não numéricas). |

## Estrutura do Repositório

O código está estruturado para separação de responsabilidades:

* **`arqs/Funcoes/funcoes.py`**: Contém a classe `Funcao` com as diversas funções analisadas (Logística, Reta, Raiz Quadrada, Cosseno, Expansora).
* **`arqs/Cobweb/cobweb.py`**: Contém a lógica de cálculo dos iterados e a construção visual do Cobweb Plot e suas animações.
* **`arqs/Menu_main/menu_main.py`**: A interface principal do programa que interage com o usuário, compila e executa as funções dos módulos.

## Status do Projeto e Melhorias Futuras

O código está **funcionando como previsto** e de acordo com a teoria matemática. Originalmente, o projeto foi desenvolvido na plataforma **Google Colab** e está em processo de adaptação e otimização para este repositório no GitHub.

**Este código ainda está sendo melhorado e otimizado.**
Existem diversas melhorias planejadas para um funcionamento ainda melhor do código, incluindo:

1.  **Aprofundamento da Análise:** Inserir a análise detalhada de pontos periódicos e pontos fixos.
2.  **Expansão da Biblioteca:** Inserir outras diversas funções dentro da classe `Funcao`.
3.  **Melhoria Visual:** Aprimorar os gráficos e animações geradas.
4.  **Referências:** Inserir todas as referências usadas até o momento e futuras.
5.  **Integração Acadêmica:** Inserção e expansão como parte do Trabalho de Conclusão de Curso (TCC).

---

## Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [Link do seu repositório]
    ```
2.  **Instale as dependências:**
    ```bash
    pip install numpy matplotlib pillow
    ```
3.  **Execute o arquivo principal:**
    ```bash
    python main.py
    ```
