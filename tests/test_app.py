from app import app


def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_whoami_reports_version_and_sha():
    res = client().get("/")
    assert res.status_code == 200
    body = res.get_json()
    assert body["service"] == "demo-service"
    assert body["version"]
    assert body["git_sha"]


def test_health():
    res = client().get("/health")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}
