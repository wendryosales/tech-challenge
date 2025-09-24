## Questão 1 — Validação de cadastro por CNPJ e CEP

Informação relevante: 

Como o Strategy decide (CEP Resolver)

- Tenta A por padrão.
- Failover para B se em A ocorrer: timeout, 5xx/erro de rede ou Circuit Breaker (CB) open.
- Não faz failover em 4xx semântico (ex.: CEP inválido) — propaga para 400.
- Se B também falhar → 502.