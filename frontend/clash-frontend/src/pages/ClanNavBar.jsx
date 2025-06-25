import React, { useState } from 'react';
import './ClanNavBar.css';

const ClanNavBar = () => {
  const [searchTerm, setSearchTerm] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Searching for clan:', searchTerm);
    // Add your search logic here
  };

  return (
    <div className="sticky-nav">
      <p>Add Clan</p>
      <form onSubmit={handleSubmit} style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
        <input
          type="text"
          placeholder="Search for clan"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        <button type="submit">Search</button>
      </form>
    </div>
  );
};

export default ClanNavBar;
