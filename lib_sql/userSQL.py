class UserSQL():
    def __init__(self, cursor) -> None:
        self.cursor = cursor

    def create_table_user(self):
        query = """
        CREATE TABLE [IF NOT EXISTS] users(
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL
        );"""
        self.cursor.execute(query)


    def add_new_user(self,name , email,password):
        query = f"""INSERT INTO users(name,email,password)
        VALUES("{name}","{email}","{password}");
        """
        self.cursor.execute(query)
        print(self.cursor)
        print("Новый пользователь успешно добавлен")

    def get_user(self,id):
        query = f"""
        SELECT * FROM users WHERE id={id}

        """
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def get_all_users(self):
        query = f"""
        SELECT * FROM users;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def delete_user(self,id):
        query = f"""
        DELETE FROM users WHERE id={id};"""
        self.cursor.execute(query)
        print(f"Пользоваель успешно  с id={id} удален")

    def update_user_email(self,id,value):
        query = f"""
        UPDATE users SET email='{value}' WHERE id={id};"""
        self.cursor.execute(query)
        print("Поле name обновлено")

    def update_user_name(self,id,value):
        query = f"""
        UPDATE users SET name='{value}' WHERE id={id};"""
        self.cursor.execute(query)
        print("Поле email обновлено")

    def update_user_password(self,id,value):
        query = f"""
        UPDATE users SET password='{value}' WHERE id={id};"""
        self.cursor.execute(query)
        print("Поле pass обновлено")





    
        





