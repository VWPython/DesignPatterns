## Padrões de projeto - GoF
***
## Princípios  e Conceitos de padrões de projeto GoF
***

Cada padrão descreve um problema que ocorre repetidamente em nosso ambiente e, em seguida, descreve o núcleo da solução para esse problema, de tal forma que você pode usar esta solução um milhão de vezes, sem nunca fazê-lo da mesma maneira duas vezes .

***
### 1. Princípios
***

#### 1.1 Princípio do aberto/fechado

* Determina que classes ou objetos e métodos devem estar abertos para extensão e fechados para modificação


* Ao construir aplicações você deve garantir que escreverá suas classes ou seus módulos de forma genêrica de modo que sempre que sentir a necessidade de extender o comportamento da classe ou do objeto, você não precisará alterar a classe propriamente dita, ao inves disso, você faz uma extensão simples da classe que deve ajudar a implementar um novo comportamento.


* Ou seja, se quiser implementar algum comportamento, você extende da classe abstrata ao inves de alterar a classe abstrata.


* Ajuda a manter a compatibilidade com versões de códigos anteriores e as classes existentes não são alteradas

#### 1.2 Princípio da inversão de controle

* Determina que módulos de alto nível não devem ser dependentes de módulos de baixo nível.


* Ambos devem ser dependentes de abstrações/templates e não o inverso.


* Dois módulos não devem ser altamente dependentes um do outro.


* **Alto acoplamento** deixa de ser predominante eliminando dependências, ou seja, ela fica **bem coesa**, com responsabilidades bem definidas.

#### 1.3 Princípio da segregação de interfaces

* Os clientes não devem ser forçados a depender de interfaces que não utilizam.


* Devemos desenvolver métodos relacionados as funcionalidades, sem que o cliente tenha que implementar métodos que não irá utilizar

#### 1.4 Princípio da responsabilidade única

* Um classe deve ter apenas um mótivo para existir, ou seja, cada classe deve ter sua responsabilidade bem definida e única


* Uma classe não devem fazer coisas que cabe a outra classe fazer.


* Fazer a classe ter **alta coesão**

#### 1.5 Princípio da substituição

* Classes derivadas devem ser capazes de substituir totalmente as classes bases


* A classe devirada deve estar o mais parecido possível com a classe base de modo que a classe derivada possa substituir a classe base se for o caso.

***
#### 2. Classificação dos Padrões de Projeto
***

Padrões de projetos são técnicas, independentes de linguagem de programação, para solucionar problemas conhecidos utilizando os princípios acima e tornando o software reutilizavem e modularizado.

Um padrão de projeto é uma solução consolidada para um problema recorrente no desenvolvimento e manutenção de software orientado a objetos.

Os padrões são divididos em três categorias: de **Criação**, **Estrutural** e **Comportamental**.


* Todos os padrões destas categorias tem um conjunto de características específicas, que motivam a categorização deles.


* Antes de falar das categorias, é importante comentar que os padrões de objeto, além das categorias, podem ser classificados também em relação ao seu escopo: de **Classe** ou de **Objetos**.

    - Padrões com escopo de Classe vão utilizar a herança para compor ou variar os objetos, mantendo
    a flexibilidade do sistema.

    - Já os padrões de Objeto irão delegar as suas responsabilidades para um objeto.
    
![image](https://user-images.githubusercontent.com/14116020/34313218-bc6bfcbe-e750-11e7-9b2e-289f41e05316.png)

***
### 3. Padrões Criacionais
***

Os padrões de criação tem como intenção principal abstrair o processo de criação de objetos, ou seja, a sua instanciação.

* Desta maneira o sistema não precisa se preocupar com questões sobre, como o objeto é criado, como é composto, qual a sua representação real.


* Quando se diz que o sistema não precisa se preocupar com a instanciação do objeto quer dizer que, se ocorrer alguma mudança neste ponto, o sistema em geral não será afetado.


* Isso é a famosa flexibilidade que os padrões de projeto buscam.

Padrões de criação com escopo de classe vão utilizar herança para garantir suaflexibilidade.

* Por exemplo, o padrão Factory Method pode criar várias subclasses para criar o produto.


* Já os padrões com escopo de Objeto, como o Prototype, delegam para um objeto (no caso o protótipo) a responsabilidade de instanciar novos objetos.

#### 3.1 Problema

* Em um sistema orientado a objetos, a criação de certos objetos pode ser uma tarefa extremamente complexa.


* Podemos destacar dois problemas relacionados a criação de objetos: definir qual classe concreta deve ser utilizada para criar o objeto e definir como os objetos devem ser criados e como eles se relacionam com outros objetos do sistema.


* Seguindo o princípio do encapsulamento, essa complexidade deve ser isolada.

#### 3.2 Padrão Factory Method

* Encapsular a escolha da classe concreta a ser utilizada na criação de objetos de um determinado tipo.


* Usamos uma fábrica quando temos que isolar o processo de criação de um objeto em um único lugar.


* Essa fábrica pode descobrir como criar o objeto dentro dela própria, mas geralmente ela não precisa de muitas informações para criar o objeto.

#### 3.3 Padrão Abstract Factory

* Encapsular a escolha das classes concretas a serem utilizadas na criação dos objetos de diversas famílias.


* Criando famílias de objetos com alta flexibilidade!

#### 3.4 Padrão Builder

* Separar o processo de construção de um objeto de sua representação e permitir a sua criação passo-a-passo.


* Geralmente usamos um builder quando precisamos passar diversas informações para a lógica que monta o objeto.


* Usa sempre que tivermos um objeto complexo de ser criado, que possui diversos atributos, ou que possui uma lógica de criação complicada, podemos esconder tudo isso em um Builder.


* Construindo o produto passo-a-passo!

#### 3.5 Padrão Prototype

* Possibilitar a criação de novos objetos a partir da cópia de objetos existentes.


* Por exemplo através de um objeto palio podemos ter palio usado, palio novo, palio weekend


* Criando objetos por cópia de uma instância!

#### 3.6 Padrão Singleton

* Permitir a criação de uma única instância de uma classe e fornecer um modo para recuperá-la.


* O Singleton nos ajuda a ter uma única instância do objeto ao longo do sistema.


* Centralizando e compartilhando recursos!

#### 3.7 Padrão Multiton

* Bem parecido com o Singleton

* Permitir a criação de uma quantidade limitada de instâncias de determinada classe e fornecer um modo para recuperá-las.

#### 3.8 Padrão Object Pool

* Possibilita o reaproveitamento de objetos

* Uma situação típica em que recursos limitados devem ser reutilizados é o do restaurante. O restaurante não adquire novas mesas a medida que clientes chegam ao restaurante e as mesas são reutilizadas por novos clientes assim que são liberadas.

***
### 4. Padrões Estruturais
***

* Os padrões estruturais vão se preocupar em como as classes e objetos são compostos, ou seja, como é a sua estrutura.

* O objetivo destes padrões e facilitar o design do sistema identificando maneiras de realizar o relacionamento entre as entidades, deixando o desenvolvedor livre desta preocupação.

* Os padrões com escopo de classe utilizam a herança para compor implementações ou interfaces.

* O padrão Adapter, por exemplo, pode definir uma nova interface para adaptar duas outras já existentes, assim uma nova classe é criada para adaptar uma interface a outra.

* Os padrões com escopo de objeto utilizam a composição de objetos para definir uma estrutura.

* Por exemplo, o padrão Composite define (explicitamente) uma estrutura de hierárquica para classes primitivas e compostas em um objeto.

#### 4.1 Problema

* As interações entre os objetos de um sistema podem gerar fortes dependências entre esses elementos.

* Essas dependências aumentam a complexidade das eventuais alterações no funcionamento do sistema.

* Consequentemente, o custo de manutenção aumenta.

* Mostraremos alguns padrões de projeto que diminuem o acoplamento entre os objetos de um sistema orientado a objetos.

#### 4.2 Padrão Adapter:

* Permitir que um objeto seja substituído por outro que, apesar de realizar a mesma tarefa, possui uma interface diferente.

* A ideia do Adapter é esconder alguma "sujeira", ou adaptar algo que é diferente e não bate com o sistema atual.

* É bem comum inclusive que a interface do Adapter já tenha sido pré-definida e já até exista no sistema.

* Ele visa adaptar um conjunto de classes que já existem, para uma outra interface, que é a requerida pelo outro sistema.

#### 4.3 Padrão Bridge:

* Separar uma abstração de sua representação, de forma que ambos possam variar e produzir tipos de objetos diferentes.

* A ideia da Bridge é justamente ser uma ponte em dois mundos/sistemas.

#### 4.4 Padrão Composite:

* Agrupar objetos que fazem parte de uma relação parte-todo de forma a tratá-los sem distinção.

* Um bom exemplo é a estrutura de pastas que forma uma arvore, na qual uma pasta tem vários arquivos porem arquivos não pode ter outros arquivos

#### 4.5 Padrão Decorator:

* Adicionar funcionalidade a um objeto dinamicamente.

* Sempre que percebemos que temos comportamentos que podem ser compostos por comportamentos de outras classes envolvidas em uma mesma hierarquia, por exemplo o caso dos impostos, que podem ser composto por outros impostos.

#### 4.6 Padrão Facade:

* Prover uma interface simplificada para a utilização de várias interfaces de um subsistema.

* O Façade cria uma interface amigável para que clientes consigam consumir sub-sistemas (ou serviços).

#### 4.7 Padrão Flyweight:

* Compartilhar, de forma eficiente, objetos que são usados em grande quantidade.

* Um Flyweight serve para quando temos muitas instâncias do mesmo objeto andando pelo sistema, e precisamos economizar.

* Para tal, o Flyweight faz uso de uma fábrica modificada, que guarda essas instâncias.

* A diferença entre o singleton e o Flyweight é que o Flyweight garante que existam apenas uma única instância de vários elementos. É um "singleton maior".

* Aplicações gráficas geralmente fazem uso desse padrão, já que elas tem muito objeto repetido.

#### 4.8 Padrão Proxy:

* Controlar as chamadas a um objeto através de outro objeto de mesma interface.

* Normalmente usada para proteger e esconder um objeto especifico utilizando um proxy para acessa-lo

***
### 5. Padrões Comportamentais
***

* Os padrões comportamentais atuam sobre como responsabilidades são atribuídas as entidades, ou seja, qual o comportamento das entidades.

* Estes padrões facilitam a comunicação entre os objetos, distribuindo as responsabilidades e definindo a comunicação interna.

* Padrões com escopo de classe utilizam herança para realizar a distribuição do comportamento.

* Um bom exemplo é o padrão Template Method, que fornece um algoritmo (comportamento) padrão e deixa as subclasses definirem alguns pontos da execução do algoritmo.

* Já os padrões de objetos vão compor os objetos para definir a comunicação, como o padrão Mediator, que define um objeto que realiza a comunicação muitos-para-muitos.

#### Padrões 5.1

* **Command**: Controlar as chamadas a um determinado componente, modelando cada requisição como um objeto. Permitir que as operações possam ser desfeitas, enfileiradas ou registradas.

* **Iterator**: Fornecer um modo eficiente para percorrer sequencialmente os elementos de uma coleção, sem que a estrutura interna da coleção seja exposta.

* **Observer**: Definir um mecanismo eficiente para reagir às alterações realizadas em determinados objetos.

* **State**: Alterar o comportamento de um determinado objeto de acordo com o estado no qual ele se encontra.

* **Strategy**: Permitir de maneira simples a variação dos algoritmos utilizados na resolução de um determinado problema.

* **Template Method**: Definir a ordem na qual determinados passos devem ser realizados na resolução de um problema e permitir que esses passos possam ser realizados de formas diferentes de acordo com a situação.

* **Visitor**: Permitir atualizações específicas em uma coleção de objetos de acordo com o tipo particular de cada objeto atualizado.

* **Mediator**: Quando uma situação em que um relacionamento muitos para muitos é necessário, uma boa prática é criar uma tabela intermediária e deixar que ela relaciona uma entidade com outras várias e vice versa.

* **Memento**: Sem violar o encapsulamento, capturar e externalizar um estado interno de um objeto, de maneira que o objeto possa ser restaurado para esse estado mais tarde.

* **Chain of responsability**: Usado para acabar com estruturas de decisão, evitando o acoplamento utilizando uma cadeia de solicitações até que uma trate

* **Interpreter**: Reconhecer padrões é um problema bem complicado, no entanto, quando conseguimos formular uma gramática para o problema a solução fica bem mais fácil. Uma vez definida a grámatica e suas regras, é possível utilizar o padrão Interpreter para montar uma estrutura para interpretar os comandos.
