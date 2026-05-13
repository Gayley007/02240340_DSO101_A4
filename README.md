# 02240340 DSO101 Assignment 4 — Flask CI/CD App

A Flask backend application with automated CI/CD via GitHub Actions and deployment to Render.

## Project Structure

```
project/
├── app.py                        # Flask application
├── test_app.py                   # Unit tests (pytest)
├── requirements.txt              # Python dependencies
├── render.yaml                   # Render deployment config
└── .github/workflows/ci.yml     # GitHub Actions CI/CD pipeline
```

## API Endpoints

| Method | Endpoint       | Description              |
|--------|----------------|--------------------------|
| GET    | `/`            | Home — returns greeting  |
| GET    | `/health`      | Health check             |
| GET    | `/add/<a>/<b>` | Returns sum of a and b   |

## Running Locally

```bash
pip install -r requirements.txt
python app.py
```

App runs at `http://localhost:5000`.

## Running Tests

```bash
pytest -v
```

## CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci.yml`) triggers on every push to `main`:

1. **Build** — checks out code, sets up Python 3.9, installs dependencies
2. **Test** — runs `pytest` with verbose output
3. **Deploy** — triggers a Render deploy hook (stored as `RENDER_DEPLOY_HOOK_URL` secret)

## Deployment (Render)

### Steps to set up auto-deploy:

1. Create a new **Web Service** on [Render](https://render.com) and connect this GitHub repo.
2. Set **Build Command**: `pip install -r requirements.txt`
3. Set **Start Command**: `gunicorn app:app`
4. Copy the **Deploy Hook URL** from Render → Settings → Deploy Hook.
5. Add it as a GitHub secret named `RENDER_DEPLOY_HOOK_URL` under:
   - GitHub repo → Settings → Secrets and variables → Actions → New repository secret

Every push to `main` will now automatically test and deploy the app.
