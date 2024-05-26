from pydantic import BaseModel

class Track(BaseModel):
    title: str
    artist: str
    duration: int  # Duration in seconds
    file_path: str  # Path to the audio file on the server
