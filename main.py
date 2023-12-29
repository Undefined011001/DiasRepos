import psycopg2

	
conn = psycopg2.connect(
        host = '78.141.227.124',
        user = 'postgres',
        database = 'GITHUB',
        password = '123')
print('Подключение успешно')

cur  = conn.cursor()

# cur.execute('SELECT * FROM students')
# # students = cur.fetchall()
# cur.execute('SELECT COUNT(*) FROM students WHERE age > 15 ')
# students = cur.fetchall()

cur.execute("SELECT AVG(age) FROM students WHERE stud_name LIKE 'A%'")
students = cur.fetchall()

for i in students: 
    print(i)

# Что ты здесь ищешь?))))
    
    
