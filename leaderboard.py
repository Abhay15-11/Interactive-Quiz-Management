import pymysql

db = pymysql.connect(host='localhost',user='root',passwd='12345')
cursor = db.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS quiz')
cursor.execute('USE quiz')
cursor.execute("""
CREATE TABLE IF NOT EXISTS leaderboard (name VARCHAR(10),score INT(5),score_limit INT(5),scoreper INT(5))""")



def score():
	# Get the current leader board
	cursor.execute("SELECT * FROM leaderboard")
	queston = cursor.fetchall()
	if queston == None:
		print("No one has taken the quiz yet")
	else:
		print("{:<20}{:<10}{:<10}{:<0}".format("Names","Score","Limit","Score Percentage"))
		for i in queston:
			print("{:<22}{:<10}{:<13}{:<0}".format(i[0],i[1],i[2],i[3],))
	return

def ranks():
	cursor.execute("SELECT * FROM leaderboard ORDER BY scoreper DESC;")
	queston = cursor.fetchall()
	if queston == None:
		print("No one has taken the quiz yet")
	else:
		range = 1
		print("{:<20}{:<10}{:<10}{:<0}".format("Names","Score","Limit","Score Percentage"))
		for i in queston:
			print("{:<5}{:<22}{:<10}{:<13}{:<0}".format(range,i[0],i[1],i[2],i[3]))
			if range == len(queston):
				break
			range += 1

def leader_board():
	while True:
		print("*" * 40)
		print(f"{'LEADER BOARD':^40}")  
		print("*" * 40)
		choice = int(input("""
1.	DISPLAY ALL USER SCORE
2.	DISPLAY RANKS BASED ON SCORE PERCENTAGE
3.	EXIT
ENTER YOUR CHOICE	:"""))

		if choice == 1:
			score()
		elif choice == 2:
			ranks()
		elif choice	== 3:
			return
		else:
			print("invelid choice")