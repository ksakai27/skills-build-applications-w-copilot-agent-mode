import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import App from './App.jsx'
import 'bootstrap/dist/css/bootstrap.min.css'

// Log the API base used by the app (helps debugging codespace-based endpoints)
const REACT_APP_CODESPACE_NAME = process.env.REACT_APP_CODESPACE_NAME
const API_BASE = REACT_APP_CODESPACE_NAME ? `https://${REACT_APP_CODESPACE_NAME}-8000.app.github.dev` : 'http://localhost:8000'
console.log('Frontend starting — API base:', API_BASE)

const root = createRoot(document.getElementById('root'))
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
)
