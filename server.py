from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    student_name = request.form['first_name']
    num_fruits = int(request.form['raspberry']) + int(request.form['strawberry']) + int(request.form['apple'])
    print(f'Charging {student_name} for {num_fruits} fruits!')
    return render_template("checkout.html", strawberries=request.form['strawberry'], 
    raspberries=request.form['raspberry'], 
    apples=request.form['apple'],
    first_name=request.form['first_name'],
    last_name=request.form['last_name'],
    student_id=request.form['student_id'])


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)