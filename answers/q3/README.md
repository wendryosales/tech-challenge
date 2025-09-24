## Questão 3 — Testes para agendador de eventos

Para cobrir o cenário acredito que deve-se testar primeiro unitariamente para garantir que o a lógica individual está correta e depois validar se as integrações estão funcionando entre si antes de testar carga. 

Para isso acho que cai bem testes unitários e de integração.

Nos testes unitários: Validar cada função isoladamente. 

Por exemplo:
- Testar a função que consulta o Redis por eventos agendados.
- Testar a função que remove o evento do Redis.

No teste de Integração: Simular o fluxo completo de uma única requisição.

* Enviar um evento para o endpoint /v1/render/scheduler.
* Verificar se o evento foi corretamente armazenado no Redis com o tempo agendado.
* Simular o processo que lê do Redis e verificar se o evento é publicado no Kafka no momento correto e removido do Redis.

Como fazer: Utilizaria frameworks como Pytest para os testes unitários e de integrações. Para simular o Redis e o Kafka sem depender dos serviços reais, usaria mocks e fixtures.


Só depois disso acredito que faça sentido ir para testes de carga/estresse e resiliência/caos. (Aqui podemos utilizar ferramentas próprias para isso, como o k6 ou Gatlin)

Esta é a etapa mais crítica para validar os requisitos de 1.000 RPS e 30ms de latência. 

### Ambiente

É importante que os testes sejam executados em um ambiente bem próximo ao real de produção com as mesmas configurações de serviços e hardware.


### Testes

* Teste de Carga: Injetar um tráfego de 1.000 RPS por um período estendido (ex: 15-30 minutos) e monitorar as métricas para garantir que o sistema se mantém estável.
* Teste de Estresse:  Aumentar a carga gradualmente (ex: de 1.000 para 1.500, 2.000 RPS) até que o sistema comece a gargalar (latência aumenta, erros). Isso vai ajudar a encontrar o limite até onde o serviço aguenta.

* Testes de Resiliência: Aqui iremos testar como o serviço se comporta em cenários de falha.
    - Falha do Redis: Simular a queda do Redis (parar o serviço Redis) e verificar se:
        - A API de agendamento continua funcionando (e falhando de forma controlada, talvez retornando um erro 500).
        - O processo de consulta de eventos agendados se recupera corretamente quando o Redis volta a operar.

    - Falha do Kafka: Simular a indisponibilidade do Kafka para o processo que publica eventos. 
        - Devemos validar se o processo de consulta do Redis não falha.
        - Ele tenta publicar novamente quando o Kafka volta.


### Métricas

As métricas que vamos olhar nos testes serão:

* Taxa de Requisições (RPS - Requests Per Second).
* Latência P50/P95/P99 da API: A latência média, o P90 e, principalmente, o P99. O P99 de 30ms significa que 99% das requisições devem ter uma latência menor ou igual a 30ms.
* Erro total.
* CPU, memória, uso de rede.
* Latência do Redis/Kafka
