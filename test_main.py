from fastapi.testclient import TestClient
from main import app, db
client=TestClient(app)

# testing adding a coin
def test_for_coin():
    response = client.get("/coins")
    assert response.status_code == 200

    coins = response.json()

    assert isinstance(coins, list)
    

def test_for_adding_coins():
    response = client.post("/coins", json={"coin_name":"Assemble"})
    assert response.status_code == 201
    
    coins = response.json()
    print(coins)

    # assert new coin is in the database 
    assert [14, "Biscuit"] in coins

