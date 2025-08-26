import clickhouse_connect
import random

client = clickhouse_connect.get_client(
    host='localhost', port=8123, username='root', password='root', database='test_db'
)

client.command("""
CREATE TABLE IF NOT EXISTS test_db.test
(
  id UInt32,
  volt_value Float32
)
ENGINE = MergeTree
ORDER BY id
""")

# батч
#client.insert('test_db.test', [(3, 220.5), (4, 221.0)], column_names=['id', 'volt_value'])

# проверка
#print(client.query('SELECT * FROM test_db.test ORDER BY id').result_rows)

# генерация данных
rows = []
for i in range(1, 16):  # id от 1 до 15
    value = random.uniform(100, 120)  # диапазон [100;120]
    rows.append((i, value))

# вставка пачкой
client.insert('test_db.test', rows, column_names=['id', 'volt_value'])

# проверка
print("Inserted rows:")
for row in client.query("SELECT * FROM test_db.test ORDER BY id").result_rows:
    print(row)