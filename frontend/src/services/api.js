const API_URL = 'http://localhost:8000';

export const api = {
  // Workers
  getWorkers: () => fetch(`${API_URL}/workers`).then(res => res.json()),
  getworker: (id) => fetch(`${API_URL}/workers/${id}`).then(res => res.json()),
  createWorker: (data) => fetch(`${API_URL}/workers`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  }).then(res => res.json()),
  updateWorker: (id, data) => fetch(`${API_URL}/workers/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  }).then(res => res.json()),
  deleteWorker: (id) => fetch(`${API_URL}/workers/${id}`, {
    method: 'DELETE',
  }).then(res => res.json()),

  // Exhibits
  getExhibits: () => fetch(`${API_URL}/exhibits`).then(res => res.json()),
  getExhibit: (id) => fetch(`${API_URL}/exhibits/${id}`).then(res => res.json()),
  createExhibit: (data) => fetch(`${API_URL}/exhibits`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  }).then(res => res.json()),
  updateExhibit: (id, data) => fetch(`${API_URL}/exhibits/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  }).then(res => res.json()),
  deleteExhibit: (id) => fetch(`${API_URL}/exhibits/${id}`, {
    method: 'DELETE',
  }).then(res => res.json()),

  // Animals
  getAnimals: () => fetch(`${API_URL}/animals`).then(res => res.json()),
  getAnimal: (id) => fetch(`${API_URL}/animals/${id}`).then(res => res.json()),
  createAnimal: (data) => fetch(`${API_URL}/animals`, { 
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  }).then(res => res.json()),
  updateAnimal: (id, data) => fetch(`${API_URL}/animals/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  }).then(res => res.json()),
  deleteAnimal: (id) => fetch(`${API_URL}/animals/${id}`, {
    method: 'DELETE', 
  }).then(res => res.json()),
  getAnimalsByExhibit: (exhibit_id) => fetch(`${API_URL}/animals?exhibit_id=${exhibit_id}`).then(res => res.json()),
  getAnimalsBySpecies: (species) => fetch(`${API_URL}/animals?species=${species}`).then(res => res.json()),
  getAnimalByHealth: (health_status) => fetch(`${API_URL}/animals?health_status=${health_status}`).then(res => res.json()),

  // Animal Images
  getAnimalImages: (animal_id) => fetch(`${API_URL}/animals/${animal_id}/images`).then(res => res.json()),
  uploadAnimalImage: (animal_id, imageData) => {
    const formData = new FormData();
    formData.append('image', imageData);
    return fetch(`${API_URL}/animals/${animal_id}/images`, {
      method: 'POST',
      body: formData,
    }).then(res => res.json());
  },
  deleteAnimalImage: (animal_id, image_id) => fetch(`${API_URL}/animals/${animal_id}/images/${image_id}`, {
    method: 'DELETE',
  }).then(res => res.json()),

  // Keepers Exhibits Assignment
  getKeeperExhibitAssignment: () => fetch(`${API_URL}/keepers-exhibits`).then(res => res.json()),
  assignKeeperToExhibit: (data) => fetch(`${API_URL}/keepers-exhibits`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  }).then(res => res.json()),
  getKeeperByExhibit: (exhibit_id) => fetch(`${API_URL}/keepers-exhibits?exhibit_id=${exhibit_id}`).then(res => res.json()),
  getExhibitByKeeper: (worker_id) => fetch(`${API_URL}/keepers-exhibits?worker_id=${worker_id}`).then(res => res.json()),
  deleteKeeperAssignment: (id) => fetch(`${API_URL}/keepers-exhibits/${id}`, {
    method: 'DELETE',
  }).then(res => res.json()),

// Food inventory
  getFoodInventory: () => fetch(`${API_URL}/food-inventory`).then(res => res.json()),
  getFoodItem: (id) => fetch(`${API_URL}/food-inventory/${id}`).then(res => res.json()),
  createFoodItem: (data) => fetch(`${API_URL}/food-inventory`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  }).then(res => res.json()),
  updateFoodItem: (id, data) => fetch(`${API_URL}/food-inventory/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  }).then(res => res.json()),
  deleteFoodItem: (id) => fetch(`${API_URL}/food-inventory/${id}`, {
    method: 'DELETE',
  }).then(res => res.json()),
  getFoodItemsByType: (type) => fetch(`${API_URL}/food-inventory?type=${type}`).then(res => res.json()),
  getLowStockItems: (threshold) => fetch(`${API_URL}/food-inventory?low_stock=${threshold}`).then(res => res.json()),




}
