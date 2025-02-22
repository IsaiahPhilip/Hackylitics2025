import React from "react";

function Court({ onClick }) {
  return (
    <div style={{ position: "relative", display: "inline-block" }}>
      <img
        src="/court.png"  // If placed in `public/`
        alt="Basketball Court"
        width="660"
        height="500"
        onClick={onClick}
        style={{ cursor: "pointer" }}
      />
    </div>
  );
}

export default Court;
