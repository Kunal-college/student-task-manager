import pytest
import app as app_module


@pytest.fixture
def client(tmp_path, monkeypatch):
    # Give each test its own temporary database.
    test_database = tmp_path / "test_tasks.db"
    monkeypatch.setattr(app_module, "DATABASE", test_database)
    app_module.init_db()

    app_module.app.config["TESTING"] = True

    with app_module.app.test_client() as client:
        yield client


def test_home_page_loads(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"My Task Manager" in response.data


def test_add_task(client):
    response = client.post(
        "/add",
        data={"title": "Complete CCA 2"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Complete CCA 2" in response.data


def test_complete_task(client):
    client.post("/add", data={"title": "Test task"})

    with app_module.get_db() as connection:
        task = connection.execute(
            "SELECT id FROM tasks WHERE title = ?",
            ("Test task",),
        ).fetchone()

    response = client.post(
        f"/complete/{task['id']}",
        follow_redirects=True,
    )

    assert response.status_code == 200

    with app_module.get_db() as connection:
        updated_task = connection.execute(
            "SELECT completed FROM tasks WHERE id = ?",
            (task["id"],),
        ).fetchone()

    assert updated_task["completed"] == 1


def test_delete_task(client):
    client.post("/add", data={"title": "Task to delete"})

    with app_module.get_db() as connection:
        task = connection.execute(
            "SELECT id FROM tasks WHERE title = ?",
            ("Task to delete",),
        ).fetchone()

    response = client.post(
        f"/delete/{task['id']}",
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Task to delete" not in response.data
