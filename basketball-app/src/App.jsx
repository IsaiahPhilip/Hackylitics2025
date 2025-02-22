import { useState } from 'react'
import './App.css'
import Court from './court.jsx'
import PercentageDisplay from './Percentage.jsx';
import BasketballIcon from './BasketballIcon.jsx';

function App() {
  const [position, setPosition] = useState(null);
  const [data, setData] = useState(null);
  const [animationKey, setAnimationKey] = useState(0);

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
    setAnimationKey(prevKey => prevKey + 1);
  }

  return (
    <div style={{ display: "flex", justifyContent: "center", alignItems: "center", height: "100vh" }}>
      {/* Basketball Court */}
      <div style={{ position: "relative" }}>
        <Court onClick={handleCourtClick} />
        {position && <Marker x={position.x} y={position.y} />}
      </div>

      {/* Popup Sidebar (Auto-Generated) */}
      {position && (

        <div key={animationKey} style={popupStyle} className="popup">
          {/* <p><strong>X:</strong> {Math.round(25 - Math.round(position.y)/10)}</p>
          <p><strong>Y:</strong> {Math.round(Math.round(position.x)/10)}</p> */}
          {/* <p>Percent: {data || "Loading..."}</p> */}
          <div id="shot-percentage">
            <PercentageDisplay/>
          </div>
          <div id="similarity">
            <h3>Most similar to:</h3>
            <p>Flipping a coin</p>
          </div>
          <div id="highest-team">
            <h3>Highest % team</h3>
            <p>Portland Trailblazers</p>
          </div>
          <div id="highest-player">
            <h3>Highest % player</h3>
            <p>Lebron James</p>
          </div>
          <div id="shot-video">
            <h3>Shot video</h3>
            <p>{Math.random()}</p>
          </div>
          {/* {probability !== null ? (
            <p><strong>Probability:</strong> {(probability * 100).toFixed(2)}%</p>
          ) : (
            <p>Loading probability...</p>
          )} */}
        </div>
      )}
    </div>
  );
}

// Marker component
function Marker({ x, y }) {
  return (
    <div style={{
      position: 'absolute',
      left: x - 10,
      top: y - 10,
      pointerEvents: 'none'
    }}>
      <BasketballIcon />
    </div>
  );
}

// Popup styles
const popupStyle = {
  width: "250px",
  height: "500px",
  marginLeft: "20px",
  backgroundColor: "#D9D9D9",
  boxShadow: "0px 0px 10px rgba(0, 0, 0, 0.1)",
  borderRadius: "8px",
  fontFamily: "Arial, sans-serif",
  padding: "20px",
  color: "#4A4A4A",
  overflowY: "auto", // Make the popup scrollable
};

//   return (
//     <div style={{ textAlign: "center" }}>
//       <Court onClick={handleCourtClick} />
//       {position && (
//         <p>
//           Shot Position: X = {Math.round(25 - Math.round(position.y)/10)}, Y = {Math.round(Math.round(position.x)/10)} <br></br>
//           Percent: {data || "Loading..."}
//         </p>
//       )}
//     </div>
//   );
// }

export default App
