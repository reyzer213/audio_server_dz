from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

tracks = []  # Список для зберігання треків

class Track:
    def __init__(self, title: str, artist: str, duration: int):
        self.title = title
        self.artist = artist
        self.duration = duration

@app.get("/tracks", response_class=HTMLResponse)
async def get_tracks():
    return templates.TemplateResponse("tracks.html", {"request": None, "tracks": tracks})

@app.get("/track/{track_id}", response_class=HTMLResponse)
async def get_track(track_id: int):
    # Знайдемо трек з вказаним ідентифікатором (індексом у списку)
    try:
        track = tracks[track_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Track not found")
    return templates.TemplateResponse("track.html", {"request": None, "track": track})

@app.post("/tracks")
async def add_track(title: str, artist: str, duration: int):
    new_track = Track(title=title, artist=artist, duration=duration)
    tracks.append(new_track)
    return {"message": "Track added successfully"}

@app.put("/track/{track_id}")
async def update_track(track_id: int, title: str, artist: str, duration: int):
    try:
        track = tracks[track_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Track not found")
    
    track.title = title
    track.artist = artist
    track.duration = duration
    
    return {"message": "Track updated successfully"}

@app.delete("/track/{track_id}")
async def delete_track(track_id: int):
    try:
        del tracks[track_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Track not found")
    return {"message": "Track deleted successfully"}
