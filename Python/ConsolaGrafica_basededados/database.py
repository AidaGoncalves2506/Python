import mysql.connector 
banana = mysql.connector.connect(host="localhost", user="root", password="", database="pi04_db")
cursor=banana.cursor()


if banana and banana.is_connected():
    
    with banana.cursor() as cursor:
        result = cursor.execute("INSERT INTO pi04 (Nome_formando, Num_Formando, Nome_Curso, Nota_Final) VALUES ('Catarina Gonçalves', '11', 'pi04', '18.6')")
        banana.commit()
        result = cursor.execute("SELECT * FROM pi04")
        
        rows = cursor.fetchall()
        
        for row in rows:
            print(row[0])
            print(row[1])
            print(row[2])
            print(row[3])
            
    banana.close()

else:
    print("Could not connect")