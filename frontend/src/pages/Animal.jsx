import { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import { api } from "../services/api";

const AnimalDetail = () => {
  const { id } = useParams();
  const [animal, setAnimal] = useState(null);
  const [images, setImages] = useState([]);

  useEffect(() => {
    const fetchAnimalData = async () => {
      try {
        const [animalData, imageData] = await Promise.all([
          api.getAnimal(id),
          api.getAnimalImages(id),
        ]);
        setAnimal(animalData);
        setImages(imageData);
      } catch (error) {
        console.error("Error fetching animal details:", error);
      }
    };

    fetchAnimalData();
  }, [id]);

  if (!animal) return <div>Loading...</div>;

  return (
    <div>
      <h1>{animal.name}</h1>
      <p>Species: {animal.species}</p>
      <p>Age: {animal.age}</p>
      <p>Health Status: {animal.isHealthy ? "Healthy" : "Sick"}</p>
      <p>Exhibit: {animal.exhibitId}</p>



      <h2>Images</h2>
      {images.length > 0 ? (
        <div>
          {images.map((image) => (
            <img
              key={image.id}
              src={image.imageUrl}
              alt={animal.name}
              style={{ maxWidth: "200px" }}
            />
          ))}
        </div>
      ) : (
        <p>No images available</p>
      )}

      <div>
        <Link to={`/animals/${id}/edit`}>Edit Animal</Link>
        <Link to="/animals">Back to Animals</Link>
      </div>
    </div>
  );
};

export default AnimalDetail;
