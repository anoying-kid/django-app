# Stage 1: Build React app with Vite
FROM node:18-alpine as build
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build
# Debug: List contents of current directory and dist
RUN ls -la && ls -la dist

# Stage 2: Setup Django backend
FROM python:3.10-slim
WORKDIR /app/backend

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend code
COPY backend/ ./

# Create a directory for static files
RUN mkdir -p staticfiles

# Copy the built React app
COPY --from=build /app/frontend/dist ./staticfiles
# Debug: List contents of staticfiles
RUN ls -la staticfiles

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]