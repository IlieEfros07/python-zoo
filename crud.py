from db import get_db_connection
import sqlite3
from fastapi import HTTPException
import models

def root():
  return {"message": "Zoo Management System"}

def addWorker(worker: models.WorkerIn):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO workers (first_name, last_name, role, notes, phone_number, created_at) VALUES (?, ?, ?, ?, ?, ?)",
             (worker.first_name, worker.last_name, worker.role, worker.notes, worker.phone_number, worker.created_at))
    worker_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return getWorkerById(worker_id)
  except sqlite3.Error as e:
    conn.close()
    raise HTTPException(status_code=400, detail=str(e))

def getWorkers():
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM workers")
    rows = cursor.fetchall()
    workers = [dict(row) for row in rows]
    conn.close()
    return workers
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in getWorkers: {str(e)}")

def getWorkerById(worker_id: int):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM workers WHERE id = ?", (worker_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
      raise HTTPException(status_code=404, detail="Worker not found")
    return dict(row)
  except HTTPException:
    raise
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error in getWorkerById: {str(e)}")

def updateWorker(worker_id: int, worker: models.WorkerIn):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE workers SET first_name = ?, last_name = ?, role = ?, notes = ?, phone_number = ? WHERE id = ?",
             (worker.first_name, worker.last_name, worker.role, worker.notes, worker.phone_number, worker_id))
    if cursor.rowcount == 0:
      conn.close()
      raise HTTPException(status_code=404, detail="Worker not found")
    conn.commit()
    conn.close()
    return getWorkerById(worker_id)
  except HTTPException:
    raise
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in updateWorker: {str(e)}")

def deleteWorker(worker_id: int):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM workers WHERE id = ?", (worker_id,))
    if cursor.rowcount == 0:
      conn.close()
      raise HTTPException(status_code=404, detail="Worker not found")
    conn.commit()
    conn.close()
    return {"message": "Worker deleted successfully"}
  except HTTPException:
    raise
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in deleteWorker: {str(e)}")

def getWorkersByRole(role: str):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM workers WHERE role = ?", (role,))  
    rows = cursor.fetchall()
    workers = [dict(row) for row in rows]
    conn.close()
    return workers
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in getWorkersByRole: {str(e)}")

def addExhibit(exhibit: models.ExhibitIn): 
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO exhibit (name, description, size_sqm, condition, location, created_at) VALUES (?, ?, ?, ?, ?, ?)",
             (exhibit.name, exhibit.description, exhibit.size_sqm, exhibit.condition, exhibit.location, exhibit.created_at))
    exhibit_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return getExhibitById(exhibit_id)
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=400, detail=f"Error in addExhibit: {str(e)}")

def getExhibits():
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM exhibit")
    rows = cursor.fetchall()
    exhibits = [dict(row) for row in rows]
    conn.close()
    return exhibits
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in getExhibits: {str(e)}")

def getExhibitById(exhibit_id: int):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM exhibit WHERE id = ?", (exhibit_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
      raise HTTPException(status_code=404, detail="Exhibit not found")
    return dict(row)
  except HTTPException:
    raise
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error in getExhibitById: {str(e)}")

def updateExhibit(exhibit_id: int, exhibit: models.ExhibitIn):  
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE exhibit SET name = ?, description = ?, size_sqm = ?, condition = ?, location = ? WHERE id = ?",
             (exhibit.name, exhibit.description, exhibit.size_sqm, exhibit.condition, exhibit.location, exhibit_id))
    if cursor.rowcount == 0:
      conn.close()
      raise HTTPException(status_code=404, detail="Exhibit not found")
    conn.commit()
    conn.close()
    return getExhibitById(exhibit_id)
  except HTTPException:
    raise
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in updateExhibit: {str(e)}")

def deleteExhibit(exhibit_id: int):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM exhibit WHERE id = ?", (exhibit_id,))
    if cursor.rowcount == 0:
      conn.close()
      raise HTTPException(status_code=404, detail="Exhibit not found")
    conn.commit()
    conn.close()
    return {"message": "Exhibit deleted successfully"}
  except HTTPException:
    raise
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in deleteExhibit: {str(e)}")

def getExhibitsByLocation(location: str):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM exhibit WHERE location = ?", (location,))
    rows = cursor.fetchall()
    exhibits = [dict(row) for row in rows]
    conn.close()
    return exhibits
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in getExhibitsByLocation: {str(e)}")

def addAnimal(animal: models.AnimalIn):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO animal (name, species, sex, date_of_birth, intake_date, description, weight_kg, height_cm, is_healthy, exhibit_id, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
             (animal.name, animal.species, animal.sex, animal.date_of_birth, animal.intake_date, animal.description, animal.weight_kg, animal.height_cm, animal.is_healthy, animal.exhibit_id, animal.created_at))
    animal_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return getAnimalById(animal_id)
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=400, detail=f"Error in addAnimal: {str(e)}")

def getAnimals():
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animal")
    rows = cursor.fetchall()
    animals = [dict(row) for row in rows]
    conn.close()
    return animals
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in getAnimals: {str(e)}")

def getAnimalById(animal_id: int):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animal WHERE id = ?", (animal_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
      raise HTTPException(status_code=404, detail="Animal not found")
    return dict(row)
  except HTTPException:
    raise
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error in getAnimalById: {str(e)}")

def updateAnimal(animal_id: int, animal: models.AnimalIn):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE animal SET name = ?, species = ?, sex = ?, date_of_birth = ?, intake_date = ?, description = ?, weight_kg = ?, height_cm = ?, is_healthy = ?, exhibit_id = ? WHERE id = ?",
             (animal.name, animal.species, animal.sex, animal.date_of_birth, animal.intake_date, animal.description, animal.weight_kg, animal.height_cm, animal.is_healthy, animal.exhibit_id, animal_id))
    if cursor.rowcount == 0:
      conn.close()
      raise HTTPException(status_code=404, detail="Animal not found")
    conn.commit()
    conn.close()
    return getAnimalById(animal_id)
  except HTTPException:
    raise
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in updateAnimal: {str(e)}")

def deleteAnimal(animal_id: int): 
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM animal WHERE id = ?", (animal_id,))
    if cursor.rowcount == 0:
      conn.close()
      raise HTTPException(status_code=404, detail="Animal not found")
    conn.commit()
    conn.close()
    return {"message": "Animal deleted successfully"}
  except HTTPException:
    raise
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in deleteAnimal: {str(e)}")

def getAnimalsBySpecies(species: str):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animal WHERE species = ?", (species,))
    rows = cursor.fetchall()
    animals = [dict(row) for row in rows]
    conn.close()
    return animals
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in getAnimalsBySpecies: {str(e)}")

def getAnimalsByHealthStatus(is_healthy: bool):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animal WHERE is_healthy = ?", (1 if is_healthy else 0,))
    rows = cursor.fetchall()
    animals = [dict(row) for row in rows]
    conn.close()
    return animals
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in getAnimalsByHealthStatus: {str(e)}")

def getAnimalsByExhibit(exhibit_id: int):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animal WHERE exhibit_id = ?", (exhibit_id,))
    rows = cursor.fetchall()
    animals = [dict(row) for row in rows]
    conn.close()
    return animals
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in getAnimalsByExhibit: {str(e)}")

def addAnimalImage(image: models.AnimalImageIn):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO animal_image (animal_id, image_url, caption, created_at) VALUES (?, ?, ?, ?)",
             (image.animal_id, image.image_url, image.caption, image.created_at))
    image_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return getAnimalImageById(image_id)
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=400, detail=f"Error in addAnimalImage: {str(e)}")

def getAnimalImageById(image_id: int):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animal_image WHERE id = ?", (image_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
      raise HTTPException(status_code=404, detail="Animal image not found")
    return dict(row)
  except HTTPException:
    raise
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error in getAnimalImageById: {str(e)}")

def getAnimalImages():
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animal_image")
    rows = cursor.fetchall()
    images = [dict(row) for row in rows]
    conn.close()
    return images
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in getAnimalImages: {str(e)}")

def getAnimalImagesByAnimal(animal_id: int):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animal_image WHERE animal_id = ?", (animal_id,))
    rows = cursor.fetchall()
    images = [dict(row) for row in rows]
    conn.close()
    return images
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in getAnimalImagesByAnimal: {str(e)}")

def deleteAnimalImage(image_id: int):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM animal_image WHERE id = ?", (image_id,))
    if cursor.rowcount == 0:
      conn.close()
      raise HTTPException(status_code=404, detail="Animal image not found")
    conn.commit()
    conn.close()
    return {"message": "Animal image deleted successfully"}
  except HTTPException:
    raise
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in deleteAnimalImage: {str(e)}")

def assignKeeperToExhibit(keeper_exhibit: models.KeeperExhibitIn):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO keeper_exhibit (keeper_id, exhibit_id, assigned_since) VALUES (?, ?, ?)",
             (keeper_exhibit.keeper_id, keeper_exhibit.exhibit_id, keeper_exhibit.assigned_since))
    conn.commit()
    conn.close()
    return {
      "keeper_id": keeper_exhibit.keeper_id,
      "exhibit_id": keeper_exhibit.exhibit_id,
      "assigned_since": keeper_exhibit.assigned_since
    }
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=400, detail=f"Error in assignKeeperToExhibit: {str(e)}")

def getExhibitsByKeeper(keeper_id: int):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
      SELECT e.* FROM exhibit e
      JOIN keeper_exhibit ke ON e.id = ke.exhibit_id
      WHERE ke.keeper_id = ?
    """, (keeper_id,))
    rows = cursor.fetchall()
    exhibits = [dict(row) for row in rows]
    conn.close()
    return exhibits
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in getExhibitsByKeeper: {str(e)}")

def getKeepersByExhibit(exhibit_id: int):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
      SELECT w.* FROM workers w
      JOIN keeper_exhibit ke ON w.id = ke.keeper_id
      WHERE ke.exhibit_id = ?
    """, (exhibit_id,))
    rows = cursor.fetchall()
    keepers = [dict(row) for row in rows]
    conn.close()
    return keepers
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in getKeepersByExhibit: {str(e)}")

def getKeeperAssignments():
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM keeper_exhibit")
    rows = cursor.fetchall()
    assignments = [dict(row) for row in rows]
    conn.close()
    return assignments
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in getKeeperAssignments: {str(e)}")

def deleteKeeperAssignment(keeper_id: int, exhibit_id: int):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM keeper_exhibit WHERE keeper_id = ? AND exhibit_id = ?", (keeper_id, exhibit_id))
    if cursor.rowcount == 0:
      conn.close()
      raise HTTPException(status_code=404, detail="Assignment not found")
    conn.commit()
    conn.close()
    return {"message": "Assignment deleted successfully"}
  except HTTPException:
    raise
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in deleteKeeperAssignment: {str(e)}")

def addFoodItem(item: models.FoodInventoryIn): 
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO food_inventory (name, quantity, unit, expiration_date, supplier, created_at) VALUES (?, ?, ?, ?, ?, ?)",
             (item.name, item.quantity, item.unit, item.expiration_date, item.supplier, item.created_at))
    item_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return getFoodItemById(item_id)
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=400, detail=f"Error in addFoodItem: {str(e)}")

def getFoodInventory():
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM food_inventory")
    rows = cursor.fetchall()
    items = [dict(row) for row in rows]
    conn.close()
    return items
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in getFoodInventory: {str(e)}")

def getFoodItemById(item_id: int):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM food_inventory WHERE id = ?", (item_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
      raise HTTPException(status_code=404, detail="Food item not found")
    return dict(row)
  except HTTPException:
    raise
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error in getFoodItemById: {str(e)}")

def updateFoodItem(item_id: int, item: models.FoodInventoryIn):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE food_inventory SET name = ?, quantity = ?, unit = ?, expiration_date = ?, supplier = ? WHERE id = ?",
             (item.name, item.quantity, item.unit, item.expiration_date, item.supplier, item_id))
    if cursor.rowcount == 0:
      conn.close()
      raise HTTPException(status_code=404, detail="Food item not found")
    conn.commit()
    conn.close()
    return getFoodItemById(item_id)
  except HTTPException:
    raise
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in updateFoodItem: {str(e)}")

def deleteFoodItem(item_id: int):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM food_inventory WHERE id = ?", (item_id,))
    if cursor.rowcount == 0:
      conn.close()
      raise HTTPException(status_code=404, detail="Food item not found")
    conn.commit()
    conn.close()
    return {"message": "Food item deleted successfully"}
  except HTTPException:
    raise
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in deleteFoodItem: {str(e)}")

def getFoodItemsByType(food_type: str):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM food_inventory WHERE type = ?", (food_type,))
    rows = cursor.fetchall()
    items = [dict(row) for row in rows]
    conn.close()
    return items
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in getFoodItemsByType: {str(e)}")

def getFoodLowStock(threshold: float):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM food_inventory WHERE quantity < ?", (threshold,))
    rows = cursor.fetchall()
    items = [dict(row) for row in rows]
    conn.close()
    return items
  except Exception as e:
    conn.close()
    raise HTTPException(status_code=500, detail=f"Error in getFoodLowStock: {str(e)}")