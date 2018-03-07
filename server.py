from flask import Flask,render_template,request,redirect

app = Flask(__name__)
@app.route('/')
def LandingPage():
	return render_template('index.html')
@app.route('/ninja')

def all_ninjas():
	return render_template('ninjas.html')
@app.route('/ninja/<ninja_color>')
def display_color_ninja(ninja_color):
	src = '../static/images/'
	if(str(ninja_color).lower() == 'blue'):
		src += 'leonardo.jpg'
	elif(str(ninja_color).lower() == 'orange'):
		src += 'michelangelo.jpg'
	elif(str(ninja_color).lower() == 'red'):
		src += 'raphael.jpg'
	elif(str(ninja_color).lower() == 'purple'):
		src += 'donatello.jpg'
	else:
		src += 'notapril.jpg'			
	return render_template('ninja_color.html',src = src)
app.run(debug=True)