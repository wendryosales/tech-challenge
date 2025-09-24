## Questão 7 — Design Patterns para normalização de serviços de terceiros


Acredito que o pattern que mais faça sentido seria o Adapter.

Como podemos ver no próprio [refatoring.guru](https://refactoring.guru/pt-br/design-patterns/adapter), "O Adapter é um padrão de projeto estrutural que permite objetos com interfaces incompatíveis colaborarem entre si."

A essência do problema que foi descrito é a incompatibilidade, onde cada serviço de e-mail ou SMS tem sua própria API, com nomes de métodos diferentes, estruturas de dados diferentes, autenticação, etc. A lógica do sistema não precisa se preocupar com isso.

* No Adapter nós criaríamos uma interface comum, por exemplo: `MessageSender`, com métodos genéricos `send_email`, `send_sms`. Ela seria o contrato que a lógica do negócio conhece.

* Aí devemos criar classes de adapters para cada serviço/provider.  Essas classes devem implementar a interface que foi criada `MessageSender` e internamente traduzir as chamadas para as chamadas especificas de cada serviço/api.


Dessa forma nós temos:

* Desacoplamento, pois a lógica do negócio fica isolada da implementação dos serviços de terceiros.
* Flexibilidade, pois é possível adicionar um novo provedor ou mudar algum existente de forma simples, basta criar um novo Adapter implementando a interface em comum.
* Reusabilidade, pois pode ser utilizado em qualquer lugar necessário.
* Manutenibilidade, pois a complexidade de lidar com as particularidades de cada API de terceiro é encapsulada em seus respectivos adaptadores.