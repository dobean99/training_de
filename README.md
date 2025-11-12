# training_de

1.set up env

- Windown: python -m venv venv
- Mac: python3 -m venv env
- Windown: venv\Scripts\activate
- Mac: source venv/bin/activate
  2.install package
  Upgrade pip safely
  python -m ensurepip --upgrade
  python -m pip install --upgrade pip
  pip install --upgrade pip
  pip install -r requirements.txt
  or pip install fastapi uvicorn celery[redis]

3. Run
   uvicorn app.main:app --reload

4. Testing
   curl -X <METHOD> <URL> [OPTIONS]
   example:
   curl -X GET "http://127.0.0.1:8000/users/"
   curl -X POST "http://127.0.0.1:8000/users/" -H "Content-Type: application/json" -d "{\"name\": \"Alice\", \"email\": \"alice@example.com\"}"

Code	Meaning	When to Use
200 OK	Successful request	Normal GET, PUT
201 Created	Resource created	After POST
204 No Content	Successful, no body	After DELETE
400 Bad Request	Invalid input data	Validation or format errors
401 Unauthorized	Missing or invalid authentication	Login/auth routes
403 Forbidden	User lacks permission	Access control
404 Not Found	Resource not found	Invalid ID, missing data
409 Conflict	Resource already exists	Duplicate entries
500 Internal Server Error	Unexpected errors	Server crash or DB issue
5. Database with SQLAlchemy
          ┌────────────────────────┐
          │      main.py           │
          │ includes routers       │
          └─────────┬──────────────┘
                    │
      ┌─────────────┴──────────────┐
      │                            │
user_router.py              product_router.py
      │                            │
      ▼                            ▼
   user_schema.py              product_schema.py
   user_model.py               product_model.py
      │                            │
      └──────────→ database.py ←────┘

(Client JSON)
↓
[ FastAPI Route (/products) ]
↓
[Pydantic Validation → ProductCreate]
↓
[SQLAlchemy Model → Product]
↓
[Database Session → commit()]
↓
[Response → ProductResponse (JSON)]

5. Background Task

6. Celery

- without Docker
  celery_app = Celery(
  "worker",
  broker="redis://localhost:6379/0",
  backend="redis://localhost:6379/0",
  )

  - install
    brew install redis
    redis-server

- with Docker
