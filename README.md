## VALI

### System

- frontend

  - Vue.js 3.x
  - Vite
  - typescript

- backend

  - Python 3.x
  - venv
  - FastAPI

- database
  - Redis

### Set up

- frontend

  ```
  cd frontend
  npm install
  ```

- backend

  ```
  cd backend
  python setup.py
  ```

### Start up

- frontend

  ```
  cd frontend
  npm run dev
  ```

- backend
  ```
  cd backend
  python startup.py
  ```

### Env

- frontend

  - VITE_API_URL : backend's domain

- backend

  - FRONT_URL : frontend's domain
  - REDIS_HOST : Redis's host
  - REDIS_PORT : Redis's port
  - REDIS_USERNAME : Redis's username
  - REDIS_PASSWORD : Redis's password
