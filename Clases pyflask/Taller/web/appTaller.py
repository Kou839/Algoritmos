from flask import Flask, request, make_response, redirect,  render_template, url_for
#se crea un objeto tipo app
app= Flask(__name__)

@app.errorhandler(404) 
def not_found(error): 
    return render_template(404)

@app.route('/') 
def home(): 
    
    return render_template('home.html')

@app.route('/hello')
def helloRoute(): 
    neko= request.cookies.get('neko')
    ip= request.cookies.get('ip')
    return render_template ('hello.html', mascota= neko, userIp= ip)

@app.route('/hey')
def heyRoute():
    return render_template('hey.html')

@app.route('/personajes')
def personajesRoute(): 
    personajes= request.cookies.get('personajes') 
    ip= request.cookies.get('ip')
    return render_template('personajes.html', tipo= personajes,userip= ip  )

@app.route('/lugares') 
def lugaresRoute():  
    lugares= request.cookies.get('lugares')
    ip= request.cookies.get('ip')
    return  render_template('lugares.html', tipo= lugares, userip= ip)

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        nameUser = request.form['name']
        passUser = request.form ['pass']
        if (passUser == 'hola1234'):
            return  redirect(url_for('home'))
        else:
            return 'Falló proceso de autenticación'
    else: 
        return render_template('login.html')


if __name__ == '__main__': 
    app.run()