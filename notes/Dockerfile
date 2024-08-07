# Stage 1: Build React app with Vite
FROM node:18-alpine as build
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
# Debug: Show contents before build
RUN echo "Contents before build:" && ls -la
# Run build with error checking
RUN npm run build || (echo "Build failed. Contents of directory:" && ls -la && exit 1)
# Debug: Show contents after build
RUN echo "Contents after build:" && ls -la
# Debug: Show contents of dist if it exists
RUN if [ -d "dist" ]; then echo "Contents of dist:" && ls -la dist; else echo "dist directory not found"; fi

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

# Copy the built React app (if it exists)
COPY --from=build /app/frontend/dist ./staticfiles || echo "Failed to copy dist folder. It might not exist."
# Debug: List contents of staticfiles
RUN echo "Contents of staticfiles:" && ls -la staticfiles

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]