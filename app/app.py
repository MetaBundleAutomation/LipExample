import streamlit as st
from core.config import settings

st.set_page_config(
    page_title=settings.page_content.title,
    page_icon=settings.images.page_icon,
)

st.title(settings.page_content.header)
st.image(settings.images.page_icon, width=50)
