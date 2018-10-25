def test_home_page(base, client):
    res = client.get(base)
    assert res.ok
    assert 'What\'s up Docker Deep Divers! You\'ve visited me' in str(res.content)
