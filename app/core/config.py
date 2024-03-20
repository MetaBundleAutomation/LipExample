from pydantic import BaseModel
from pydantic_settings import BaseSettings


class PageContent(BaseModel):
    title: str = "Meta Bundle Services"
    header: str = "Lip Reader"


class Images(BaseModel):
    page_icon: str = "./app/images/logo.jpg"


class Settings(BaseSettings):
    service_name: str = "Streamlit"
    # token: SecretStr
    images: Images = Images()
    page_content: PageContent = PageContent()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
