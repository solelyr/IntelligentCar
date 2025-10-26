import axios from "axios";

export async function sendCommand(action: string) {
  const res = await axios.post("/api/control", { action });
  console.log("res:",res);
  return res.data;
}
