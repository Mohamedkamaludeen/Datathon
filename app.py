from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/home',methods=['POST', 'GET'])
def index():
     if request.method == 'POST':
        loc=request.form['loc']
        loc=request.form['n']
        loc=request.form['v']
        loc=request.form['e']
        loc=request.form['t']
        loc=request.form['lOCode']
        loc=request.form['uniq_Opnd']
        loc=request.form['total_Op']
        loc=request.form['total_Opnd']
        loc=request.form['branchCount']

        feature_list = []

         feature_list.append(float(loc))
         feature_list.append(float(n))
         feature_list.append(float(v))
         feature_list.append(float(e))
         feature_list.append(float(t))
         feature_list.append(float(lOCode))
         feature_list.append(float(uniq_Opnd))
         feature_list.append(float(total_Op))
         feature_list.append(float(total_Opnd))
         feature_list.append(float(branchCount))
    return render_template('index.html')

@app.route('/home1')
def index2():
    return "Hello Ravindu"

@app.route('/nav')
def index3():
    return render_template('nav.html')

@app.route('/upload')
def index4():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)