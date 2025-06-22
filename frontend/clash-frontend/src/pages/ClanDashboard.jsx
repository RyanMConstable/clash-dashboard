import {useParams } from 'react-router-dom';
import React, {useEffect, useState } from 'react';
import { PieChart, Pie, Cell, Tooltip, Legend } from 'recharts';
import "./ClanDashboard.css"
import { useReactTable, getCoreRowModel, flexRender, getFilteredRowModel, getSortedRowModel} from '@tanstack/react-table';
import EloTable from "./EloTable";

const tableHeaders = ["Name", "Elo", "Total Stars", "Destruction %", "3 Stars", "2 Stars", "1 Stars", "0 Stars", "Missed Attacks", "Total Attacks"]
const COLORS = ['#8096a8', '#70d484'];
const ENEMYCOLORS = ['#8096a8', '#c22f36'];

function ClanDashboard() {
  const { clantag } = useParams();
  const [clanData, setClanData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [clanname, setClanname] = useState('');
  const [clanmemberelo, setClanmemberelo] = useState('');
  const [clanimage, setClanImage] = useState('');
  const [warstatus, setWarStatus] = useState('');
  const [warresult, setWarResult] = useState('');



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
			  setClanmemberelo(data.clanmemberattacks);
			  setClanImage(data.clanbadge);
			  setWarStatus(data.warstatus);
			  if (data.clanvalues === null) {
				  setError("Clan Values Empty")
			  } else {
				  if (warresult != "inWar") {
					  if (data.clanvalues.stars > data.clanvalues.enemystars) {
						  setWarResult(<span style={{ color: 'green' }}>WIN</span>)
					  } else if (data.clanvalues.stars < data.clanvalues.enemystars) {
						  setWarResult(<span style={{ color: 'red' }}>WIN</span>)
					  } else {
						  setWarResult(<span style={{ color: 'green' }}>WIN</span>)
					  }
				  }
			  }
			  console.log("Set data")
			  console.log(data)
		  } catch (err) {
			  console.log("Setting error")
			  setError(err.message);
		  } finally {
			  console.log("Loading set to false")
			  setLoading(false);
		  }
	  };

	  fetchClanData();
  }, [clantag]);

console.log("Error")
console.log(error)
if (loading) return <p>Loading clan data...</p>;

let pieData = [];
let pieDataEnemyAttacks = [];
let pieDataStars = [];
let pieDataEnemyStars = [];
let pieDataDestruction = [];
let pieDataEnemyDestruction = [];

if (!error) {
	console.log("Setting pie data")

	pieData = [
		{ name: 'Total attacks', value: (clanData.teamsize * clanData.attackspermember) - clanData.attacks },
		{ name: 'Attacks used', value: clanData.attacks }
	];
	pieDataEnemyAttacks = [
		{ name: 'Total attacks', value: (clanData.teamsize * clanData.attackspermember) - clanData.enemyattacks },
		{ name: 'Attacks used', value: clanData.enemyattacks }
	];
	pieDataStars = [
		{ name: 'Available Stars', value: (clanData.teamsize * 3) - clanData.stars },
		{ name: 'Stars Gained', value: clanData.stars }
	];
	pieDataEnemyStars = [
		{ name: 'Available Stars', value: (clanData.teamsize * 3) - clanData.enemystars },
		{ name: 'Stars Gained', value: clanData.enemystars }
	];
	pieDataDestruction = [
		{ name: 'Intact', value: 100 - clanData.destructionpercentage },
		{ name: 'Dmg', value: clanData.destructionpercentage }
	];
	pieDataEnemyDestruction = [
		{ name: 'Intact', value: 100 - clanData.enemydestructionpercentage },
		{ name: 'Dmg', value: clanData.enemydestructionpercentage }
	];
}

console.log(clanimage)
if (!error) {
  return (
    <>
      <div class="clanname">
	<img src={clanimage} />
        <h1>{ clanname }</h1>
	<img src={clanimage} />
      </div>

      <div className="dashboard-container">

      <div class="attackusage">
      <div class="chart">
      {warstatus === "inWar" ? (<h1>Current War</h1>) : (<h1>War Results<br/> {warresult}</h1>)}
	  </div>
	  <div class="chart">
	  <h2>Attack usage</h2>
	  <div class="attack-usage-container">
	  	<PieChart width={150} height={100}>
	  		<Pie
	  			data={pieData}
	  			dataKey="value"
	  			nameKey="name"
	  			cx="50%"
	  			cy="50%"
	  			outerRadius={15}
	  			fill="#8884d8"
	  			label
	  		>
	  		{pieData.map((entry, index) => (
				<Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
			))}
	  		</Pie>
	  		<Tooltip />
	  	</PieChart>
	  	<PieChart width={150} height={100}>
	  		<Pie
	  			data={pieDataEnemyAttacks}
	  			dataKey="value"
	  			nameKey="name"
	  			cx="50%"
	  			cy="50%"
	  			outerRadius={15}
	  			fill="#8884d8"
	  			label
	  		>
	  		{pieData.map((entry, index) => (
				<Cell key={`cell-${index}`} fill={ENEMYCOLORS[index % ENEMYCOLORS.length]} />
			))}
	  		</Pie>
	  		<Tooltip />
	  	</PieChart>
	  </div>
	  </div>
	  <div class="chart">
          <h2>Current Stars</h2>
	  <div className="attack-usage-container">
	  	<PieChart width={150} height={100}>
	  		<Pie
	  			data={pieDataStars}
	  			dataKey="value"
	  			nameKey="name"
	  			cx="50%"
	  			cy="50%"
	  			outerRadius={15}
	  			fill="#8884d8"
	  			label
	  		>
	  		{pieData.map((entry, index) => (
				<Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
			))}
	  		</Pie>
	  		<Tooltip />
	  	</PieChart>
	  	<PieChart width={150} height={100}>
	  		<Pie
	  			data={pieDataEnemyStars}
	  			dataKey="value"
	  			nameKey="name"
	  			cx="50%"
	  			cy="50%"
	  			outerRadius={15}
	  			fill="#8884d8"
	  			label
	  		>
	  		{pieData.map((entry, index) => (
				<Cell key={`cell-${index}`} fill={ENEMYCOLORS[index % ENEMYCOLORS.length]} />
			))}
	  		</Pie>
	  		<Tooltip />
	  	</PieChart>
	  </div>
	  </div>
	  <div class="chart">
          <h2>Destruction Percentage</h2>
	  <div className="attack-usage-container">
	  	<PieChart width={150} height={100}>
	  		<Pie
	  			data={pieDataDestruction}
	  			dataKey="value"
	  			nameKey="name"
	  			cx="50%"
	  			cy="50%"
	  			outerRadius={15}
	  			fill="#8884d8"
	  			label
	  		>
	  		{pieData.map((entry, index) => (
				<Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
			))}
	  		</Pie>
	  		<Tooltip />
	  	</PieChart>
	  	<PieChart width={150} height={100}>
	  		<Pie
	  			data={pieDataEnemyDestruction}
	  			dataKey="value"
	  			nameKey="name"
	  			cx="50%"
	  			cy="50%"
	  			outerRadius={15}
	  			fill="#8884d8"
	  			label
	  		>
	  		{pieData.map((entry, index) => (
				<Cell key={`cell-${index}`} fill={ENEMYCOLORS[index % ENEMYCOLORS.length]} />
			))}
	  		</Pie>
	  		<Tooltip />
	  	</PieChart>
	  </div>
	  </div>
      </div>
     
      <div className="elo-table-container">
          <EloTable clanmemberelo={clanmemberelo} />	
      </div>
      </div>

    </>
  ) 
}

if (error) {
  return (
    <>
      <div class="clanname">
	<img src={ clanimage } />
        <h1>{ clanname }</h1>
	<img src={ clanimage } />
      </div>

      <div class="attackusage">
	  <h1>No clan war data exists</h1>
      </div>
    </>
  ) 
}
}


export default ClanDashboard 
