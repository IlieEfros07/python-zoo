import { useState } from 'react'

import Dashboard from './pages/Dashboard'
import Animals from './pages/Animals'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import './App.css'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/Animals" element={<Animals />} />
      </Routes>
    </Router>
  )
}



export default App
