# FastAPI + React Product Management System

A full-stack Product Management application built using FastAPI, React, SQLAlchemy, and PostgreSQL. This project provides CRUD operations for managing products through a REST API and a React frontend.

## Features

- View all products
- Add new products
- Update product details
- Delete products
- REST API using FastAPI
- Database integration using SQLAlchemy
- Frontend and backend integration
- Interactive API documentation using Swagger

## Tech Stack

### Frontend
- React
- JavaScript
- HTML/CSS

### Backend
- FastAPI
- Python
- SQLAlchemy
- Pydantic

### Database
- PostgreSQL

## Project Structure

```txt
fastapi-react-product-manager/
│
├── backend/
├── frontend/
├── screenshots/
├── README.md
├── .gitignore
└── docker-compose.yml
```

## Run Backend

```bash
uvicorn main:app --reload
```

Backend runs at:

```txt
http://127.0.0.1:8000
```

Swagger documentation:

```txt
http://127.0.0.1:8000/docs
```

## Run Frontend

```bash
npm start
```

Frontend runs at:

```txt
http://localhost:3000
```

## Future Improvements

- JWT Authentication
- User login system
- Docker deployment
- Cloud deployment
- Search and filter products

## Author

Somesh Omkar

Learning and building full-stack applications using FastAPI and React 🚀