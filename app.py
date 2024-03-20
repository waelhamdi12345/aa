from flask import Flask, render_template
from flask_socketio import SocketIO, emit
app = Flask(__name__)
somelist=['appel','pease','kzda','eggge']
i=0
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
@app.route('/')
def index():
    return render_template('index.html')
@socketio.on('message')
def handle_message(message):
    print(message)
    global i 
    if i< len(somelist):
        socketio.send(somelist[i])
        i+=1
    
if __name__ == '__main__':
    app.run()(debug=False,host='0.0.0.0')
