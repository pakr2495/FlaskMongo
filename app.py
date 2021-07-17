from flask import Flask,render_template,jsonify,g,url_for,request,flash,redirect
from db import DB


app = Flask(__name__)

app.secret_key = "Hi Hello Bye"

@app.before_request
def beforeRequest():
    if not hasattr(g,"conn"):
        g.conn = DB()


@app.route('/',methods=['GET'])
def index():
    datas = g.conn.collection.find({})
    return render_template("display.html",datas=datas)

@app.route('/new',methods=['GET','POST'])
def new():
    if request.method == 'POST':
        form_data = request.form
        g.conn.insertData(int(form_data['id']),form_data['name'],form_data['description'],form_data['status'],form_data['duedate'])
        flash(message='Sucessfully Updated',category='info')
        return redirect('/')

    else:
        return render_template('new.html'),200

@app.route('/delete/<int:id>',methods=['GET'])
def delete(id):
    print(g.conn.collection.count_documents({"Id":id}))
    g.conn.collection.delete_one({"Id":id})
    flash(message='Sucessfully Deleted',category='info')
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True,port=3000)

