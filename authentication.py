from models import User

class UserAuthentication:
    @staticmethod
    def authenticate(uid, pw, bcrypt):
        userAuth="Invalid ID/PW"
        usermatch=User.query.filter(User.username == uid)
        for u in usermatch:
           if bcrypt.check_password_hash(u.password, pw):
              userAuth="True"
        return userAuth

    @staticmethod
    def register (uid, pw, db, bcrypt):
        userExists=False
        usermatch=User.query.filter(User.username == uid)
        for u in usermatch:
            userExists=True
        if userExists:
            return "User Already Exists"
        try:
            db.session.add(User(username=uid, password=bcrypt.generate_password_hash(pw)))
            db.session.commit()
            return "True"
        except Exception as e:
            return "There is an Error: %s"%e


