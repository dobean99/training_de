# training_de
1.set up env
python -m venv venv
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
4.Testing
curl -X <METHOD> <URL> [OPTIONS]
example:
curl -X POST "http://127.0.0.1:8000/users" -H "Content-Type: application/json" -d "{\"name\": \"Alice\", \"email\": \"alice@example.com\"}"

