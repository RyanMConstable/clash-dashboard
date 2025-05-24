import React from 'react';
import {useParams } from 'react-router-dom';

function ClanDashboard() {
  const { clantag } = useParams();

  const fetchClanData = async (clantag) => {
	  const reponse = await fetch(`/api/clandashboard?clantag=${encodeURIComponent(clantag)}`);
	  if (!response.ok) throw new Error("Failed to fetch clan data");
	  const data = await response.json();
	  console.log(data);
	  return data;
  };


  return (
    <>
      <div>
	  <h1>{ clantag }</h1>
      </div>
    </>
  )
}

export default ClanDashboard 
