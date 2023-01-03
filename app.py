from flask import Flask, render_template,request,redirect

app = Flask(__name__)

dic=[]
@app.route("/create_user",methods=["POST","GET"])
def create_user():
    name=request.json.get("name")
    mobile=request.json.get("mobile")
    about=request.json.get("about")
    temp={"name":name,"mobile":mobile,"about":about}
    dic.append(temp)
    return dic

if __name__=="__main__":
    app.run(debug=True)