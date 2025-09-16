import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { api } from "../services/api";

const AnimalForm = ({ editMode = false }) => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    name: "",
    species: "",
    age: "",
    isHealthy: true,
    exhibitId: "",
  });

  useEffect(() => {
    if (editMode && id) {
      const fetchAnimal = async () => {
        try {
          const animal = await api.getAnimal(id);
          setFormData({
            name: animal.name,
            species: animal.species,
            age: animal.age,
            isHealthy: animal.isHealthy,
            exhibitId: animal.exhibitId,
          });
        } catch (error) {
          console.error("Error fetching animal:", error);
        }
      };
      fetchAnimal();
    }
  }, [editMode, id]);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editMode) {
        await api.updateAnimal(id, formData);
      } else {
        await api.createAnimal(formData);
      }
      navigate("/animals");
    } catch (error) {
      console.error("Error saving animal:", error);
    }
  };

  return (
    <div>
      <h1>{editMode ? "Edit Animal" : "Add New Animal"}</h1>

      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Species:</label>
          <input
            type="text"
            name="species"
            value={formData.species}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Age:</label>
          <input
            type="number"
            name="age"
            value={formData.age}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Healthy:</label>
          <input
            type="checkbox"
            name="isHealthy"
            checked={formData.isHealthy}
            onChange={handleChange}
          />
        </div>

        <div>
          <label>Exhibit ID:</label>
          <input
            type="number"
            name="exhibitId"
            value={formData.exhibitId}
            onChange={handleChange}
          />
        </div>

        <button type="submit">{editMode ? "Update" : "Create"} Animal</button>
        <button type="button" onClick={() => navigate("/animals")}>
          Cancel
        </button>
      </form>
    </div>
  );
};

export default AnimalForm;
