from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from motor_control import MotorControl
import atexit

# 指定静态目录（React 构建产物）
app = Flask(__name__, static_folder="../frontend/dist", static_url_path="/")
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
motor = MotorControl(socketio=socketio)

@app.route("/")
def index():
    # 返回前端 index.html
    return send_from_directory(app.static_folder, "index.html")

@app.route("/api/status")
def status():
    return jsonify({"status": "SmartCar running 🚗"})

@socketio.on("connect")
def on_connect():
    print("✅ WebSocket connected")
    socketio.emit("status", {"message": "已连接智能小车系统 🚗"})

@socketio.on("disconnect")
def on_disconnect():
    print("❌ WebSocket disconnected")

@socketio.on("control")
def on_control(data):
    action = data.get("action")
    print(f"收到控制指令: {action}")
    if action == "forward":
        motor.forward()
    elif action == "backward":
        motor.backward()
    elif action == "left":
        motor.left()
    elif action == "right":
        motor.right()
    elif action == "stop":
        motor.stop()
    else:
        socketio.emit("status", {"message": "❓ 未知指令"})

if __name__ == "__main__":
    print("🚀 启动 Flask + React 一体化服务: http://localhost:8000")
    socketio.run(app, host="0.0.0.0", port=8000)

atexit.register(motor.cleanup)