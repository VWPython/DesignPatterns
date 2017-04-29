## Padrões de projeto - GoF
***

* ISSUES: state, interpreter, templateMethod

* Código de todos os padrões de projetos em python

* Dificilmente, uma empresa consegue sobreviver sem auxílio de ferramentas computacionais.

* Apesar de específicos, os sistemas corporativos possuem diversas características semelhantes.
Consequentemente, muitos problemas se repetem em contextos distintos.

* Suponha que um determinado problema ocorrerá em duzentos sistemas diferentes.

  - Em cada sistema, esse problema pode ser resolvido de uma forma distinta.

  - Então, globalmente, teríamos duzentas soluções para o mesmo problema.

  - Provavelmente, algumas soluções seriam melhores que outras ou até mesmo uma delas melhor do que todas as outras.

* Para não perder tempo e dinheiro elaborando soluções diferentes para o mesmo problema, poderíamos escolher uma solução como padrão e
adotá-la toda vez que o problema correspondente ocorrer.

* Além de evitar o retrabalho, facilitaríamos a comunicação dos desenvolvedores e o entendi- mento técnico do sistema.

* Daí surge o conceito de **padrão de projeto** ou **design pattern**.

* Um padrão de projeto é uma solução consolidada para um problema recorrente no desenvolvimento e manutenção de software orientado a objetos.

***
#### Classificação dos Padrões de Projeto GoF
***

* Os padrões são divididos em três categorias: de **Criação**, **Estrutural** e **Comportamental**.

* Todos os padrões destas categorias tem um conjunto de características específicas, que motivam a categorização deles.

* Antes de falar das categorias, é importante comentar que os padrões de objeto, além das categorias, podem ser classificados também em relação
ao seu escopo: de **Classe** ou de **Objetos**.

  - Padrões com escopo de **Classe** vão utilizar a herança para compor ou variar os objetos, mantendo a flexibilidade do sistema.

  - Já os padrões de **Objeto** irão delegar as suas responsabilidades para um objeto.

    ![padrões](https://cloud.githubusercontent.com/assets/14116020/25073183/6401a2e4-22b7-11e7-9ab7-fb2077ab2b4a.png)

***
#### Padrões de Criação
***

* **Factory Method**:

  - Encapsular a escolha da classe concreta a ser utilizada na criação de objetos de um determinado tipo.

  - Criando objetos com alta flexibilidade!

* **Abstract Factory**:

  - Encapsular a escolha das classes concretas a serem utilizadas na criação dos objetos de diversas famílias.

  - Criando famílias de objetos com alta flexibilidade!

* **Builder**:

  - Separar o processo de construção de um objeto de sua representação e permitir a sua criação passo-a-passo.

  - Diferentes tipos de objetos podem ser criados com implementações distintas de cada passo.

  - Construindo o produto passo-a-passo!

* **Prototype**:

  - Possibilitar a criação de novos objetos a partir da cópia de objetos existentes.

  - Criando objetos por cópia de uma instância!

* **Singleton**:

  - Permitir a criação de uma única instância de uma classe e fornecer um modo para recuperá-la.

  - Centralizando e compartilhando recursos!


***
#### Padrões Estruturais
***


* **Adapter**: Permitir que um objeto seja substituído por outro que, apesar de realizar a mesma tarefa, possui uma interface diferente.

* **Bridge**: Separar uma abstração de sua representação, de forma que ambos possam variar e produzir tipos de objetos diferentes.

* **Composite**: Agrupar objetos que fazem parte de uma relação parte-todo de forma a tratá-los sem distinção.

* **Decorator**: Adicionar funcionalidade a um objeto dinamicamente.

* **Facade**: Prover uma interface simplificada para a utilização de várias interfaces de um subsistema.

* **Flyweight**: Compartilhar, de forma eficiente, objetos que são usados em grande quantidade.

* **Proxy**: Controlar as chamadas a um objeto através de outro objeto de mesma interface.

***
#### Padrões Comportamentais
***

* **Command**: Controlar as chamadas a um determinado componente, modelando cada requisição como um objeto.
  Permitir que as operações possam ser desfeitas, enfileiradas ou registradas.

* **Iterator**: Fornecer um modo eficiente para percorrer sequencialmente os elementos de uma coleção, sem que a estrutura interna
  da coleção seja exposta.

* **Observer**: Definir um mecanismo eficiente para reagir às alterações realizadas em determinados objetos.

* **State**: Alterar o comportamento de um determinado objeto de acordo com o estado no qual ele se encontra.

* **Strategy**: Permitir de maneira simples a variação dos algoritmos utilizados na resolução de um determinado problema.

* **Template Method**: Definir a ordem na qual determinados passos devem ser realizados na resolução de um problema e permitir que esses
  passos possam ser realizados de formas diferentes de acordo com a situação.

* **Visitor**: Permitir atualizações específicas em uma coleção de objetos de acordo com o tipo particular de cada objeto atualizado.
