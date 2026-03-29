from sqlalchemy.orm import Session
from ..models import models
from fastapi import Response, status

def create(db: Session, sandwich):
    db_sandwich = models.Sandwich(
        sandwich_name=sandwich.sandwich_name,
        price=sandwich.price
    )
    db.add(db_sandwich) [cite: 111]
    db.commit() [cite: 114]
    db.refresh(db_sandwich) [cite: 115]
    return db_sandwich [cite: 117]

def read_all(db: Session):
    return db.query(models.Sandwich).all() [cite: 120]

def read_one(db: Session, sandwich_id):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first() [cite: 132, 133]

def update(db: Session, sandwich_id, sandwich):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id) [cite: 148]
    update_data = sandwich.dict(exclude_unset=True) [cite: 160]
    db_sandwich.update(update_data, synchronize_session=False) [cite: 164]
    db.commit() [cite: 166]
    return db_sandwich.first() [cite: 167]

def delete(db: Session, sandwich_id):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id) [cite: 171]
    db_sandwich.delete(synchronize_session=False) [cite: 181]
    db.commit() [cite: 184]
    return Response(status_code=status.HTTP_204_NO_CONTENT) [cite: 186]