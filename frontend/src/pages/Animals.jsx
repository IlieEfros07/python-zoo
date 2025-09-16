import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { api } from "../services/api";

const Animals = () => {
  const [animals, setAnimals] = useState([]);
  const [filter, setFilter] = useState("");
  const [sortBy, setSortBy] = useState("name");

  useEffect(() => {
    const fetchAnimals = async () => {
      try {
        const data = await api.getAnimals();
        setAnimals(data);
      } catch (error) {
        console.error("Error fetching animals:", error);
      }
    };

    fetchAnimals();
  }, []);

  const filteredAnimals = animals.filter(
    (animal) =>
      animal.name.toLowerCase().includes(filter.toLowerCase()) ||
      animal.species.toLowerCase().includes(filter.toLowerCase())
  );

  const sortedAnimals = [...filteredAnimals].sort((a, b) => {
    if (a[sortBy] < b[sortBy]) return -1;
    if (a[sortBy] > b[sortBy]) return 1;
    return 0;
  });

  return (
    <div>
      <h1>Animals Management</h1>

      <div>
        <input
          type="text"
          placeholder="Filter animals..."
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
        />
        <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
          <option value="name">Name</option>
          <option value="species">Species</option>
          <option value="age">Age</option>
        </select>
        <Link to="/animals/new">Add New Animal</Link>
      </div>

      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Species</th>
            <th>Age</th>
            <th>Health Status</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {sortedAnimals.map((animal) => (
            <tr key={animal.id}>
              <td>{animal.name}</td>
              <td>{animal.species}</td>
              <td>{animal.age}</td>
              <td>{animal.isHealthy ? "Healthy" : "Sick"}</td>
              <td>
                <Link to={`/animals/${animal.id}`}>View</Link>
                <Link to={`/animals/${animal.id}/edit`}>Edit</Link>
                <button onClick={() => handleDelete(animal.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Animals;
