import { useState } from 'react'
import './App.css'
import Court from './court.jsx'
import PercentageDisplay from './Percentage.jsx';

function App() {
  const [position, setPosition] = useState(null);

  

  function handleCourtClick(event) {
    const rect = event.target.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    setPosition({ x, y });
  }

  return (
    <div style={{ textAlign: "center" }}>
      <Court onClick={handleCourtClick} />
      {position && (
        <p>
          Shot Position: X = {Math.round(25 - Math.round(position.y)/10)}, Y = {Math.round(Math.round(position.x)/10)}
          <PercentageDisplay/>
        </p>
      )}
    </div>
  );
}

export default App
