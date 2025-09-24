## Questão 2 — Relatório de utilização (30 dias)

Eu faria o relatório por eventos assíncronos: 

* o /launch só enfileira um evento leve e retorna; uma pipeline/serviço, seja Direct Event Bus ou Outbox + Event Bus alimenta um Analytics DB. 

Assim o lançamento nunca bloqueia por causa do relatório, e ainda fica fácil observar e reprocessar. Para evitar duplicações, uso o trace_id como chave de idempotência no consumo (UPSERT).

#### Sobre Outbox: 
Na versão transacional (a recomendada), o /launch grava o lançamento e a linha na outbox na mesma transação, um Outbox Relay publica no bus e marca sent.
Isso elimina o “buraco” entre lançar e publicar e garante a entrega mesmo se o broker estiver fora na hora do request. 
Se não der para compartilhar a transação, dá para usar uma staging table: o relay lê de lá e publica no bus, garantindo at-least-once para tudo que entrou na staging. O trade-off é a janelinha entre o commit do launch e o insert na staging, se a app cair nesse intervalo, aquele evento pode não existir. 


Idempotência por trace_id (producer/consumer → UPSERT).