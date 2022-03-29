from urllib.parse import urlparse

import psycopg2


def connect_postgresql_db(jdbc_url: str, password: str):
    result = urlparse(jdbc_url)
    username = result.username
    database = result.path[1:]
    hostname = result.hostname
    port = result.port

    connection = psycopg2.connect(user=username,
                                  password=password,
                                  host=hostname,
                                  port=port,
                                  database=database,
                                  connect_timeout=10)

    return connection
