from flask import Flask, render_template_string
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Google Meet Clone</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                background-color: #f1f3f4;
                font-family: 'Roboto', sans-serif;
            }
            #header {
                background-color: #white;
                color: black;
                padding: 20px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
            }
            #header img {
                width: 120px;
                height: auto;
            }
            #header .title {
                font-size: 24px;
                font-weight: 500;
            }
            #video-container {
                display: flex;
                justify-content: center;
                align-items: center;
                height: calc(100vh - 140px);
                margin-top: 20px;
                position: relative;
            }
            #my-video {
                width: 700px;
                height: 400px;
                border-radius: 10px;
                background-color: #000;
                box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.2);
            }
            #buttons-container {
                position: absolute;
                bottom: 50px;
                width: 100%;
                display: flex;
                justify-content: center;
                gap: 20px;
            }
            .action-button {
                background-color: #f8f9fa;
                border: none;
                padding: 10px;
                border-radius: 50%;
                box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.2);
                cursor: pointer;
                transition: all 0.3s ease;
            }
            .action-button:hover {
                background-color: #e8e8e8;
            }
            .action-button.active {
                background-color: #34b7f1;
            }
            .action-button.inactive {
                background-color: #e53935;
            }
            #chat-container {
                position: fixed;
                bottom: 20px;
                right: 20px;
                width: 300px;
                height: 400px;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
                padding: 20px;
                overflow-y: scroll;
            }
            #chat-messages {
                margin-bottom: 20px;
                overflow-y: auto;
                height: 80%;
                font-size: 14px;
            }
            #chat-input {
                width: 100%;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            #join-button {
                background-color: #34b7f1;
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 18px;
                border-radius: 25px;
                box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.2);
                cursor: pointer;
                transition: all 0.3s ease;
            }
            #join-button:hover {
                background-color: #0f75d5;
            }
        </style>
    </head>
    <body>

        <div id="header">
            <img src="https://static-00.iconduck.com/assets.00/google-meet-icon-2048x2048-js4zjooy.png" alt="Google Meet">
            <div class="title">Google Meet</div>
        </div>

        <div id="video-container">
            <video id="my-video" autoplay muted></video>
            <div id="buttons-container">
                <button id="microphone-btn" class="action-button inactive" onclick="toggleMicrophone()">Mic</button>
                <button id="camera-btn" class="action-button inactive" onclick="toggleCamera()">Camera</button>
            </div>
        </div>

        <div id="chat-container">
            <div id="chat-messages"></div>
            <input type="text" id="chat-input" placeholder="Type your message..." onkeydown="sendMessage(event)">
        </div>

        <button id="join-button" onclick="joinMeeting()">Join</button>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.0/socket.io.min.js"></script>
        <script>
            let socket = io();

            let videoElement = document.getElementById('my-video');
            let localStream;
            let isCameraOn = false;
            let isMicrophoneOn = false;

            function toggleCamera() {
                if (isCameraOn) {
                    localStream.getTracks().forEach(track => {
                        if (track.kind === 'video') {
                            track.stop();
                        }
                    });
                    videoElement.srcObject = null;
                    document.getElementById('camera-btn').classList.remove('active');
                    document.getElementById('camera-btn').classList.add('inactive');
                } else {
                    navigator.mediaDevices.getUserMedia({ video: true, audio: false })
                        .then(stream => {
                            localStream = stream;
                            videoElement.srcObject = stream;
                            document.getElementById('camera-btn').classList.remove('inactive');
                            document.getElementById('camera-btn').classList.add('active');
                        });
                }
                isCameraOn = !isCameraOn;
            }

            function toggleMicrophone() {
                if (isMicrophoneOn) {
                    localStream.getTracks().forEach(track => {
                        if (track.kind === 'audio') {
                            track.stop();
                        }
                    });
                    document.getElementById('microphone-btn').classList.remove('active');
                    document.getElementById('microphone-btn').classList.add('inactive');
                } else {
                    navigator.mediaDevices.getUserMedia({ video: false, audio: true })
                        .then(stream => {
                            localStream = stream;
                            document.getElementById('microphone-btn').classList.remove('inactive');
                            document.getElementById('microphone-btn').classList.add('active');
                        });
                }
                isMicrophoneOn = !isMicrophoneOn;
            }

            function joinMeeting() {
                document.getElementById('join-button').innerText = 'Joining...';
                setInterval(() => {
                    document.getElementById('join-button').innerText = 'Joined!';
                }, 2000);
            }

            function sendMessage(event) {
                if (event.key === 'Enter') {
                    let message = document.getElementById('chat-input').value;
                    if (message) {
                        socket.emit('message', message);
                        document.getElementById('chat-input').value = '';
                    }
                }
            }

            socket.on('message', function(response) {
                let messagesDiv = document.getElementById('chat-messages');
                let newMessage = document.createElement('div');
                newMessage.textContent = response;
                messagesDiv.appendChild(newMessage);
            });
        </script>

    </body>
    </html>
    ''')

@socketio.on('message')
def handle_message(msg):
    responses = {
        'hello': 'Hi there! How can I help you today?', #229+-233 Open-Source
        'how are you?': "I'm doing well, thank you for asking!",
        'what is python?': "Python is a popular programming language."
    }
    response = responses.get(msg.lower(), "Sorry, I don't understand that.")
    emit('message', response)

if __name__ == '__main__':
    socketio.run(app, debug=True)