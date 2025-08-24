import pymysql

db = pymysql.connect(host='localhost',user='root',passwd='12345')
cursor = db.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS quiz')
cursor.execute('USE quiz')
cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions(
        qno INT(5) PRIMARY KEY AUTO_INCREMENT, 
        question VARCHAR(100), 
        a VARCHAR(50), 
        b VARCHAR(50), 
        c VARCHAR(50), 
        d VARCHAR(50), 
        correct VARCHAR(50)
    )
""")
db.commit()

def insert():
	f_name = input("Enter file name.extension	:")
	fp = open(f_name, "r")
	for line in fp.readlines():
		line = line.split(",")
		cursor.execute("INSERT INTO questions (qno, question, a, b, c, d, correct) VALUES (%s, %s, %s, %s, %s, %s, %s)",(line[0], line[1], line[2], line[3], line[4], line[5], line[6]))
		db.commit()
		print("Data inserted successfully")

def view_question():
	print("{:<5}{:<60}".format("qno","Question"))
	cursor.execute("SELECT * FROM questions")
	queston = cursor.fetchall()
	for i in queston:
		print("{:<5}{:<60}".format(i[0],i[1]))
	return

def delete_question():
	while True:
		choice = int(input("""
1.	Remove all questions.
2.	Remove selectd question.
3.	Exit
Enter a number	:
"""))
		if choice==1:
			cursor.execute("DELETE FROM questions")
			db.commit()
			print("All questions deleted")
		elif choice==2:
			sno = int(input("Enter question number	:"))
			cursor.execute("DELETE FROM questions WHERE qno = %s",(sno))
			print(f"{sno} is Deleted")
			db.commit()
			choice = input("Do you want to delete more(y/n)    :")
			if choice.lower() == "n":
				break
		elif choice == 3:
			return
		else:
			print("Invalid choice")

def add_question():
	while True:
		sno = int(input("Enter question number	:"))
		question = (input("Enter question	:"))
		a = (input("Enter option a	:"))
		b = (input("Enter option b	:"))
		c = (input("Enter option c	:"))
		d = (input("Enter option d	:"))
		correct = (input("Enter correct option	:"))
		cursor.execute("INSERT INTO questions (qno, question, a, b, c, d, correct) VALUES (%s, %s, %s, %s, %s, %s, %s)",( sno, question, a, b, c, d, correct))
		print("This question is add in Database")
		db.commit()
		choice = input("Do you want to add more(y/n)    :")
		if choice.lower() == "n":
			break

def quiz_manage():
		while True:
			print("*" * 40)
			print(f"{'QUIZ MANAGEMENT':^40}")  
			print("*" * 40)
			choice = int(input("""
1.	ADD QUESTION
2.	DELETE QUESTION
3.	VIEW QUESTION
4.  INSERT QUESTIONS FROM CSV FILE
5.	Exit
ENTER YOUR CHOICE	:"""))

			if choice == 1:
				add_question()
			elif choice == 2:
				delete_question()
			elif choice	== 3:
				view_question()
			elif choice == 4:
				insert()
			elif choice == 5:
				return
			else:
				print("invelid choice")
