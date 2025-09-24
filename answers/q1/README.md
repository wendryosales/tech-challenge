## Questão 1 — Validação de cadastro por CNPJ e CEP

Informação relevante: 

Como o Strategy decide (CEP Resolver)

- Tenta A por padrão.
- Failover para B se em A ocorrer: timeout, 5xx/erro de rede ou Circuit Breaker (CB) open.
- Não faz failover em 4xx semântico (ex.: CEP inválido) — propaga para 400.
- Se B também falhar → 502.


#### Cache de CNPJ/CEP (opcional): 
- Deixei como opção porque os dados são quase estáticos e o gargalo está nas APIs externas. 
- Em cenários de repetição (reenvios, integrações, lotes), o cache reduz latência e ajuda em caso de instabilidade dos provedores. 
- Se a aplicação já usar Redis, o trade-off é mínimo.