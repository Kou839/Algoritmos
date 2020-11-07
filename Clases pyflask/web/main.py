from flask import Flask, request, make_response, redirect,  render_template, url_for
#se crea un objeto tipo app
app= Flask(__name__)

@app.errorhandler(404) 
def not_found(error): 
    return render_template(404)

@app.route('/') 
def home(): 
    user_ip = request.remote_addr
    response= make_response(redirect('hello'))
    response.set_cookie('ip', user_ip) 
    response.set_cookie('neko','miau')
    return response 

@app.route('/hello')
def helloRoute(): 
    neko= request.cookies.get('neko')
    ip= request.cookies.get('ip')
    return render_template ('hello.html', mascota= neko, userIp= ip)

@app.route('/hey')
def heyRoute():
    return render_template('hey.html')


if __name__ == '__main__': 
    app.run()