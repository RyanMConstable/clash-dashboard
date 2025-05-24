import React from 'react';
import {useParams } from 'react-router-dom';
import {useEffect, useState } from 'react';

function ClanDashboard() {
  const { clantag } = useParams();
  const [clanData, setClanData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);


  useEffect(() => {
	  const fetchClanData = async () => {
		  try {
			  const response = await fetch(`/api/clandashboard?clantag=${clantag}`);
			  if (!response.ok) {
				  throw new Error('Failed to fetch clan data');
			  }
			  const data = await response.json();
			  setClanData(data);
		  } catch (err) {
			  setError(err.message);
		  } finally {
			  setLoading(false);
		  }
	  };

	  fetchClanData();
  }, [clantag]);

if (loading) return <p>Loading clan data...</p>;
if (error) return <p>Error: {error}</p>;

  return (
    <>
      <div>
	  <h1>{ clantag }</h1>
	  <pre>{JSON.stringify(clanData, null, 2)}</pre>
      </div>
    </>
  )
}

export default ClanDashboard 
