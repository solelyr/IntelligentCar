import React from "react";

interface Props {
  streamUrl: string;
}

export default function VideoPlayer({ streamUrl }: Props) {
  console.log("streamUrl:",streamUrl);
  return (
    <div style={{ textAlign: "center", marginBottom: "20px" }}>
      <iframe
        src={streamUrl}
        allow="camera; microphone; fullscreen; autoplay"
        style={{
          width: "90%",
          height: "320px",
          borderRadius: "8px",
          border: "2px solid #ccc",
        }}
        title="Camera Stream"
      />
    </div>
  );
}
