## Questão 4 — Revisão de anti-patterns

`back_end/waimea/anti_patterns/src/middlewares/exception_handler.py`

* Está vazando a stacktrace e a mensagem de erro toda para o cliente. Risco de segurança.
* Retorna string em vez de objeto JSON, o que não é um problema mas dificulta quem vai consumir

`back_end/waimea/anti_patterns/src/app.py`

* Liberação de CORS para tudo.
* Somente o módulo de health está configurado, o registration não.

`back_end/waimea/anti_patterns/src/middlewares/tools.py`

* Mistura de responsabilidades (infra + HTTP + validações) herdando de repositório.
* Muito acoplamento, viola SRP e dificulta testes.
* SQL-injection com f-string em várias queries. O correto seria utilizar as queries com parâmetros, algo assim: 

```python
    row = await session.execute(text(
        "SELECT access_key FROM secrets WHERE id = :id LIMIT 1"
    ), {"id": id})
```
* Algumas chamadas de promises estão sem `await`.
* Me parece que o método `send_instant_message` está retornando um atributo ao invés de chamar o método `.json()`

`back_end/waimea/anti_patterns/src/endpoints/registration/manager.py`

* Camada extra sem valor (não orquestra nada).

`back_end/waimea/anti_patterns/src/infrastructure/repositories/sql_repository.py`

* Método `filter_all_by`faltou retornar a lista de itens com o `.all()` igual o método `get_all`


`back_end/waimea/anti_patterns/src/endpoints/registration/repository.py`

* selectinload só funciona em relacionamentos, não em colunas. Provavalmente isso deve estourar um erro.
* Import do Base está incorreto.

`back_end/waimea/anti_patterns/src/endpoints/registration/controllers.py`

* leitura de um path param `customer_id` que não está definido na rota.

`back_end/waimea/anti_patterns/src/config.py`

* limites de paginação estão bem altos, vale uma atenção nisso. 