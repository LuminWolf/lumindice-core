import sqlite3
import toml

config = toml.load("config.toml")
db_folder = config['database']['folder_path']


if __name__ == '__main__':
    db_path = f'{db_folder}/class.sqlite3'

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # sql = "CREATE TABLE 职业特性(职业名, 特性名)"
    # cur.execute(sql)

    cur.close()
    conn.close()
