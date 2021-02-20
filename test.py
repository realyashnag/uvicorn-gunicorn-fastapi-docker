import requests

def test_1():
    response = requests.get("http://localhost:80/items/5?q=somequery")
    print (response)
    # assert response['item_id'] == 5 
    # assert response['item_id'] == "somequery"

test_1()
