# Instagram Sync API
Django REST API for:
1. Syncing posts from Instagram
2. Saving data to PostgreSQL
3. Sending comments via the Instagram Graph API

## Running with Docker

### 1. Create a `.env` file in the project root
```bash
SECRET_KEY=your_django_secret_key
DATABASE_NAME=instagram_db
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432
INSTAGRAM_ACCESS_TOKEN=your_instagram_token
```

### 2. Build and run the container
```bash
docker-compose up --build
```

The application will be available at:
http://127.0.0.1:8000/

## Important
If you are located in Russia, all requests must be made through a VPN.
