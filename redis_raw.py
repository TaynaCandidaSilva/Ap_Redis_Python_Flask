import redis

redis_conn = redis.Redis(host="localhost", port=6379, db=0)


# Para Insert e Update no banco
redis_conn.set("chave_1", "trocando_o_meu_valor")

# Para Select no banco
meu_valor = redis_conn.get("chave_1").decode("utf-8")

# Para Delete no banco
redis_conn.delete("chave_1")

print(meu_valor)
print(type(meu_valor))
