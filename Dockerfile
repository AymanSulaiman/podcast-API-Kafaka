FROM python:3.10-slim

# syntax=docker/dockerfile:1

COPY . .
RUN pip install pandas asyncio fastapi aiokafka pyarrow fastparquet
RUN pip install "uvicorn[standard]"
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]