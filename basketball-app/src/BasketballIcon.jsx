import React from 'react';

function BasketballIcon() {
  return (
    <svg
      width="20"
      height="20"
      viewBox="0 0 24 24"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <circle cx="12" cy="12" r="10" stroke="black" strokeWidth="1" fill="#E8D5B7" />
      <path d="M12 2C6.48 2 2 6.48 2 12" stroke="black" strokeWidth="1" />
      <path d="M12 22C17.52 22 22 17.52 22 12" stroke="black" strokeWidth="1" />
      <path d="M2 12C2 17.52 6.48 22 12 22" stroke="black" strokeWidth="1" />
      <path d="M22 12C22 6.48 17.52 2 12 2" stroke="black" strokeWidth="1" />
    </svg>
  );
}

export default BasketballIcon;