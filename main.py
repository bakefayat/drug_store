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
    def __init__(self, pa_id, name, family, age, birthday, gender, insurance,\
                 ins_id, phone, history, province, city, address):
        self.pa_id = pa_id
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


class Doctor:
    def __init__(self, doc_id, name, family, position, start_date, degree, medical_id):
        self.doc_id = doc_id
        self.name = name
        self.family = family
        self.position = position
        self.start_date = start_date
        self.degree = degree
        self.medical_id = medical_id


class Prescription:
    def __init__(self, pre_id, pa_id, doc_id, export_date, deliver_date):
        self.pre_id = pre_id
        self.pa_id = pa_id
        self.doc_id = doc_id
        self.export_date = export_date
        self.deliver_date = deliver_date
