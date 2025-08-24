# from quiz.admin import admin,logout
# from quiz.quiz import play_quiz
# from quiz.leaderboard import leader_board
# import pymysql

# db = pymysql.connect(host='localhost',user='root',passwd='12345')
# cursor = db.cursor()
# cursor.execute('CREATE DATABASE IF NOT EXISTS quiz')
# cursor.execute('USE quiz')
# cursor.execute("CREATE TABLE IF NOT EXISTS login( username VARCHAR(10), password VARCHAR(10), role VARCHAR(7), status VARCHAR(10))")


def login():
	user = input("Enter user name	:")
	password = input("Enter user password	:")
	status = "active"
	cursor.execute("SELECT username FROM login WHERE username = %s AND password = %s",(user, password))
	check = cursor.fetchone()
	if check == None:
		print("Invalid isername or password")
	else:
		cursor.execute(f"UPDATE login SET status = %s WHERE username = %s",(status,user))
		print("Log in succesfully...")
	
	db.commit()

def main():
	while True:
		print("*" * 40)
		print(f"{'MAIN MENU':^40}")  
		print("*" * 40)
		choice = int(input("""
1.	LOGIN
2.	PLAY QUIZ
3.	SHOW LEADER BOARD
4.	Exit
ENTER YOUR CHOICE	:"""))

		if choice == 1:
			login()
			admin()
		elif choice == 2:
			play_quiz()
		elif choice	== 3:
			leader_board()
		elif choice == 4:
			logout()
			exit()
		else:
			print("invelid choice")

main()