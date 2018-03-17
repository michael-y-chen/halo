from flask import Flask, render_template, request,  make_response, session
from models import db, User, Record 
from authentication import UserAuthentication
from functools import wraps
from flask.ext.session import Session
from flask.ext.bcrypt import Bcrypt

import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SESSION_TYPE'] = 'memcached'
app.secret_key = "HaloKey"
bcrypt = Bcrypt(app)
db.init_app(app)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
            init()
            AuthUser=session.get("user",None)
            authenticated = False  
            validUser= User.query.filter(User.username==AuthUser)
            for r in validUser:
                authenticated=True
            if authenticated:
                return f(*args, **kwargs)
            return render_template("login.html")
    return decorated_function




#VIEWS 


## Home -- Entry point
@app.route('/')
@login_required
def index():
    return render_template("index.html")


## GET and SET

@app.route('/get')
@login_required
def get():
    AuthUser=session.get("user", None)
    reqK=request.args.get("k")
    theRec=Record.query.filter(Record.user==AuthUser, Record.key == reqK)
    ret=[]
    for r in theRec:
      ret.append({'user':r.user,'key':r.key,'value':r.value})
    return json.dumps(ret)


@app.route('/set',methods=["POST"])
@login_required
def set():
    AuthUser=session.get("user", None)
    reqK=request.form.get("k")
    reqV=request.form.get("v")
    theRec=Record.query.filter(Record.user==AuthUser, Record.key == reqK).first()
    ret=""
    if theRec == None:
        db.session.add(Record(key=reqK, value=reqV, user=AuthUser))
        ret="Added"
    else:
        theRec.value=reqV
        ret="Updated"
    db.session.commit()
    return ret

##Showing All Results -- test purpose only

@app.route('/showall')
def showall():
     allRec=Record.query.all()
     rec=[]
     for r in allRec:
       rec.append({'user':r.user,'key':r.key,'value':r.value})
     allUsr=User.query.all()
     usr=[]
     for r in allUsr:
       usr.append({'username':r.username,'password':r.password})
     ret = {"users":usr, "records":rec}
     return json.dumps(ret)



## giveme all my records

@app.route('/showmine')
@login_required
def showmine():
    AuthUser=session.get("user", None)
    allRec=Record.query.filter(Record.user==AuthUser)
    ret=[]
    for r in allRec:
      ret.append({'user':r.user,'key':r.key,'value':r.value})
    return json.dumps(ret)


## USER login/ register API's . 
## can use flask_security but it redirects me to / URL, without port number 
## my test platform got port 80 used 

@app.route("/logout")
def logout():
    session["user"]=None
    return "Logged Out"

@app.route("/login", methods=["POST"])
def login():
    uid=request.form.get("uid")
    pw = request.form.get("password")
    auth = UserAuthentication.authenticate(uid, pw, bcrypt)
    if auth == "True":
        session["user"]= uid

    return auth


@app.route("/register", methods=["POST"])
def register():
    uid=request.form.get("uid")
    pw = request.form.get("password")
    return UserAuthentication.register(uid,pw, db,bcrypt)


def init():
    db.create_all()
    
