from flask import Flask , render_template 
app=Flask(__name__)



@app.route('/') 
def show_user_profile():
    return  "Hello World!"
    
@app.route('/dojo') 
def show_user_profile1():
    return  "Dojo!"

@app.route('/say/<name>') 
def show_user_profile2(name):
    return  "Hi "+name

@app.route('/repeat/<id>/<name>') 
def show_user_profile3(name,id):
   
    return render_template('index.html', _n=name ,_num=int(id))


if __name__=="__main__":
    app.run(debug=True)
    
    
    
 
