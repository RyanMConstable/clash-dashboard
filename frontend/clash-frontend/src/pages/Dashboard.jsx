import React from 'react';
import {useParams } from 'react-router-dom';

function Dashboard() {
  const { clantag } = useParams();

  return (
    <>
      <div>
	  <p>Dashboard</p>
      </div>
    </>
  )
}

export default Dashboard 
