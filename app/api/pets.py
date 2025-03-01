from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.deps import get_current_user
from app.core.database import get_db
from app.models.user import User
from app.models.pet import Pet
from app.schemas.pet import PetCreate, PetUpdate, PetInDB
from app.services.ai_service import AIService

router = APIRouter(prefix="/pets", tags=["pets"])

@router.post("/", response_model=PetInDB)
async def create_pet(
    pet: PetCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_pet = Pet(**pet.dict(), last_modified_by=current_user.username)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

@router.get("/", response_model=List[PetInDB])
async def read_pets(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    pets = db.query(Pet).filter(Pet.user_id == current_user.id).offset(skip).limit(limit).all()
    return pets

@router.get("/{pet_id}", response_model=PetInDB)
async def read_pet(
    pet_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    pet = db.query(Pet).filter(Pet.id == pet_id, Pet.user_id == current_user.id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

@router.put("/{pet_id}", response_model=PetInDB)
async def update_pet(
    pet_id: int,
    pet_update: PetUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_pet = db.query(Pet).filter(Pet.id == pet_id, Pet.user_id == current_user.id).first()
    if not db_pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    update_data = pet_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_pet, field, value)
    
    db_pet.last_modified_by = current_user.username
    db.commit()
    db.refresh(db_pet)
    return db_pet

@router.delete("/{pet_id}")
async def delete_pet(
    pet_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_pet = db.query(Pet).filter(Pet.id == pet_id, Pet.user_id == current_user.id).first()
    if not db_pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    db.delete(db_pet)
    db.commit()
    return {"message": "Pet deleted successfully"}