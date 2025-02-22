import { useEffect, useState } from 'react';

const PercentageDisplay = () => {
  const [data, setData] = useState(null);
  const[loading,setLoading] = useState(true);
  const[error,setError] = useState(null);

  const fetchRandomData = () => { 
    setLoading(true); 
    fetch('http://localhost:5000/')
    .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Fetched data:', data); // Log the fetched data
        setData(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        setError(error);
        setLoading(false);
      });
  }

  useEffect(() => {
    fetchRandomData(); 
  }, []); 

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error.message}</p>;
  }

  return (
    <div> 
    {data ? (
        <div>
            <p>Percentage: {data.percentage} </p>
            <button onClick={fetchRandomData}>Get Another Random Percentage</button>
        </div>
            
        ): (
            <p> No data available</p>
        )}
    </div>
  );
};

export default PercentageDisplay;