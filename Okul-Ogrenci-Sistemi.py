import sqlite3
class university:
    def __init__(self,name,country):
        self.name= name
        self.country= country
        self.status= True
        self.connect_db()
    def run(self):
        self.menu()
        choice= self.choice()
        if choice==1:
            self.add_student()
        if choice==2:
            self.delete_student()
        if choice==3:
            self.update_student()
        if choice==4:
            while True:
                try:
                    orderby= int(input("List by 1- Show All Students 2- Faculty 3- Department 4- Type 5-Status: "))

                    if orderby<1 or orderby>5:
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number between 1 and 5.")
            
            self.list_students()
        if choice==5:
            self.system_exit()
    def menu(self):
        print("******** {} Administration System ********".format(self.name))
        print("1- Add Student")
        print("2- Delete Students")
        print("3- Update Student")
        print("4- List Students")
        print("5- Exit")
    
    def choice(self):
        while True:
            try:
                process= int(input("Choose your operation: "))
                if process<1 or process>5:
                    print("Please enter a valid number between 1 and 5")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")    
        return process
    def add_student(self):
        print("***Student İnformation Addition Screen***")
        name= input("Enter Student Name: ").lower().capitalize()
        surname= input("Enter Student Surname: ").lower().capitalize()
        faculty= input("Enter Student Faculty: ").lower().capitalize()
        department= input("Enter Student Department: ").lower().capitalize()
        stid= input("Enter Student ID: ")
        while True:
            try:
                typ= int(input("Enter Student Type (1-Undergraduate, 2-Graduate): "))
                if typ<1 or typ>2:
                    print("Please enter a valid number (1 or 2).")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        status= "Active"
        self.cursor.execute("INSERT INTO students Values('{}','{}','{}','{}','{}',{},'{}') ".format(name,surname,faculty,department,stid,typ,status))
        self.connect.commit()
        print("Student {} {} has been added to the system.".format(name,surname))
    def delete_student(self):
        self.cursor.execute("SELECT * FROM students")
        allstudents= self.cursor.fetchall()
        convertallstring= lambda x: [str(y) for y in x]
        
        for i,j in enumerate(allstudents,1):
            print("{}) {} ".format(i,"".join(convertallstring(j))))
        while True:
            try:
                select= int(input("Select the student to delete (by number): "))
                break
            except ValueError:
                print("Please enter a valid number.")
        self.cursor.execute("DELETE FROM students WHERE rowid={}".format(select))
        self.connect.commit()    
        print("The selected student has been deleted from the system.")

    def update_student(self):
        self.cursor.execute("SELECT * FROM students")
        allstudents= self.cursor.fetchall()
        convertallstring= lambda x: [str(y) for y in x]
        
        for i,j in enumerate(allstudents,1):
            print("{}) {} ".format(i,"".join(convertallstring(j))))
        while True:
            try:
                select= int(input("Select the student to update (by number): "))
                break
            except ValueError:
                print("Please enter a valid number.")
        while True:
            try:
                updateSelect= int(input(" Select Your  1-) Update Name 2-) Update Surname 3-) Update Faculty 4-) Update Department 5-) Update Student ID 6-) Update Education Type 7-) Update Status"))
                if updateSelect<1 or updateSelect>7:
                    print("Please enter a valid number between 1 and 7.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        operation = ["name","surname","faculty","department","stid","typ","status"]
        if updateSelect == 6:
            while True:
                try:
                    newvalue= int(input("Enter the new value (1-Undergraduate, 2-Graduate): "))
                    if newvalue not in [1,2]:
                        print("Please enter a valid number (1 or 2).")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")
            self.cursor.execute("UPDATE students SET typ={} WHERE rowid={}".format(newvalue,select))
        else:
            newvalue= input("Enter the new value: ").lower().capitalize()
            self.cursor.execute("UPDATE students SET {}='{}' WHERE rowid={}".format(operation[updateSelect-1],newvalue,select))           
        self.connect.commit()
                
    def list_students(self,by):
        if by==1:
                    self.cursor.execute("SELECT * FROM students")
        allfaculties= self.cursor.fetchall()
        convertallstring= lambda x: [str(y) for y in x]
        
        for i,j in enumerate(allfaculties,1):
            print("{}) {} ".format(i,"".join(convertallstring(j))))
        if by==2:
            self.cursor.execute("SELECT faculty From students")
            allfaculties=enumerate(list(set(self.cursor.fetchall())))
            for i,j in allfaculties:
                print("{}){}".format(i,j[0]))
            while True:
                try:
                    selectfaculty= input("Select Faculty: ").lower().capitalize()
                    break
                except ValueError:
                    print("Please enter a valid faculty name.")
            self.cursor.execute("SELECT * FROM students WHERE faculty='{}'".format(allfaculties[selectfaculty-1][1][0]))
        if by==3:
            self.cursor.execute("SELECT department From students")
            alldepartment=enumerate(list(set(self.cursor.fetchall())))
            for i,j in alldepartment:
                print("{}){}".format(i,j[0]))
            while True:
                try:
                    selectdepartment= input("Select Department: ").lower().capitalize()
                    break
                except ValueError:
                    print("Please enter a valid department name.")
            self.cursor.execute("SELECT * FROM students WHERE department='{}'".format(alldepartment[selectdepartment-1][1][0]))
        if by==4:
            
            self.cursor.execute("SELECT typ From students")
            alltyp=enumerate(list(set(self.cursor.fetchall())))
            for i,j in alltyp:
                print("{}){}".format(i,j[0]))
            while True:
                try:
                    selecttyp= input("Select Type: ").lower().capitalize()
                    break
                except ValueError:
                    print("Please enter a valid type.")
            self.cursor.execute("SELECT * FROM students WHERE typ='{}'".format(alltyp[selecttyp-1][1][0]))
        if by==5:
            self.cursor.execute("SELECT status From students")
            allstatus=enumerate(list(set(self.cursor.fetchall())))
            for i,j in allstatus:
                print("{}){}".format(i,j[0]))
            while True:
                try:
                    selectstatus= input("Select status: ").lower().capitalize()
                    break
                except ValueError:
                    print("Please enter a valid status.")
            self.cursor.execute("SELECT * FROM students WHERE status={}".format(allstatus[selectstatus-1][1][0]))

    def system_exit(self):
        self.status= False

    def connect_db(self):
        self.connect= sqlite3.connect("odtu.db")
        self.cursor= self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, surname TEXT, faculty TEXT, department TEXT, stid TEXT,typ INT,status Text)")

ODTU = university("Orta Dogu Teknik Universitesi","Turkiye")

while ODTU.status:
    ODTU.run()