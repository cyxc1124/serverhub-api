from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.server import Server
from app.models.user import User
from app.schemas.server import ServerCreate, ServerRead, ServerUpdate

router = APIRouter(prefix="/servers", tags=["服务器管理"])


@router.get("/", response_model=list[ServerRead])
def list_servers(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.is_superuser:
        return db.query(Server).all()
    return db.query(Server).filter(Server.owner_id == current_user.id).all()


@router.post("/", response_model=ServerRead, status_code=201)
def create_server(
    payload: ServerCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    server = Server(**payload.model_dump(), owner_id=current_user.id)
    db.add(server)
    db.commit()
    db.refresh(server)
    return server


@router.get("/{server_id}", response_model=ServerRead)
def get_server(
    server_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    server = db.query(Server).filter(Server.id == server_id).first()
    if not server:
        raise HTTPException(status_code=404, detail="服务器不存在")
    if not current_user.is_superuser and server.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="权限不足")
    return server


@router.put("/{server_id}", response_model=ServerRead)
def update_server(
    server_id: int,
    payload: ServerUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    server = db.query(Server).filter(Server.id == server_id).first()
    if not server:
        raise HTTPException(status_code=404, detail="服务器不存在")
    if not current_user.is_superuser and server.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="权限不足")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(server, field, value)
    db.commit()
    db.refresh(server)
    return server


@router.delete("/{server_id}", status_code=204)
def delete_server(
    server_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    server = db.query(Server).filter(Server.id == server_id).first()
    if not server:
        raise HTTPException(status_code=404, detail="服务器不存在")
    if not current_user.is_superuser and server.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="权限不足")
    db.delete(server)
    db.commit()
