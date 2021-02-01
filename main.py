import mysql.connector
# mydb = mysql.connector.connect(
#    host = "localhost",
#   user = "root",
#    passwd = ""
# )
# cursor = mydb.cursor()


class Drug:
    def __init__(self, id, name, conflicts):
        self.id = id
        self.name = name
        self.conflicts = conflicts


class Patient:
    def __init__(self, id, name, family, age, birthday, gender, insurance,\
                 ins_id, phone, history, province, city, address):
        self.id = id
        self.name = name
        self.family = family
        self.age = age
        self.birthday = birthday
        self.gender = gender
        self.insurance = insurance
        self.ins_id = ins_id
        self.phone = phone
        self.history = history
        self.province = province
        self.city = city
        self.address = address
