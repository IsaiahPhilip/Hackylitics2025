import { useState, useEffect} from 'react'
import './App.css'
import Court from './court.jsx'

function App() {
  const [position, setPosition] = useState(null);
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/data")
      .then((response) => response.json())
      .then((data) => setData(data.message))
      .catch((error) => console.error("Error fetching data:", error));
  }, []);


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
          Percent: {data || "Loading..."}
        </p>
      )}
    </div>
  );
}

export default App
