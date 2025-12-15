# x

Backend API for x

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/Malleswar-249/E-COMMERCE-WEBSITE))

## Project Structure

```
x/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- user registration
- user authentication
- profile management
- password reset

## API Endpoints

- `POST /api/register` - Create a new user account.
- `POST /api/login` - Authenticate an existing user account.
- `GET /api/profile` - Retrieve the current user's profile information.
- `PUT /api/profile` - Update the current user's profile information.
- `POST /api/password_reset` - Initiate a password reset for the current user.

## License

MIT
