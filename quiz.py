import pymysql,time

db = pymysql.connect(host='localhost',user='root',passwd='12345')
cursor = db.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS quiz')
cursor.execute('USE quiz')
cursor.execute("""
CREATE TABLE IF NOT EXISTS leaderboard (name VARCHAR(10),score INT(5),score_limit INT(5),scoreper INT(5))""")

def play_quiz():
	print("""
Rule:
	1. A,B,C,D and a,b,c,d and 1,2,3,4 is not accepted.
	2. Small letterand Capitel letter is correct
""")
	name = input("Enter your name to start quiz	:")
	score = 0
	limit = 0
	cursor.execute("SELECT * FROM questions")
	queston = cursor.fetchall()
	if queston == None:
		print("No questions available...")
	else:
		for i in queston:
			print()
			print("{:<5}{:<60}".format(i[0],i[1]))
			answer = input("""
(A) {:<5}
(B) {:<5}
(C) {:<5}
(D) {:<5}
Write your answer	:""".format(i[2],i[3],i[4],i[5]))
			limit +=1
			if answer == i[6]:
				score += 1
				print("✅	Correct Answer...")
				print(f"Your score is {score}")
				choice = input("Do you want to play next(y/n)	:")
			else:
				print("❌	Incorrect Answer...")
				print(f"Correct answer is {i[6]}")
				print(f"Your score is {score}")
				choice = input("Do you want to play next(y/n)	:")

			if choice == "n":
				break

		scoreper = (score / limit) * 100
		print(f"{name} your total score is {score} out of {limit} and your score percent is {scoreper}")
		cursor.execute("INSERT INTO leaderboard( name, score, score_limit, scoreper) VALUES(%s,%s,%s,%s)",(name,score,limit,scoreper))
		db.commit()
		return
