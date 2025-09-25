import { useState } from 'react'

import Dashboard from './pages/Dashboard'
import Animals from './pages/Animals'
import Workers from './pages/Workers'
import WorkerForm from './pages/addWorker'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import './App.css'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/Animals" element={<Animals />} />
        <Route path="/Workers" element={<Workers />} />
        <Route path="/worker/new" element={<WorkerForm />} />
      </Routes>
    </Router>
  );
}



export default App
