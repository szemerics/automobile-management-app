from odmantic import Model
from typing import List, Optional, Union
from datetime import datetime

class Movie(Model):
    # _id: str
    title: str
    plot: Optional[str] = None
    genres: Optional[List[str]] = None
    runtime: Optional[int] = None
    cast: Optional[List[str]] = None
    poster: Optional[str] = None
    fullplot: Optional[str] = None
    languages: Optional[List[str]] = None
    released: Optional[datetime] = None
    directors: Optional[List[str]] = None
    rated: Optional[str] = None
    lastupdated: Optional[str] = None
    year: Optional[Union[int, str]] = None
    type: Optional[str] = None
    countries: Optional[List[str]] = None
    num_mflix_comments: Optional[int] = None
    awards: Optional[dict] = None
    imdb: Optional[dict] = None
    tomatoes: Optional[dict] = None

    model_config = {
            "collection": "movies"
        }