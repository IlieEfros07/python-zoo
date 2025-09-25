import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../services/api";

const Dashboard = () => {
  const [stats, setStats] = useState({
    totalAnimals: 0,
    totalExhibits: 0,
    totalWorkers: 0,
    healthyAnimals: 0,
    sickAnimals: 0,
  });
  const [lowStockItems, setLowStockItems] = useState([]);
  const [recentActivity, setRecentActivity] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Get all data needed for dashboard
        const [animals, exhibits, workers, lowStock] = await Promise.all([
          api.getAnimals(),
          api.getExhibits(),
          api.getWorkers(),
          api.getLowStockItems(10), // Threshold of 10
        ]);

        // Calculate stats
        const healthyAnimals = animals.filter(
          (animal) => animal.isHealthy
        ).length;

        setStats({
          totalAnimals: animals.length,
          totalExhibits: exhibits.length,
          totalWorkers: workers.length,
          healthyAnimals,
          sickAnimals: animals.length - healthyAnimals,
        });

        setLowStockItems(lowStock);

        // Simple recent activity (in a real app, you'd have a dedicated activity endpoint)
        const activity = [
          {
            type: "Animal",
            action: "Added",
            name: "New Lion",
            time: "2 hours ago",
          },
          {
            type: "Exhibit",
            action: "Updated",
            name: "Savannah Exhibit",
            time: "5 hours ago",
          },
          {
            type: "Worker",
            action: "Added",
            name: "John Doe",
            time: "1 day ago",
          },
        ];
        setRecentActivity(activity);
      } catch (error) {
        console.error("Error fetching dashboard data:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>

      <h2>Key Metrics</h2>
      <div>
        <p>Total Animals: {stats.totalAnimals}</p>
        <p>Total Exhibits: {stats.totalExhibits}</p>
        <p>Total Workers: {stats.totalWorkers}</p>
        <p>Healthy Animals: {stats.healthyAnimals}</p>
        <p>Sick Animals: {stats.sickAnimals}</p>
      </div>

      <h2>Low Stock Alerts</h2>
      {lowStockItems.length > 0 ? (
        <ul>
          {lowStockItems.map((item) => (
            <li key={item.id}>
              {item.name} - {item.quantity} left
            </li>
          ))}
        </ul>
      ) : (
        <p>No low stock items</p>
      )}

      <h2>Recent Activity</h2>
      <ul>
        {recentActivity.map((activity, index) => (
          <li key={index}>
            {activity.type} {activity.action}: {activity.name} ({activity.time})
          </li>
        ))}
      </ul>

      <h2>Quick Actions</h2>
      <div>
        <button onClick={() => navigate("/animals")}>Animals</button>
        <button onClick={() => navigate("/exhibits")}>Exhibits</button>
        <button onClick={() => navigate("/Workers")}>Workers</button>
        <button onClick={() => navigate("/inventory")}>Check Inventory</button>
      </div>
    </div>
  );
};

export default Dashboard;
