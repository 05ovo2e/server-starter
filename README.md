# Server Starter

Python + FastAPI 기반의 server-starter입니다.

## 기술 스택

- Python: 3.13+
- Package Manager: uv
- Web Framework: FastAPI
- Data Validation: Pydantic
- Testing: pytest
- Code Quality: Ruff

## 프로젝트 구조

```
server-starter/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI 애플리케이션 진입점
│   ├── config.py            # 환경변수 설정 (Pydantic BaseSettings)
│   └── api/
│       └── v1/
│           ├── __init__.py
│           └── routes.py    # API v1 라우트
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # pytest 설정 및 픽스처
│   └── test_main.py         # 메인 테스트
├── pyproject.toml           # 프로젝트 설정 및 의존성
├── .env.example             # 환경변수 예시
├── .gitignore               # git 무시 파일
├── CLAUDE.md                # 개발 가이드라인
└── README.md                # 이 파일
```

## 설치 및 실행

### 1. 환경변수 설정

```bash
# .env 파일 생성 (선택사항)
cp .env.example .env
```

### 2. 의존성 설치

```bash
# 기본 의존성 + 개발 도구(pytest, ruff) 설치
uv sync

# 프로덕션 환경에서 개발 도구 제외 (선택사항)
uv sync --no-dev
```

### 3. 애플리케이션 실행

```bash
# 개발 서버 실행
uv run fastapi dev app/main.py

# 또는 uvicorn 직접 사용
uv run uvicorn app.main:app --reload
```

서버는 `http://localhost:8000`에서 실행됩니다.

### API 엔드포인트

- `GET /` - 루트 엔드포인트
- `GET /api/v1/health` - 헬스 체크 (API v1)
- `GET /docs` - Swagger UI 문서
- `GET /redoc` - ReDoc 문서

## 테스트

```bash
# 전체 테스트 실행
uv run pytest

# 상세 출력과 함께 테스트 실행
uv run pytest -v

# 특정 테스트 파일 실행
uv run pytest tests/test_main.py
```

## 코드 품질

### Ruff를 사용한 Linting

```bash
# 코드 검사
uv run ruff check app/ tests/

# 자동 수정
uv run ruff check --fix app/ tests/

# 포맷팅
uv run ruff format app/ tests/
```

### 코드 스타일

- 라인 길이: 100자
- 대상 Python 버전: 3.13+
- Import 순서: 자동 정렬 (isort)

## 개발 workflow

1. **코드 작성**: `app/` 디렉토리에 코드 추가
2. **라우트 추가**: `app/api/v1/routes.py` (또는 새로운 라우터 파일)에 엔드포인트 추가
3. **테스트 작성**: `tests/` 디렉토리에 테스트 추가
4. **검증**:
   ```bash
   uv run pytest           # 테스트 실행
   uv run ruff check --fix # Lint 검사 및 수정
   ```

## 주요 파일 설명

### app/main.py
FastAPI 애플리케이션 진입점. 설정 로딩 및 라우터 등록.

### app/config.py
Pydantic BaseSettings를 사용한 환경변수 관리.
`.env` 파일에서 자동으로 읽습니다.

### app/api/v1/routes.py
API v1 엔드포인트 정의.
향후 API 버전 확장 시 `app/api/v2/routes.py` 등으로 추가 가능.

### tests/conftest.py
pytest 설정 및 전역 픽스처 정의.
TestClient 등을 포함합니다.

## 다음 단계

이 starter를 기반으로 다음을 추가할 수 있습니다:

- **데이터베이스**: SQLAlchemy + Alembic (PostgreSQL 권장)
- **인증**: JWT + python-jose
- **캐싱**: Redis
- **컨테이너**: Docker + docker-compose
- **LLM 통합**: LangChain + LangGraph
- **모니터링**: Prometheus + Grafana
- **로깅**: structlog

## 라이선스

MIT