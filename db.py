import psycopg2

conn = psycopg2.connect(
    host = "postgres_db",
    database = "f_db",
    user = "user",
    password = "pass"
)

curs = conn.cursor