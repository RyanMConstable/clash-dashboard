import {useParams } from 'react-router-dom';
import React, {useEffect, useState } from 'react';
import { PieChart, Pie, Cell, Tooltip, Legend } from 'recharts';
import "./ClanDashboard.css"

const COLORS = ['#8096a8', '#70d484'];

function ClanDashboard() {
  const { clantag } = useParams();
  const [clanData, setClanData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [clanname, setClanname] = useState('');



  useEffect(() => {
	  const fetchClanData = async () => {
		  try {
			  const response = await fetch(`/api/clandashboard?clantag=${clantag}`);
			  if (!response.ok) {
				  throw new Error('Failed to fetch clan data');
			  }
			  const data = await response.json();
			  setClanData(data.clanvalues);
			  setClanname(data.clanname);
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
if (!clanData) return <p>No clan data found.</p>;

const pieData = [
	{ name: 'Total attacks', value: (clanData.teamsize * clanData.attackspermember) - clanData.attacks },
	{ name: 'Attacks used', value: clanData.attacks }
];
const pieDataEnemyAttacks = [
	{ name: 'Total attacks', value: (clanData.teamsize * clanData.attackspermember) - clanData.enemyattacks },
	{ name: 'Attacks used', value: clanData.enemyattacks }
];
const pieDataStars = [
	{ name: 'Available Stars', value: (clanData.teamsize * 3) - clanData.stars },
	{ name: 'Stars Gained', value: clanData.stars }
];
const pieDataEnemyStars = [
	{ name: 'Available Stars', value: (clanData.teamsize * 3) - clanData.enemystars },
	{ name: 'Stars Gained', value: clanData.enemystars }
];
const pieDataDestruction = [
	{ name: 'Destruction Percentage', value: 100 - clanData.destructionpercentage },
	{ name: '', value: clanData.destructionpercentage }
];
const pieDataEnemyDestruction = [
	{ name: 'Destruction Percentage', value: 100 - clanData.enemydestructionpercentage },
	{ name: '', value: clanData.enemydestructionpercentage }
];

  return (
    <>
      <h1>{ clanname }</h1>
      <div class="attackusage">
	  <div class="chart">
          	<h2>Current War Attack Usage</h2>
	  	<PieChart width={400} height={300}>
	  		<Pie
	  			data={pieData}
	  			dataKey="value"
	  			nameKey="name"
	  			cx="50%"
	  			cy="50%"
	  			outerRadius={100}
	  			fill="#8884d8"
	  			label
	  		>
	  		{pieData.map((entry, index) => (
				<Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
			))}
	  		</Pie>
	  		<Tooltip />
	  		<Legend />
	  	</PieChart>
	  </div>
	  <div class="chart">
          	<h2>Enemy Current War Attack Usage</h2>
	  	<PieChart width={400} height={300}>
	  		<Pie
	  			data={pieDataEnemyAttacks}
	  			dataKey="value"
	  			nameKey="name"
	  			cx="50%"
	  			cy="50%"
	  			outerRadius={100}
	  			fill="#8884d8"
	  			label
	  		>
	  		{pieData.map((entry, index) => (
				<Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
			))}
	  		</Pie>
	  		<Tooltip />
	  		<Legend />
	  	</PieChart>
	  </div>
      </div>
      <div class="attackusage">
	  <div class="chart">
          	<h2>Current Stars</h2>
	  	<PieChart width={400} height={300}>
	  		<Pie
	  			data={pieDataStars}
	  			dataKey="value"
	  			nameKey="name"
	  			cx="50%"
	  			cy="50%"
	  			outerRadius={100}
	  			fill="#8884d8"
	  			label
	  		>
	  		{pieData.map((entry, index) => (
				<Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
			))}
	  		</Pie>
	  		<Tooltip />
	  		<Legend />
	  	</PieChart>
	  </div>
	  <div class="chart">
          	<h2>Enemy Current Stars</h2>
	  	<PieChart width={400} height={300}>
	  		<Pie
	  			data={pieDataEnemyStars}
	  			dataKey="value"
	  			nameKey="name"
	  			cx="50%"
	  			cy="50%"
	  			outerRadius={100}
	  			fill="#8884d8"
	  			label
	  		>
	  		{pieData.map((entry, index) => (
				<Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
			))}
	  		</Pie>
	  		<Tooltip />
	  		<Legend />
	  	</PieChart>
	  </div>
      </div>
      <div class="destruction">
	  <div class="chart">
          	<h2>Destruction Percentage</h2>
	  	<PieChart width={400} height={300}>
	  		<Pie
	  			data={pieDataDestruction}
	  			dataKey="value"
	  			nameKey="name"
	  			cx="50%"
	  			cy="50%"
	  			outerRadius={100}
	  			fill="#8884d8"
	  			label
	  		>
	  		{pieData.map((entry, index) => (
				<Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
			))}
	  		</Pie>
	  		<Tooltip />
	  		<Legend />
	  	</PieChart>
	  </div>
	  <div class="chart">
          	<h2>Destruction Percentage</h2>
	  	<PieChart width={400} height={300}>
	  		<Pie
	  			data={pieDataEnemyDestruction}
	  			dataKey="value"
	  			nameKey="name"
	  			cx="50%"
	  			cy="50%"
	  			outerRadius={100}
	  			fill="#8884d8"
	  			label
	  		>
	  		{pieData.map((entry, index) => (
				<Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
			))}
	  		</Pie>
	  		<Tooltip />
	  		<Legend />
	  	</PieChart>
	  </div>
      </div>
    </>
  )
}

export default ClanDashboard 
