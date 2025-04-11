from flask import Flask, render_template_string, jsonify, request
import threading
import time
import random

app = Flask(__name__)

scanning = False
scan_progress = 0
stop_scan_flag = False
real_time_protection = False
vpn_on = False
current_file = ""
detected_threats = [] 


SIMULATED_FILES = [ #Open-Source
    "C:/Windows/System32/drivers/etc/hosts",
    "C:/Program Files/SecureX AV.exe/engine.dll",
    "C:/Users/Admin/Documents/invoice.pdf",
    "C:/Users/Admin/Downloads/setup.exe",
    "C:/Users/Admin/AppData/Local/temp123.tmp",
    "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/startup.lnk",
    "C:/Games/Fortnite/cheat.dll",
    "C:/Users/Admin/Desktop/My_CV.pdf",
    "C:\Program Files\Microsoft VS Code",
]

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SecureX AI </title>
    <style>
        body {
            background-color: #f0f4f8;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: #0a74da;
            font-size: 3rem;
        }
        button {
            background-color: #0a74da;
            color: white;
            border: none;
            padding: 15px 30px;
            margin: 10px;
            font-size: 1rem;
            border-radius: 10px;
            cursor: pointer;
        }
        button:hover {
            background-color: #095aba;
        }
        #progressBar {
            width: 100%;
            background-color: #ccc;
            border-radius: 20px;
            margin-top: 30px;
        }
        #progressBarFill {
            height: 30px;
            width: 0%;
            background-color: #0a74da;
            border-radius: 20px;
            transition: width 0.5s;
        }
        #currentFile, #vpnStatus {
            margin-top: 20px;
            font-size: 1.2rem;
            color: #555;
        }
        #fixButton {
            background-color: #ff4d4d;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>SecureX AI</h1>
    <button onclick="startScan('quick')">Quick Scan</button>
    <button onclick="startScan('full')">Full Scan</button>
    <button onclick="stopScan()">Stop Scan</button>
    <button onclick="toggleVPN()">Start/Stop VPN</button>
    <button onclick="toggleRTP()">Toggle Real-Time Protection</button>

    <div id="progressBar">
        <div id="progressBarFill"></div>
    </div>

    <div id="currentFile"></div>
    <div id="vpnStatus">VPN: OFF</div>

    <div id="fixButton" style="display: none;">
        <button onclick="fixThreats()">Fix</button>
    </div>

    <audio id="startSound" src="https://actions.google.com/sounds/v1/cartoon/wood_plank_flicks.ogg"></audio>
    <audio id="completeSound" src="https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg"></audio>

    <script>
        let scanning = false;
        let scanInterval = null;

        function playSound(id) {
            document.getElementById(id).play();
        }

        function startScan(type) {
            if (scanning) return;
            scanning = true;
            playSound('startSound');
            fetch('/start_scan', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({type: type})
            });
            scanInterval = setInterval(updateProgress, 1000);
        }

        function stopScan() {
            if (!scanning) return;
            if (confirm("Are you sure you want to stop the scan?")) {
                scanning = false;
                clearInterval(scanInterval);
                fetch('/stop_scan', {method: 'POST'});
                document.getElementById('progressBarFill').style.width = '0%';
                document.getElementById('currentFile').innerText = "";
            }
        }

        function toggleVPN() {
            fetch('/toggle_vpn', {method: 'POST'})
                .then(response => response.json())
                .then(data => {
                    document.getElementById('vpnStatus').innerText = "VPN: " + (data.vpn_on ? "ON" : "OFF");
                });
        }

        function toggleRTP() {
            fetch('/toggle_rtp', {method: 'POST'})
                .then(response => response.json())
                .then(data => alert(data.message));
        }

        function updateProgress() {
            fetch('/progress')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('progressBarFill').style.width = data.progress + '%';
                    document.getElementById('currentFile').innerText = "Scanning: " + data.current_file;
                    if (data.progress >= 100) {
                        clearInterval(scanInterval);
                        scanning = false;
                        playSound('completeSound');
                        alert(data.alert_message);
                        if (data.threats.length > 0) {
                            document.getElementById('fixButton').style.display = 'block';
                        }
                        document.getElementById('currentFile').innerText = "";
                    }
                });
        }

        function fixThreats() {
            fetch('/fix_threats', {method: 'POST'})
                .then(response => response.json())
                .then(data => {
                    alert(data.message);
                    document.getElementById('fixButton').style.display = 'none';
                });
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/start_scan", methods=["POST"])
def start_scan():
    global scanning, stop_scan_flag, fake_files, detected_threats
    scanning = True
    stop_scan_flag = False
    detected_threats = []  
    scan_type = request.json.get('type')
    fake_files = random.choices(SIMULATED_FILES, k=50)
    threading.Thread(target=scan, args=(scan_type,)).start()
    return '', 204

@app.route("/stop_scan", methods=["POST"])
def stop_scan():
    global scanning, stop_scan_flag
    scanning = False
    stop_scan_flag = True
    return '', 204

@app.route("/toggle_vpn", methods=["POST"])
def toggle_vpn():
    global vpn_on
    vpn_on = not vpn_on
    return jsonify({"vpn_on": vpn_on})

@app.route("/toggle_rtp", methods=["POST"])
def toggle_rtp():
    global real_time_protection
    real_time_protection = not real_time_protection
    message = "Real-Time Protection Enabled" if real_time_protection else "Real-Time Protection Disabled"
    return jsonify({"message": message})

@app.route("/progress")
def progress():
    global detected_threats
    return jsonify({
        "progress": scan_progress, 
        "current_file": current_file,
        "threats": detected_threats,
        "alert_message": "Scan Complete, no threats found" if not detected_threats else "Threats detected!"
    })

@app.route("/fix_threats", methods=["POST"])
def fix_threats():
    global detected_threats
    
    detected_threats = []
    return jsonify({"message": "Threats have been removed successfully!"})

def scan(scan_type):
    global scan_progress, scanning, current_file, detected_threats
    scan_progress = 0
    current_file = ""
    total_time = 60 if scan_type == "quick" else 600  #

    start_time = time.time()
    while scanning and not stop_scan_flag:
        elapsed = time.time() - start_time
        scan_progress = min(int((elapsed / total_time) * 100), 100)
        if fake_files:
            current_file = fake_files.pop(0)
        else:
            current_file = "C:/scanning/fakefile" + str(random.randint(1000, 9999)) + ".exe"

        
        if random.random() < 0.3 and int(elapsed) > 10:
            detected_threats.append(current_file)

        if scan_progress >= 100:
            scanning = False
            break
        time.sleep(1)

    scan_progress = 100
    current_file = ""

if __name__ == "__main__":
    app.run(debug=True)

