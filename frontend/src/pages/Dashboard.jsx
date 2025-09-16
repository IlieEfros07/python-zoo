import React from 'react';
import { NavLink } from 'react-router-dom';

const Dashboard = () => {
    return (
        <div className="dashboard">
            <h1>Dashboard</h1>
            <nav>
                <ul>
                    <li><NavLink to="/workers">Workers</NavLink></li>
                    <li><NavLink to="/exhibits">Exhibits</NavLink></li>
                    <li><NavLink to="/animals">Animals</NavLink></li>
                    <li><NavLink to="/animal-images">Animal Images</NavLink></li>
                    <li><NavLink to="/food-inventory">Food Inventory</NavLink></li>
                </ul>
            </nav>
        </div>
    );
};

export default Dashboard;
