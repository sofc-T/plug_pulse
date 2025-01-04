def test_metadata_endpoint(client):
    response = client.get("/metadata/")
    assert response.status_code == 200
    assert response.json["model"] == "example_model"