def test_get_activities_returns_all_activity_details(client):
    # Arrange

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200

    activities = response.json()
    assert "Chess Club" in activities
    assert activities["Chess Club"]["description"]
    assert activities["Chess Club"]["schedule"]
    assert isinstance(activities["Chess Club"]["max_participants"], int)
    assert isinstance(activities["Chess Club"]["participants"], list)