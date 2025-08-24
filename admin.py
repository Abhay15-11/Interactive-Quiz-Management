import pymysql


db = pymysql.connect(host='localhost',user='root',passwd='12345')
cursor = db.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS quiz')
cursor.execute('USE quiz')
cursor.execute("CREATE TABLE IF NOT EXISTS login( username VARCHAR(10), password VARCHAR(10), role VARCHAR(7), status VARCHAR(10))")

def create_user():
	user = input("Enter user name	:")
	password = input("Enter user password	:")
	role = input("Enter your role(admin or player)	:")
	status = "active"
	cursor.execute("SELECT * FROM login WHERE username = %s AND password = %s AND role = %s",(user, password, role))
	if cursor.fetchone() is not None:
		print("user already exist...")
	else:
		cursor.execute("INSERT INTO login (username, password, role, status) VALUES (%s, %s, %s, %s)",(user, password, role, status))	
		print("New user is created...")
	db.commit()

def logout():
	user = input("Enter user name(for logout)	:")
	print("You are succesfully logout...")
	status = "deactive"
	cursor.execute(f"UPDATE login SET status = %s WHERE username = %s",(status,user))
	db.commit()
	exit()

def change_password():
	user = input("Enter user name	:")
	password = input("Enter new password	:")
	conform_password = input("Enter comform password	:")
	if password == conform_password:
		cursor.execute(f"UPDATE login SET password = %s WHERE username = %s",(password,user))
		print("Password is changed...")
	else:
		print("Invailed username and password...")
	db.commit()

def admin():
	while True:
		print("*" * 40)
		print(f"{'ADMIN AUTHENTICATION':^40}")  
		print("*" * 40)
		choice = int(input("""
1.	MODIFY QUIZ
2.	CREATE USER
3.	CHANGE PASSWORD
4.	Exit
ENTER YOUR CHOICE	:"""))

		if choice == 1:
			from quiz.quizmgmt import quiz_manage
			quiz_manage()
		elif choice == 2:
			create_user()
		elif choice	== 3:
			change_password()
		elif choice == 4:
			return
		else:
			print("invelid choice...")