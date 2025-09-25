import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { api } from "../services/api";

const WorkerForm = ({ editMode = false }) => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    role: "keeper",
    phone_number: "",
    notes: "",
  });

  useEffect(() => {
    if (editMode && id) {
      const fetchWorker = async () => {
        try {
          const worker = await api.getWorker(id);
          setFormData({
            first_name: worker.first_name || "",
            last_name: worker.last_name || "",
            role: worker.role || "keeper",
            phone_number: worker.phone_number || "",
            notes: worker.notes || "",
          });
        } catch (error) {
          console.error("Error fetching worker:", error);
        }
      };
      fetchWorker();
    }
  }, [editMode, id]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editMode) {
        await api.updateWorker(id, formData);
      } else {
        await api.createWorker(formData);
      }
      navigate("/workers");
    } catch (error) {
      console.error("Error saving worker:", error);
      alert("Error saving worker: " + error.message);
    }
  };

  return (
    <div>
      <h1>{editMode ? "Edit Worker" : "Add New Worker"}</h1>

      <form onSubmit={handleSubmit}>
        <div>
          <label>First Name:</label>
          <input
            type="text"
            name="first_name"
            value={formData.first_name}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Last Name:</label>
          <input
            type="text"
            name="last_name"
            value={formData.last_name}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Role:</label>
          <select name="role" value={formData.role} onChange={handleChange}>
            <option value="keeper">Keeper</option>
            <option value="cleaner">Cleaner</option>
            <option value="admin">Admin</option>
          </select>
        </div>

        <div>
          <label>Phone Number:</label>
          <input
            type="tel"
            name="phone_number"
            value={formData.phone_number}
            onChange={handleChange}
            placeholder="+1234567890"
          />
        </div>

        <div>
          <label>Notes:</label>
          <textarea
            name="notes"
            value={formData.notes}
            onChange={handleChange}
            rows={4}
            placeholder="Specializes in reptiles, etc."
          />
        </div>

        <button type="submit">{editMode ? "Update" : "Create"} Worker</button>
        <button type="button" onClick={() => navigate("/workers")}>
          Cancel
        </button>
      </form>
    </div>
  );
};

export default WorkerForm;
