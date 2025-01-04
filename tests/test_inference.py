def test_inference_endpoint(client):
    sample_data = {"instances": [[1.0, 2.0, 3.0]]}
    response = client.post("/inference/", json=sample_data)
    assert response.status_code == 200
    assert "predictions" in response.json