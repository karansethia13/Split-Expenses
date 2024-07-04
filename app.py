from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/a',methods=['POST','GET'])
def home():
    num_people=0
    if request.method == 'POST' and 'hid' in request.form:
        names=[]
        for i in range(num_people):
            temp=request.form.get(f'person{i}')
            print(temp)
            names.append(temp)
        return render_template('index.html',num_people=int(num_people),names=names)
    elif request.method == 'POST' and 'peoplenumber' in request.form: 
        print('t' if 'peoplenumber' in request.form else 'nah')
        num_people=request.form.get('peoplenumber')
        return render_template('index.html',num_people=int(num_people))
    

    return render_template('index.html', num_people=num_people)

if __name__ == '__main__':
    app.run(debug=True)