db = {
    'user': 'root',
    'password': 'rlatnsxo12!@',
    'host': '0.0.0.0',
    'port': '8080',
    'database': 'board_test'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
