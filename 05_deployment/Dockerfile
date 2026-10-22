# 1. Official lightweight Python base image
FROM python:3.13-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy requirements first
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy ONLY predict.py and the trained binary model file
COPY predict.py .
COPY model_C=1.0.bin .

# 6. Expose the port Uvicorn will listen on
EXPOSE 9696

# 7. Start the FastAPI server using Uvicorn
CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]