from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template('index.html')

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/ninja/blue')
def blue():
    return render_template('blue.html')

@app.route('/ninja/orange')
def orange():
    return render_template('orange.html')

@app.route('/ninja/red')
def red():
    return render_template('red.html')

@app.route('/ninja/purple')
def purple():
    return render_template('purple.html')

@app.route('/ninja/<input>')
def show(input):
    if input !='red' or 'blue' or 'orange' or 'purple':
        return render_template('april.html')



app.run(debug=True) # run our server
