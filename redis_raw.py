import redis

redis_conn = redis.Redis(host="localhost", port=6379, db=0)


# Para Insert e Update no banco
redis_conn.set("chave_1", "trocando_o_meu_valor")

# Para Select no banco
meu_valor = redis_conn.get("chave_1").decode("utf-8")

# Para Delete no banco
redis_conn.delete("chave_1")

# Comandos para hash

meu_hash = {  # chave de exemplo
    "nome": "joao",  # field: values
    "idade": 30,
    "cidade": "sao paulo",
}
# O HSET serve para Insert e Update

redis_conn.hset("meu_hash", "nome", "joao")
redis_conn.hset("meu_hash", "idade", 30)
redis_conn.hset("meu_hash", "cidade", "sao paulo")

valor1 = redis_conn.hget("meu_hash", "nome").decode("utf-8")

redis_conn.hdel("meu_hash", "cidade")

## Busca por existencia
elem = redis_conn.exists("chave_1")
print(elem)

elem2 = redis_conn.hexists("meu_hash", "nome")
print(elem2)
