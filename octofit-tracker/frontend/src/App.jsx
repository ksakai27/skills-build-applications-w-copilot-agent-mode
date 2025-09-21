import React from 'react'
import { Routes, Route, NavLink } from 'react-router-dom'
import Activities from './components/Activities.jsx'
import Leaderboard from './components/Leaderboard.jsx'
import Teams from './components/Teams.jsx'
import Users from './components/Users.jsx'
import Workouts from './components/Workouts.jsx'
import './App.css'

function getApiBase() {
  const name = process.env.REACT_APP_CODESPACE_NAME
  if (name) return `https://${name}-8000.app.github.dev`
  return 'http://localhost:8000'
}

export default function App() {
  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
        <div className="container">
          <NavLink className="navbar-brand logo-left" to="/">
            <img src="/docs/octofitapp-small.png" alt="Octofit" className="small-logo" />
            <span>Octofit</span>
          </NavLink>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav">
            <span className="navbar-toggler-icon" />
          </button>
          <div className="text-white ms-3 small api-badge">API: {getApiBase()}</div>
          <div className="collapse navbar-collapse" id="mainNav">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item"><NavLink className="nav-link" to="/activities">Activities</NavLink></li>
              <li className="nav-item"><NavLink className="nav-link" to="/workouts">Workouts</NavLink></li>
              <li className="nav-item"><NavLink className="nav-link" to="/teams">Teams</NavLink></li>
              <li className="nav-item"><NavLink className="nav-link" to="/users">Users</NavLink></li>
              <li className="nav-item"><NavLink className="nav-link" to="/leaderboard">Leaderboard</NavLink></li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="container mt-4 app-container">
        <Routes>
          <Route path="/activities" element={<Activities/>} />
          <Route path="/workouts" element={<Workouts/>} />
          <Route path="/teams" element={<Teams/>} />
          <Route path="/users" element={<Users/>} />
          <Route path="/leaderboard" element={<Leaderboard/>} />
          <Route path="/" element={<div className="card p-4"><h2>Welcome to Octofit Tracker</h2><p className="lead">Use the navigation to view data from the backend.</p></div>} />
        </Routes>
      </div>
    </div>
  )
}
