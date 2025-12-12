# Análise de Iterações Discretas via Cobweb Plot em Python

Este repositório é dedicado ao projeto cobweb em python.

## Sobre o Projeto

[cite_start]O projeto **Análise de Iterações Discretas via Cobweb Plot** consiste em uma ferramenta desenvolvida em Python para visualização e análise de **Sistemas Dinâmicos Discretos**[cite: 27].
[cite_start]A análise é realizada por meio do **Cobweb Plot** (Gráfico Teia de Aranha) [cite: 42][cite_start], um modelo gráfico que permite estudar o comportamento de funções iteradas ($x_{n+1} = f(x_{n})$) [cite: 50] [cite_start]para identificar rapidamente pontos fixos, pontos periódicos e o início de comportamentos caóticos[cite: 51].

[cite_start]Este trabalho se idealizou através da intenção de fazer uma **conexão direta com minha pesquisa de Iniciação Científica** na universidade, aplicando a teoria de Sistemas Dinâmicos com programação prática. [cite: 19]

## Tecnologias e Habilidades Aplicadas

| Habilidade Técnica | Ferramenta/Conceito | Aplicação no Projeto |
| :--- | :--- | :--- |
| **Linguagem** | [cite_start]Python [cite: 3] | Linguagem principal para desenvolvimento dos módulos. |
| **Visualização** | [cite_start]Matplotlib [cite: 71][cite_start], Numpy [cite: 70] | [cite_start]Geração de gráficos estáticos e animações (GIFs) dinâmicas do Cobweb Plot[cite: 72]. |
| **Estrutura** | [cite_start]Programação Orientada a Objetos (POO) [cite: 79] | [cite_start]Implementação da classe `Funcao` para modularizar as funções matemáticas[cite: 79]. |
| **Robustez** | Tratamento de Erros | [cite_start]Garantia de que a interface de menu lida com entradas inválidas (não numéricas)[cite: 350, 357]. |

## Estrutura do Repositório

O código está estruturado para separação de responsabilidades:

* [cite_start]**`funcoes.py`**: Contém a classe `Funcao` com as diversas funções analisadas (Logística, Reta, Raiz Quadrada, Cosseno, Expansora)[cite: 102, 110, 117, 126, 134].
* [cite_start]**`cobweb.py`**: Contém a lógica de cálculo dos iterados e a construção visual do Cobweb Plot e suas animações[cite: 81].
* [cite_start]**`main_menu.py`**: A interface principal do programa que interage com o usuário, compila e executa as funções dos módulos[cite: 83].

## Status do Projeto e Melhorias Futuras

[cite_start]O código está **funcionando como previsto** e de acordo com a teoria matemática[cite: 486].
Originalmente, o projeto foi desenvolvido na plataforma **Google Colab** e está em processo de adaptação e otimização para este repositório no GitHub.

**Este código ainda está sendo melhorado e otimizado.** Existem diversas melhorias planejadas para um funcionamento ainda melhor do código, incluindo:

1.  [cite_start]**Aprofundamento da Análise:** Inserir a análise detalhada de pontos periódicos e pontos fixos[cite: 494].
2.  [cite_start]**Expansão da Biblioteca:** Inserir outras diversas funções dentro da classe `Funcao`[cite: 495].
3.  [cite_start]**Melhoria Visual:** Aprimorar os gráficos e animações geradas[cite: 496].
4.  [cite_start]**Integração Acadêmica:** Inserção e expansão como parte do Trabalho de Conclusão de Curso (TCC)[cite: 496].

---

## 🏃 Como Executar

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

Sinta-se à vontade para enviar *pull requests* ou abrir *issues* com sugestões!
