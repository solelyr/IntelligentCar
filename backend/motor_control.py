try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    IS_RPI = True
    print("项目启动")
except (ImportError, RuntimeError):
    print("⚠️ 运行在非树莓派环境，使用虚拟 GPIO 模式")
    IS_RPI = False

class MotorControl:
    def __init__(self, socketio=None):  # ✅ 增加 socketio 参数
        self.socketio = socketio
        if IS_RPI:
            self.left_forward = 13
            self.left_backward = 19
            self.ENA = 26 
            self.right_forward = 20
            self.right_backward = 21
            self.ENB = 16
            GPIO.setup(
                [self.left_forward, self.left_backward, self.right_forward, self.right_backward,self.ENA,self.ENB],
                GPIO.OUT,
            )

    def _emit(self, message: str):
        """用于向前端实时发送状态"""
        if self.socketio:
            self.socketio.emit("status", {"message": message})
        else:
            print(f"[LOG] {message}")

    def forward(self):
        print("前进")
        self._emit("🚗 正在前进")
        if IS_RPI:
            GPIO.output(self.left_forward, 1)
            GPIO.output(self.left_backward, 0)
            GPIO.output(self.ENA, 1)
            GPIO.output(self.right_forward, 1)
            GPIO.output(self.right_backward, 0)
            GPIO.output(self.ENB, 1)

    def backward(self):
        print("后退")
        self._emit("↩️ 正在后退")
        if IS_RPI:
            GPIO.output(self.left_forward, 0)
            GPIO.output(self.left_backward, 1)
            GPIO.output(self.ENA, 1)
            GPIO.output(self.right_forward, 0)
            GPIO.output(self.right_backward, 1)
            GPIO.output(self.ENB, 1)

    def left(self):
        print("左转")
        self._emit("⬅️ 左转中")
        if IS_RPI:
            GPIO.output(self.left_forward, 0)
            GPIO.output(self.left_backward, 1)
            GPIO.output(self.ENA, 1)
            GPIO.output(self.right_forward, 1)
            GPIO.output(self.right_backward, 0)
            GPIO.output(self.ENB, 1)

    def right(self):
        print("右转")
        self._emit("➡️ 右转中")
        if IS_RPI:
            GPIO.output(self.left_forward, 1)
            GPIO.output(self.left_backward, 0)
            GPIO.output(self.ENA, 1)
            GPIO.output(self.right_forward, 0)
            GPIO.output(self.right_backward, 1)
            GPIO.output(self.ENB, 1)

    def stop(self):
        print("停止")
        self._emit("⛔ 已停止")
        if IS_RPI:
            GPIO.output(self.left_forward, 0)
            GPIO.output(self.left_backward, 0)
            GPIO.output(self.ENA, 0)
            GPIO.output(self.right_forward, 0)
            GPIO.output(self.right_backward, 0)
            GPIO.output(self.ENB, 0)

    def cleanup(self):
        if IS_RPI:
            GPIO.cleanup()
