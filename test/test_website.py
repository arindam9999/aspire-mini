import responses, json

from website.models import User, Loan

from datetime import datetime

LOAN = 1200

def initialize_login_req(client, is_admin):
    client.get("/logout")
    client.post("/sign-up", data={"email": f"test@test{is_admin}.com", "password1": "testpassword", "password2": "testpassword", "first_name": "test_name", "is_admin": is_admin})
    client.post("/login", data={"email": f"test@test{is_admin}.com", "password": "testpassword"})

# Test user signup
def test_signup(client, app):
    response = client.post("/sign-up", data={"email": "test@test.com", "password1": "testpassword", "password2": "testpassword", "first_name": "test_name", "is_admin": "True"})
    assert response.status_code == 200
    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().email == "test@test.com"

# Test user login
def test_login(client, app):
    client.post("/sign-up", data={"email": "test@test.com", "password1": "testpassword", "password2": "testpassword", "first_name": "test_name", "is_admin": "True"})
    response = client.post("/login", data={"email": "test@test.com", "password": "testpassword"})
    assert response.status_code == 200

# Test loan functionality
@responses.activate
def test_loan(client, app):
    initialize_login_req(client, is_admin="False")
    # Test loan apply request.
    response = client.post("/loan", data={"amount": f"{LOAN}"})
    assert response.status_code == 200
    with app.app_context():
        assert Loan.query.count() == 1
        assert Loan.query.first().amount == LOAN
    
    # Test loan display request
    response = client.get("/loan")
    data = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['status'] == False 
    assert data[0]['amount'] == LOAN

    # Update Loan Status (Current user should not be able to update)
    response = client.post("/approve-loan", data={"loan_id": f"{data[0]['id']}"})
    assert response.status_code != 200

    # Update Loan Status (Admin user should be able to update)
    initialize_login_req(client, is_admin="True")
    response = client.post("/approve-loan", data={"loan_id": f"{data[0]['id']}"})
    assert response.status_code == 200

    # Test display of repayments scheduled for user
    initialize_login_req(client, is_admin="False")
    response = client.get("/repayment")
    data = json.loads(response.data.decode("utf-8"))[0]['repayments']
    assert response.status_code == 200 
    assert len(data) == 3
    assert data[0]['amount'] == LOAN/3
    assert data[0]['status'] == False

    # Make repayment
    response = client.post("/repayment", data={"amount": f"{LOAN/3}", "repayment_id": data[0]['id']})
    assert response.status_code == 200 

    # The first loan repayment has status changed to true (previously it was false)
    initialize_login_req(client, is_admin="False")
    response = client.get("/repayment")
    data = json.loads(response.data.decode("utf-8"))[0]['repayments']
    assert response.status_code == 200 
    assert len(data) == 3
    assert data[0]['amount'] == LOAN/3
    assert data[0]['status'] == True

# Test login required functionality
def test_invalid_login(client):
    response = client.get("/payments")

    assert response.status_code == 404