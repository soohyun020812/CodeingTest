from fastapi import APIRouter, HTTPException, Depends
from services.lock_service import acquire_lock, release_lock, get_lock_status

router = APIRouter()

@router.post("/lock")
def lock_file(project_id: str, file_id: str, user_id: str):
    success, message = acquire_lock(project_id, file_id, user_id)
    if not success:
        raise HTTPException(status_code=409, detail=message)
    return {"message": message}

@router.post("/unlock")
def unlock_file(project_id: str, file_id: str, user_id: str):
    success, message = release_lock(project_id, file_id, user_id)
    if not success:
        raise HTTPException(status_code=403, detail=message)
    return {"message": message}

@router.get("/status")
def status(project_id: str, file_id: str):
    return get_lock_status(project_id, file_id)

@router.get("/dummy")
def dummy_lock():
    return {"message": "This is a dummy file lock route."}

