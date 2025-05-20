import { Link } from 'react-router-dom';
import './LandingPage.css'

export default function LandingPage() {
  return (
    <>
      <div className="landing-container">
	  <h1 className="landing-title">Clash-Dashboard</h1>
	  <div className="landing-buttons">
	    <Link to="/login" className="landing-button">Login</Link>
	    <Link to="/signup" className="landing-button">Sign Up</Link>
	  </div>
      </div>
    </>
  );
}
