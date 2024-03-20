from dataclasses import dataclass

@dataclass
class Image:
    name: str
    image_url: str | None = None
