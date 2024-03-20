FROM python:3.10-slim

WORKDIR /app

ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONDONTWRITEBYTEapp 1
ENV PYTHONUNBUFFERED True
ENV PYTHONBUFFERED 1
ENV PYTHONPATH=/app

RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./app ./app

EXPOSE 8080
CMD ["streamlit", "run", "app/app.py", "--server.port", "8080"]
