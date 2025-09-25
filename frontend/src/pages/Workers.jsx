import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { api } from "../services/api";

const Workers = () => {
  const [workers, setWorkers] = useState([]);
  const [filter, setFilter] = useState("");
  const [sortBy, setSortBy] = useState("first_name");
  const [roleFilter, setRoleFilter] = useState("all");

  useEffect(() => {
    const fetchWorkers = async () => {
      try {
        const data = await api.getWorkers();
        setWorkers(data);
      } catch (error) {
        console.error("Error fetching workers:", error);
      }
    };

    fetchWorkers();
  }, []);

  const filteredWorkers = workers.filter(
    (worker) =>
      (worker.first_name?.toLowerCase().includes(filter.toLowerCase()) ||
        worker.last_name?.toLowerCase().includes(filter.toLowerCase()) ||
        worker.role?.toLowerCase().includes(filter.toLowerCase())) &&
      (roleFilter === "all" || worker.role === roleFilter)
  );

  const sortedWorkers = [...filteredWorkers].sort((a, b) => {
    if (sortBy === "name") {
      const nameA = `${a.first_name} ${a.last_name}`.toLowerCase();
      const nameB = `${b.first_name} ${b.last_name}`.toLowerCase();
      if (nameA < nameB) return -1;
      if (nameA > nameB) return 1;
      return 0;
    }
    if (a[sortBy] < b[sortBy]) return -1;
    if (a[sortBy] > b[sortBy]) return 1;
    return 0;
  });

  const handleDelete = async (workerId) => {
    if (window.confirm("Are you sure you want to delete this worker?")) {
      try {
        await api.deleteWorker(workerId);
        setWorkers(workers.filter((worker) => worker.id !== workerId));
      } catch (error) {
        console.error("Error deleting worker:", error);
      }
    }
  };

  return (
    <div>
      <h1>Workers</h1>

      <div>
        <input
          type="text"
          placeholder="Filter workers..."
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
        />
        <select
          value={roleFilter}
          onChange={(e) => setRoleFilter(e.target.value)}
        >
          <option value="all">All Roles</option>
          <option value="keeper">Keeper</option>
          <option value="cleaner">Cleaner</option>
          <option value="admin">Admin</option>
        </select>
        <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
          <option value="name">Name</option>
          <option value="first_name">First Name</option>
          <option value="last_name">Last Name</option>
          <option value="role">Role</option>
        </select>
        <Link to="/worker/new">Add New Worker</Link>
      </div>

      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Role</th>
            <th>Phone Number</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {sortedWorkers.map((worker) => (
            <tr key={worker.id}>
              <td>
                {worker.first_name} {worker.last_name}
              </td>
              <td>{worker.role}</td>
              <td>{worker.phone_number || "N/A"}</td>
              <td>
                <Link to={`/worker/${worker.id}`}>View</Link>
                <Link to={`/worker/${worker.id}/edit`}>Edit</Link>
                <button onClick={() => handleDelete(worker.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Workers;
