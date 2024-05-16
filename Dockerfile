# Start with the FastAPI base image
FROM python
WORKDIR /Evaldevops
COPY ..
RUN pip install --no-cache-dir firebase-admin pydantic
EXPOSE 5000
CMD ["python groq.py"]
#COPY .env /app
# Set environment variables from .env file
#ENV ENV_FILE_LOCATION=/app/.env
