import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/api": "http://localhost:8000", // Flask 后端
      "/socket.io": {
        target: "http://localhost:8000",
        ws: true
      }
    }
  }
});
