import mysql.connector
class drug:
    def __init__(self, id, name, conflicts):
        self.id = id
        self.name = name
        self.conflicts = conflicts


class patient:
    def __init__(self, name, family, gender, address, history):
        self.name = name
        self.family = family
        self.gender = gender
        self.address = address
        self.history = history
#mydb = mysql.connector.connect(
#    host = "localhost",
#   user = "root",
#    passwd = ""
#)
#cursor = mydb.cursor()
p1 = patient('ehsan','bakefayat','male', 'iran', 'heart diesase')
print(p1.name)