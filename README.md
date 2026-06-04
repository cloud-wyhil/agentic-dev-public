# StudyNest Demo

FastAPI 기반 Hello World 프로젝트입니다.

## 실행

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
uvicorn app.main:app --reload
```

## 엔드포인트

- GET `/`
- GET `/api/v1/hello/`
- GET `/api/v1/health/live`
- GET `/api/v1/health/ready`
- Swagger UI: `/docs`

## 테스트

```bash
pytest -v
```

## 린트

```bash
ruff check .
```
