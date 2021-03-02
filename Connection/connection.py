import psycopg2
from Connection.con_parameters import Con_parameters
class Connection:
    def __init__(self):
        self.con=None
    def __enter__(self):
        self.con=psycopg2.connect(database=Con_parameters.DATABASE, user=Con_parameters.USER, password=Con_parameters.PASSWORD, port=Con_parameters.PORT)
        return self.con
    def __exit__(self,exc_type, exc_value,exc_tb):
        if exc_type or exc_value or exc_tb: #catching possible errors to close without commiting
            self.con.close()
        else:
            self.con.commit()
            self.con.close()
