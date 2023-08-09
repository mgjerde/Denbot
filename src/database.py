import sqlite3


class Database:
    def __init__(self):
        self.__DB_LOCATION = "../data/denbot.sqlite"
        self.__connection = sqlite3.connect(self.__DB_LOCATION)
        self.cur = self.__connection.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS servers (guild_id NOT NULL PRIMARY KEY, ac_channel, streaming_role, lfg_role, auto_role);"
        )

    def __del__(self):
        self.__connection.close()

    def execute(self, new_data):
        result = self.cur.execute(new_data)
        return result.fetchone()

    def executemany(self, many_new_data):
        self.cur.executemany(many_new_data)

    def commit(self):
        self.__connection.commit()


def create_table():
    db = Database()
    db.execute(
        "CREATE TABLE IF NOT EXISTS servers (guild_id NOT NULL PRIMARY KEY, ac_channel, streaming_role, lfg_role, auto_role);"
    )


def add_guild(guild):
    db = Database()
    db.execute(f"INSERT OR IGNORE INTO servers (guild_id) VALUES ({guild});")
    db.commit()


def update_setting(guild_id, custom_id, value):
    db = Database()
    db.execute(
        f"UPDATE servers SET {custom_id} = {value} WHERE guild_id LIKE {guild_id};"
    )
    db.commit()


def get_setting(guild_id, setting_name):
    db = Database()
    return db.execute(
        f"SELECT {setting_name} FROM servers WHERE guild_id LIKE {guild_id};"
    )[0]


# Todo: Move over to aiosqlite
