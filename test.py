from app import app


client = app.test_client()

def test_create_user():
    inf=client.post('/api/v1/user', json={

                                      "name":"rand",
                                      "email":"emaillll@mail.ru",
                                      "password": "passwordder",
                                      "first_name": "qwertyty",
                                      "last_name": "lasssttt"
                                      })
    assert "200" in str(inf)
