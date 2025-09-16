from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

#  ---------- Workers --------- 
class WorkerIn(BaseModel):
    first_name: str
    last_name: str
    role: str = Field(..., pattern="^(keeper|cleaner|admin)$")
    notes: Optional[str] = None
    phone_number: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)

class WorkerOut(WorkerIn):
    id: int
    
#  ---------- Exhibits --------- 
class ExhibitIn(BaseModel):
    name: str
    description: Optional[str] = None
    size_sqm: Optional[float] = None
    condition: Optional[str] = None
    location: str
    created_at: datetime = Field(default_factory=datetime.now)
    
class ExhibitOut(ExhibitIn):
    id: int
    
#  ---------- Animals --------- 
class AnimalIn(BaseModel):
    name: str
    species: str
    sex: str = Field("unknown", pattern="^(male|female|unknown)$")
    date_of_birth: Optional[datetime] = None
    intake_date: Optional[datetime] = None
    description: Optional[str] = None
    weight_kg: Optional[float] = None
    height_cm: Optional[float] = None
    is_healthy: bool = True
    exhibit_id: int
    created_at: datetime = Field(default_factory=datetime.now)
    
class AnimalOut(AnimalIn):
    id: int
    
#  ---------- Animal Images --------- 
class AnimalImageIn(BaseModel):
    animal_id: int
    image_url: str
    caption: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)
    
class AnimalImageOut(AnimalImageIn):
    id: int

#  ---------- Keeper Exhibit --------- 
class KeeperExhibitIn(BaseModel):
    keeper_id: int
    exhibit_id: int
    assigned_since: Optional[datetime] = None
    
class KeeperExhibitOut(KeeperExhibitIn):
    pass

#  ---------- Food Inventory --------- 
class FoodInventoryIn(BaseModel):
    name: str
    quantity: float = 0.0
    unit: str = Field(..., pattern="^(kg|g|l|ml|pieces)$")
    type: Optional[str] = None
    notes: Optional[str] = None
    vendor: Optional[str] = None
    purchase_price_per_unit: Optional[float] = None
    created_at: datetime = Field(default_factory=datetime.now)
    
class FoodInventoryOut(FoodInventoryIn):
    id: int