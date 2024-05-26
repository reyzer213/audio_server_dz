from fastapi import APIRouter, HTTPException, File, UploadFile
from app.models import Track

router = APIRouter()

@router.get("/tracks")
async def get_all_tracks():
    # Return all tracks
    pass

@router.get("/tracks/{track_id}")
async def get_track(track_id: int):
    # Return details of a specific track
    pass

@router.post("/tracks")
async def upload_track(track: Track, file: UploadFile = File(...)):
    # Upload a new track
    pass

@router.put("/tracks/{track_id}")
async def update_track(track_id: int, track: Track):
    # Update details of a track
    pass

@router.delete("/tracks/{track_id}")
async def delete_track(track_id: int):
    # Delete a track
    pass
