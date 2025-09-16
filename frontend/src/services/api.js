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







}
