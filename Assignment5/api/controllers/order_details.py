from sqlalchemy.orm import Session
from ..models import models
from fastapi import Response, status

def create(db: Session, order_detail):
    db_detail = models.OrderDetail(
        order_id=order_detail.order_id,
        sandwich_id=order_detail.sandwich_id,
        amount=order_detail.amount
    )
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail

def read_all(db: Session):
    return db.query(models.OrderDetail).all()

def read_one(db: Session, detail_id):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id).first()

def update(db: Session, detail_id, order_detail):
    query = db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id)
    update_data = order_detail.dict(exclude_unset=True)
    query.update(update_data, synchronize_session=False)
    db.commit()
    return query.first()

def delete(db: Session, detail_id):
    query = db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id)
    query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)