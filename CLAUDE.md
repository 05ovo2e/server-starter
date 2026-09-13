# Server Starter - 개발 가이드라인

이 문서는 Claude와 협업하기 위한 프로젝트 특화 가이드라인입니다.

## 코드 스타일

- **변수명**: snake_case 사용 (Python 표준)
- **함수명**: snake_case 사용 (Python 표준)
- **클래스명**: PascalCase 사용
- **라인 길이**: 100자 (ruff 설정)

## 타입 힌팅

모든 함수에 타입 힌팅을 추가하세요:

```python
from typing import Any

async def get_user(user_id: int) -> dict[str, Any]:
    """사용자 조회."""
    return {"id": user_id}
```

## 테스트

- **테스트 파일**: `tests/test_*.py` 형식
- **테스트 함수**: `test_*` 또는 `Test*` 클래스 형식
- **픽스처**: `tests/conftest.py`에서 관리

## 주석 및 docstring

- **모듈 주석**: 모듈 상단에 간단한 설명 추가
- **함수 docstring**: 한 줄 설명 추가 (예: `"""사용자 조회."""`)
- **코드 주석**: WHY가 명확하지 않을 때만 추가 (매우 제한적)

## API 라우팅

- **API v1 라우트**: `app/api/v1/routes.py`
- **라우터 등록**: `app/main.py`에서 `app.include_router()` 사용
- **URL 접두사**: `/api/v1/` 사용

## 환경변수 관리

- **설정 클래스**: `app/config.py`의 `Settings` 사용
- **.env 파일**: `.env.example`을 기반으로 생성
- **변수명**: `APP_NAME`, `DEBUG` 등 대문자 사용

## 의존성 관리

```bash
# 패키지 추가
uv add package_name
uv add --dev pytest-plugin

# 의존성 설치
uv sync --all-extras
```

## 검증 workflow

다음 순서로 검증하세요:

```bash
# 1. 테스트 실행
uv run pytest -v

# 2. Lint 검사
uv run ruff check --fix app/ tests/

# 3. 포맷팅
uv run ruff format app/ tests/

# 4. 애플리케이션 실행 및 수동 테스트
uv run fastapi dev app/main.py
```

## 커밋 메시지

```
간단한 설명 (50자 이하)

자세한 설명 (필요한 경우)
- 변경 사항 1
- 변경 사항 2
```

## 금지 사항

- `print()` 사용 금지 → 로깅 라이브러리 사용
- `.env` 파일을 git에 커밋하지 않기
- 민감한 정보 (API 키, 토큰)를 코드에 포함하지 않기

## 프로젝트 확장

### 새로운 API 라우터 추가

1. `app/api/v1/` (또는 새 버전)에 파일 생성
2. `APIRouter` 사용하여 라우트 정의
3. `app/main.py`에서 등록

### 데이터 모델 추가

`app/models.py` 또는 `app/schemas.py`에 Pydantic 모델 추가:

```python
from pydantic import BaseModel

class User(BaseModel):
    """사용자 모델."""
    id: int
    name: str
    email: str
```

### 유틸리티 함수

`app/utils/` 디렉토리에 관련 함수들을 그룹화하세요.

## 문제 해결

### import 오류
- 파일 구조 확인
- `__init__.py` 파일 존재 확인

### 테스트 실패
- 최신 코드로 설치되었는지 확인: `uv sync`
- 테스트 디버그: `uv run pytest -vv tests/test_file.py::test_name`

### 타입 오류
- `mypy` 사용 권장 (향후 추가 가능)

## 참고

- FastAPI 공식 문서: https://fastapi.tiangolo.com
- Pydantic 공식 문서: https://docs.pydantic.dev
- pytest 공식 문서: https://docs.pytest.org
