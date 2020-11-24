from flask import Flask, request, make_response, redirect, render_template, url_for

app= Flask(__name__) 

@app.errorhandler(404) 
def not_found(error): 
    return render_template('404.html') 

@app.route('/') 
def home(): 
    return render_template('home.html') 

@app.route('/pacientes') 
def pacientesRoute(): 
    pacientes= request.cookies.get('pacientes') 
    ip= request.cookies.get('ip')
    return render_template('pacientes.html', tipo= pacientes, userIp= ip)

@app.route('/doctors') 
def doctorsRoute(): 
    doctores= request.cookies.get('doctores') 
    ip= request.cookies.get('ip')
    return render_template('doctors.html', tipo= doctores, userIp= ip)  

@app.route('/conocenos') 
def conocenosRoute(): 
    conocenos= request.cookies.get('conocenos') 
    ip= request.cookies.get('ip')
    return render_template('conocenos.html', tipo= conocenos, userIp= ip)  

@app.route('/contact')
def contactRoute(): 
    contactos= request.cookies.get('contactos') 
    ip= request.cookies.get('ip')
    return render_template('contact.html', tipo= contactos, userIp= ip) 

@app.route('/curioso')
def curiosoRoute(): 
    curioso= request.cookies.get('curioso') 
    ip= request.cookies.get('ip')
    return render_template('curioso.html', tipo= curioso, userIp= ip) 



