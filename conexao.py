import mysql.connector as bd
import config


def conectar(nome_banco):
    con = bd.connect(
        user=config.USUARIO,
        password=config.SENHA,
        host=config.HOST,
        port=config.PORTA,
        database=nome_banco
    )
    return con
