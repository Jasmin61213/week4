from email import message
from flask import Flask 
from flask import request 
from flask import redirect 
from flask import render_template 
from flask import session
from flask import url_for

app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/" 
)
app.secret_key="any string but secret"

# 首頁
@app.route("/")
def index():
    return render_template("main.html")

# 登入驗證 post方法 導向成功或失敗
@app.route("/signin",methods=["post"])
def signin():
    account=request.form["account"]
    account=str(account)
    secret=request.form["secret"]
    secret=str(secret)
    if account=="test":
        if secret=="test":
            session["account"]=request.form["account"]
        elif secret=="":
            return redirect(url_for("error",message="請輸入帳號,密碼"))
        else:
            return redirect(url_for("error",message="帳號或密碼輸入錯誤"))
        return redirect("/member")
    elif account=="":
        render_template("error.html",data="請輸入帳號,密碼")
        return redirect(url_for("error",message="請輸入帳號,密碼"))
    elif secret=="":
        return redirect(url_for("error",message="請輸入帳號,密碼"))      
    else:
        return redirect(url_for("error",message="帳號或密碼輸入錯誤"))

# 成功頁面
@app.route("/member")
def member():
    if "account" in session:
        return render_template("member.html")
    else:
        return render_template("main.html")

# 失敗頁面
@app.route("/error")
def error():
    data=request.args.get("message","")
    data=str(data)
    return render_template("error.html",message=data)

# 登出頁面導向首頁
@app.route("/signout")
def signout():
    session.pop("account", None)
    return render_template("main.html")

# 計算正整數平方
@app.route("/square")
def square():
    number=request.args.get("num","")
    number=int(number)
    result=number*number
    return render_template("result.html",data=result)

# 埠號
app.run(port=3000)
