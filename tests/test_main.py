"""메인 애플리케이션 테스트."""


def test_root(client):
    """루트 엔드포인트 테스트."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_check_v1(client):
    """API v1 헬스 체크 테스트."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["version"] == "v1"
