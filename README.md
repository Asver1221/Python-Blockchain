# Readme first!
**Activate the virtual environment**
```
source flask-venv/bin/activate
```

**Install all packages**
```
pip install -r requirements.txt
```

**Run the tests**

Make sure to activate the virtual environment.
```
python3 -m pytest backend/tests
```

**Run the application and API**

```
python -m backend.app
```

**Run a peer instance**

```
set PEER=True
python -m backend.app
```

**Run the frontend**

In the frontend directory:
```
npm run start
```

**Seed the backend with data**
```
set SEED_DATA=True
python -m backend.app
```
