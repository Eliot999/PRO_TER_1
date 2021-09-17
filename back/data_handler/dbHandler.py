import psycopg2

class Logger(object):
    def __init__(self) -> None:
        self.con = psycopg2.connect(
            dbname='',
            host='',
            user='',
            password='',
            port=''
        )
        self.cur = self.con.cursor()