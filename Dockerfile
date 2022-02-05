# Start with python 3.8 image
FROM python:3.8

EXPOSE 8080

RUN apt update && curl -sL https://deb.nodesource.com/setup_14.x | bash -

RUN apt -y install nodejs

# Install python dependencies
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# Copy frontend directory & install dependencies
COPY frontend/package.json /frontend/package.json
RUN cd frontend/ && npm install

COPY backend/ /backend
COPY frontend/ /frontend

# Build frontend assets
WORKDIR /frontend
RUN npm rebuild esbuild
RUN npm run build

WORKDIR /backend

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]


