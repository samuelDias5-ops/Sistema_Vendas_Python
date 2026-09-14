import mysql.connector

print("A")

conexao = mysql.connector.connect(
    host = "127.0.0.1",
    port=3306,
    user = "root",
    password = "Animes@123",
    connection_timeout=5,
    use_pure=True
)
cursor = conexao.cursor()
cursor.execute("SHOW DATABASES")

for banco in cursor:
    print(banco)
cursor.close()
conexao.close()
