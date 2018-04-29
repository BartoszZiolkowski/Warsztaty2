
config_path = "db_cinema.json"
def connection(config_file):
    cfg_string = open(config_file).read()
    cfg_json = json.loads(cfg_string)
    return connect(user=cfg_json["username"],
                   password=cfg_json["passwd"],
                   host=cfg_json["hostname"],
                   database=cfg_json["db_name"])


def db_execute(cursor, sql):
    try:
        cursor.execute(sql)
    except Exception as e:
        print("Niepowodzenie:", e)


def db_unisolated_execute(cursor, sql):
    try:
        cnx.set_isolation_level(0)
        cursor.execute(sql)
        cnx.set_isolation_level(1)
    except Exception as e:
        print("Niepowodzenie:", e)

try:
    cnx = connection(config_path)
    print("Polaczono z baza ")
except Exception as e:
    print("Niepowodzenie:", e)
    exit()

cursor = cnx.cursor()