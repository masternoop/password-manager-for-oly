import pymysql
from getpass import getpass

class PasswordManager:
    def __init__(self):
        self.db = pymysql.connect(
            host="localhost",
            user="nice try",    
            password=getpass("nope"),    
            database="password_manager"
        )
        self.cursor = self.db.cursor()

    def add_password(self, website, username, password):
        sql = "INSERT INTO passwords (website, username, password) VALUES (%s, %s, %s)"
        val = (website, username, password)
        self.cursor.execute(sql, val)
        self.db.commit()
        print("Password added successfully")

    def get_password(self, website):
        sql = "SELECT username, password FROM passwords WHERE website = %s"
        val = (website,)
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        if result:
            print(f"Website: {website}")
            print(f"Username: {result[0]}")
            print(f"Password: {result[1]}")
        else:
            print("No password found for this website")

    def update_password(self, website, username, new_password):
        sql = "UPDATE passwords SET password = %s WHERE website = %s AND username = %s"
        val = (new_password, website, username)
        self.cursor.execute(sql, val)
        self.db.commit()
        print("Password updated successfully")

    def delete_password(self, website, username):
        sql = "DELETE FROM passwords WHERE website = %s AND username = %s"
        val = (website, username)
        self.cursor.execute(sql, val)
        self.db.commit()
        print("Password deleted successfully")

    def list_passwords(self):
        sql = "SELECT website, username, password FROM passwords"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        for (website, username, password) in results:
            print(f"Website: {website}, Username: {username}, Password: {password}")

if __name__ == "__main__":
    pm = PasswordManager()
    
    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Update Password")
        print("4. Delete Password")
        print("5. List All Passwords")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            pm.add_password(website, username, password)
        elif choice == "2":
            website = input("Enter website: ")
            pm.get_password(website)
        elif choice == "3":
            website = input("Enter website: ")
            username = input("Enter username: ")
            new_password = getpass("Enter new password: ")
            pm.update_password(website, username, new_password)
        elif choice == "4":
            website = input("Enter website: ")
            username = input("Enter username: ")
            pm.delete_password(website, username)
        elif choice == "5":
            pm.list_passwords()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
