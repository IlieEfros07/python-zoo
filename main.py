from fastapi import FastAPI, HTTPException
from db import init_db
import crud
import models

app = FastAPI()

init_db()

@app.get("/")
async def read_root():
  """
  return: dict -> Welcome message
  params: None
  description: Returns a welcome message for the Zoo Management System
  """
  return crud.root()

@app.post("/workers", response_model=models.WorkerOut)
async def create_worker(worker: models.WorkerIn):
  """
  return: WorkerOut -> Created worker object
  params: worker: WorkerIn - Worker data to create
  description: Creates a new worker in the system
  """
  try:
    return crud.addWorker(worker)
  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))

@app.get("/workers")
async def get_workers():
  """
  return: list[WorkerOut] -> List of all workers
  params: None
  description: Returns all workers in the system
  """
  try:
    return crud.getWorkers()
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@app.get("/workers/{worker_id}", response_model=models.WorkerOut)
async def get_worker(worker_id: int):
  """
  return: WorkerOut -> Worker object
  params: worker_id: int - ID of the worker to retrieve
  description: Returns a specific worker by ID
  """
  try:
    return crud.getWorkerById(worker_id)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.put("/workers/{worker_id}", response_model=models.WorkerOut)
async def update_worker(worker_id: int, worker: models.WorkerIn):
  """
  return: WorkerOut -> Updated worker object
  params: worker_id: int - ID of the worker to update
           worker: WorkerIn - Updated worker data
  description: Updates an existing worker
  """
  try:
    return crud.updateWorker(worker_id, worker)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.delete("/workers/{worker_id}")
async def delete_worker(worker_id: int):
  """
  return: dict -> Success message
  params: worker_id: int - ID of the worker to delete
  description: Deletes a worker from the system
  """
  try:
    return crud.deleteWorker(worker_id)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.get("/workers/role/{role}", response_model=list[models.WorkerOut])
async def get_workers_by_role(role: str):
  """
  return: list[WorkerOut] -> List of workers by role
  params: role: str - Role to filter by (keeper, cleaner, admin)
  description: Returns all workers with a specific role
  """
  try:
    return crud.getWorkersByRole(role)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.post("/exhibits", response_model=models.ExhibitOut)
async def create_exhibit(exhibit: models.ExhibitIn):
  """
  return: ExhibitOut -> Created exhibit object
  params: exhibit: ExhibitIn - Exhibit data to create
  description: Creates a new exhibit in the system
  """
  try:
    return crud.addExhibit(exhibit)
  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))

@app.get("/exhibits", response_model=list[models.ExhibitOut])
async def get_exhibits():
  """
  return: list[ExhibitOut] -> List of all exhibits
  params: None
  description: Returns all exhibits in the system
  """
  try:
    return crud.getExhibits()
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@app.get("/exhibits/{exhibit_id}", response_model=models.ExhibitOut)
async def get_exhibit(exhibit_id: int):
  """
  return: ExhibitOut -> Exhibit object
  params: exhibit_id: int - ID of the exhibit to retrieve
  description: Returns a specific exhibit by ID
  """
  try:
    return crud.getExhibitById(exhibit_id)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.put("/exhibits/{exhibit_id}", response_model=models.ExhibitOut)
async def update_exhibit(exhibit_id: int, exhibit: models.ExhibitIn):
  """
  return: ExhibitOut -> Updated exhibit object
  params: exhibit_id: int - ID of the exhibit to update
           exhibit: ExhibitIn - Updated exhibit data
  description: Updates an existing exhibit
  """
  try:
    return crud.updateExhibit(exhibit_id, exhibit)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.delete("/exhibits/{exhibit_id}")
async def delete_exhibit(exhibit_id: int):
  """
  return: dict -> Success message
  params: exhibit_id: int - ID of the exhibit to delete
  description: Deletes an exhibit from the system
  """
  try:
    return crud.deleteExhibit(exhibit_id)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.get("/exhibits/location/{location", response_model=list[models.ExhibitOut])
async def get_exhibits_by_location(location: str):
  """
  return: list[ExhibitOut] -> List of exhibits by location
  params: location: str - Location to filter by
  description: Returns all exhibits in a specific location
  """
  try:
    return crud.getExhibitsByLocation(location)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.post("/animals", response_model=models.AnimalOut)
async def create_animal(animal: models.AnimalIn):
  """
  return: AnimalOut -> Created animal object
  params: animal: AnimalIn - Animal data to create
  description: Creates a new animal in the system
  """
  try:
    return crud.addAnimal(animal)
  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))

@app.get("/animals", response_model=list[models.AnimalOut])
async def get_animals():
  """
  return: list[AnimalOut] -> List of all animals
  params: None
  description: Returns all animals in the system
  """
  try:
    return crud.getAnimals()
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@app.get("/animals/{animal_id}", response_model=models.AnimalOut)
async def get_animal(animal_id: int):
  """
  return: AnimalOut -> Animal object
  params: animal_id: int - ID of the animal to retrieve
  description: Returns a specific animal by ID
  """
  try:
    return crud.getAnimalById(animal_id)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.put("/animals/{animal_id}", response_model=models.AnimalOut)
async def update_animal(animal_id: int, animal: models.AnimalIn):
  """
  return: AnimalOut -> Updated animal object
  params: animal_id: int - ID of the animal to update
           animal: AnimalIn - Updated animal data
  description: Updates an existing animal
  """
  try:
    return crud.updateAnimal(animal_id, animal)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.delete("/animals/{animal_id}")
async def delete_animal(animal_id: int):
  """
  return: dict -> Success message
  params: animal_id: int - ID of the animal to delete
  description: Deletes an animal from the system
  """
  try:
    return crud.deleteAnimal(animal_id)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.get("/animals/species/{species}", response_model=list[models.AnimalOut])
async def get_animals_by_species(species: str):
  """
  return: list[AnimalOut] -> List of animals by species
  params: species: str - Species to filter by
  description: Returns all animals of a specific species
  """
  try:
    return crud.getAnimalsBySpecies(species)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.get("/animals/exhibit/{exhibit_id}", response_model=list[models.AnimalOut])
async def get_animals_by_exhibit(exhibit_id: int):
  """
  return: list[AnimalOut] -> List of animals in exhibit
  params: exhibit_id: int - ID of the exhibit to filter by
  description: Returns all animals in a specific exhibit
  """
  try:
    return crud.getAnimalsByExhibit(exhibit_id)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.get("/animals/healthy/{is_healthy}", response_model=list[models.AnimalOut])
async def get_animals_by_health(is_healthy: bool):
  """
  return: list[AnimalOut] -> List of animals by health status
  params: is_healthy: bool - Health status to filter by
  description: Returns all animals with a specific health status
  """
  try:
    return crud.getAnimalsByHealthStatus(is_healthy)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.post("/animal-images", response_model=models.AnimalImageOut)
async def create_animal_image(animal_image: models.AnimalImageIn):
  """
  return: AnimalImageOut -> Created animal image object
  params: animal_image: AnimalImageIn - Animal image data to create
  description: Adds an image for an animal
  """
  try:
    return crud.addAnimalImage(animal_image)
  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))

@app.get("/animal-images/animal/{animal_id}", response_model=list[models.AnimalImageOut])
async def get_animal_images_by_animal(animal_id: int):
  """
  return: list[AnimalImageOut] -> List of animal images
  params: animal_id: int - ID of the animal to get images for
  description: Returns all images for a specific animal
  """
  try:
    return crud.getAnimalImagesByAnimal(animal_id)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.delete("/animal-images/{image_id}")
async def delete_animal_image(image_id: int):
  """
  return: dict -> Success message
  params: image_id: int - ID of the image to delete
  description: Deletes an animal image from the system
  """
  try:
    return crud.deleteAnimalImage(image_id)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.post("/keeper-exhibits", response_model=models.KeeperExhibitOut)
async def assign_keeper_to_exhibit(keeper_exhibit: models.KeeperExhibitIn):
  """
  return: KeeperExhibitOut -> Created assignment object
  params: keeper_exhibit: KeeperExhibitIn - Assignment data to create
  description: Assigns a keeper to an exhibit
  """
  try:
    return crud.assignKeeperToExhibit(keeper_exhibit)
  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))

@app.get("/keeper-exhibits", response_model=list[models.KeeperExhibitOut])
async def get_keeper_exhibits():
  """
  return: list[KeeperExhibitOut] -> List of all keeper assignments
  params: None
  description: Returns all keeper-exhibit assignments
  """
  try:
    return crud.getKeeperAssignments()
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@app.get("/keeper-exhibits/keeper/{keeper_id}", response_model=list[models.ExhibitOut])
async def get_exhibits_by_keeper(keeper_id: int):
  """
  return: list[ExhibitOut] -> List of exhibits assigned to keeper
  params: keeper_id: int - ID of the keeper to filter by
  description: Returns all exhibits assigned to a specific keeper
  """
  try:
    return crud.getExhibitsByKeeper(keeper_id)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.get("/keeper-exhibits/exhibit/{exhibit_id}", response_model=list[models.WorkerOut])
async def get_keepers_by_exhibit(exhibit_id: int):
  """
  return: list[WorkerOut] -> List of keepers assigned to exhibit
  params: exhibit_id: int - ID of the exhibit to filter by
  description: Returns all keepers assigned to a specific exhibit
  """
  try:
    return crud.getKeepersByExhibit(exhibit_id)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.delete("/keeper-exhibits/{keeper_id}/{exhibit_id}")
async def delete_keeper_exhibit(keeper_id: int, exhibit_id: int):
  """
  return: dict -> Success message
  params: keeper_id: int - ID of the keeper
           exhibit_id: int - ID of the exhibit
  description: Removes a keeper assignment from an exhibit
  """
  try:
    return crud.deleteKeeperAssignment(keeper_id, exhibit_id)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.post("/food-inventory", response_model=models.FoodInventoryOut)
async def create_food_inventory(item: models.FoodInventoryIn):
  """
  return: FoodInventoryOut -> Created food item object
  params: item: FoodInventoryIn - Food item data to create
  description: Adds a new food item to inventory
  """
  try:
    return crud.addFoodItem(item)
  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))

@app.get("/food-inventory", response_model=list[models.FoodInventoryOut])
async def get_food_inventory():
  """
  return: list[FoodInventoryOut] -> List of all food items
  params: None
  description: Returns all food items in inventory
  """
  try:
    return crud.getFoodInventory()
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@app.get("/food-inventory/{item_id}", response_model=models.FoodInventoryOut)
async def get_food_item(item_id: int):
  """
  return: FoodInventoryOut -> Food item object
  params: item_id: int - ID of the food item to retrieve
  description: Returns a specific food item by ID
  """
  try:
    return crud.getFoodItemById(item_id)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.put("/food-inventory/{item_id}", response_model=models.FoodInventoryOut)
async def update_food_item(item_id: int, item: models.FoodInventoryIn):
  """
  return: FoodInventoryOut -> Updated food item object
  params: item_id: int - ID of the food item to update
           item: FoodInventoryIn - Updated food item data
  description: Updates an existing food item
  """
  try:
    return crud.updateFoodItem(item_id, item)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.delete("/food-inventory/{item_id}")
async def delete_food_item(item_id: int):
  """
  return: dict -> Success message
  params: item_id: int - ID of the food item to delete
  description: Deletes a food item from inventory
  """
  try:
    return crud.deleteFoodItem(item_id)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.get("/food-inventory/type/{type}", response_model=list[models.FoodInventoryOut])
async def get_food_items_by_type(type: str):
  """
  return: list[FoodInventoryOut] -> List of food items by type
  params: type: str - Type to filter by
  description: Returns all food items of a specific type
  """
  try:
    return crud.getFoodItemsByType(type)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.get("/food-inventory/low-stock/{threshold}", response_model=list[models.FoodInventoryOut])
async def get_food_items_low_stock(threshold: float):
  """
  return: list[FoodInventoryOut] -> List of low stock food items
  params: threshold: float - Quantity threshold for low stock
  description: Returns all food items with quantity below threshold
  """
  try:
    return crud.getFoodLowStock(threshold)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))