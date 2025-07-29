from utils.redis import redis_client
import json

LOCK_PREFIX = "lock"

# 파일 락 획득

def acquire_lock(project_id: str, file_id: str, user_id: str):
    lock_key = f"{LOCK_PREFIX}:{project_id}:{file_id}"
    user_lock_key = f"user:{user_id}:lock:{project_id}"

    if redis_client.get(user_lock_key):
        return False, "User already locked another file in this project"

    existing = redis_client.get(lock_key)
    if existing:
        return False, "File is already locked"

    redis_client.set(lock_key, user_id)
    redis_client.set(user_lock_key, file_id)
    return True, "Lock acquired"

# 파일 락 해제

def release_lock(project_id: str, file_id: str, user_id: str):
    lock_key = f"{LOCK_PREFIX}:{project_id}:{file_id}"
    user_lock_key = f"user:{user_id}:lock:{project_id}"

    current = redis_client.get(lock_key)
    if current != user_id:
        return False, "You do not hold the lock"

    redis_client.delete(lock_key)
    redis_client.delete(user_lock_key)
    return True, "Lock released"

# 락 상태 확인

def get_lock_status(project_id: str, file_id: str):
    lock_key = f"{LOCK_PREFIX}:{project_id}:{file_id}"
    holder = redis_client.get(lock_key)
    return {"locked_by": holder if holder else None}
