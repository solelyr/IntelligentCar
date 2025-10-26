import { useEffect, useState } from "react";
import { io } from "socket.io-client";
import VideoPlayer from "./VideoPlayer";
import "./index.css";

// 自动适配当前运行环境
const socket = io(window.location.origin);

export default function App() {
  const [status, setStatus] = useState("未连接");
  const [logs, setLogs] = useState<string[]>([]);

  // ✅ MediaMTX WebRTC 地址（改成你的树莓派IP）
  const streamUrl = "http://192.168.1.2:8889/cam/";

  useEffect(() => {
    socket.on("connect", () => {
      setStatus("✅ 已连接服务器");
    });

    socket.on("disconnect", () => {
      setStatus("❌ 连接断开");
    });

    socket.on("status", (data) => {
      setLogs((prev) => [data.message, ...prev]);
    });

    return () => {
      socket.disconnect();
    };
  }, []);

  function send(action: string) {
    console.log("control", { action });
    socket.emit("control", { action });
  }

  return (
    <div className="container">
      <h1>🚗 树莓派智能小车控制台</h1>
      <p>{status}</p>

      {/* 摄像头实时视频 */}
      <h3>📹 实时视频</h3>
      <VideoPlayer streamUrl={streamUrl} />

      {/* 控制区 */}
      <div className="controls">
        <button onClick={() => send("forward")}>↑</button>
        <div>
          <button onClick={() => send("left")}>←</button>
          <button onClick={() => send("stop")}>■</button>
          <button onClick={() => send("right")}>→</button>
        </div>
        <button onClick={() => send("backward")}>↓</button>
      </div>

      {/* 状态日志 */}
      <h3>📡 状态日志</h3>
      <ul>
        {logs.map((msg, i) => (
          <li key={i}>{msg}</li>
        ))}
      </ul>
    </div>
  );
}
