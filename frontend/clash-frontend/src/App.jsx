import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from "./pages/LandingPage";
import SignupPage from "./pages/SignupPage";
import LoginPage from "./pages/LoginPage";
import ClanDashboard from "./pages/ClanDashboard";

import './App.css'

function App() {
  return (
    <Router>
      <Routes>
	<Route path="/" element={<LandingPage />} />
	<Route path="/signup" element={<SignupPage />} />
	<Route path="/login" element={<LoginPage />} />
	<Route path="/clandashboard" element={<ClanDashboard />} />
	<Route path="/clandashboard/:clantag" element={<ClanDashboard />} />
      </Routes>
    </Router>
  )
}

export default App
