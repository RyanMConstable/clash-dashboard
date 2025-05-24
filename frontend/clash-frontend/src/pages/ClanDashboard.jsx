import React from 'react';
import {useParams } from 'react-router-dom';

function ClanDashboard() {
  const { clantag } = useParams();
  console.log('clantag from useParams:', clantag);

  return (
    <>
      <div>
	  <h1>Dashboard for clan: { clantag || "No clan tag provided"}</h1>
      </div>
    </>
  )
}

export default ClanDashboard 
