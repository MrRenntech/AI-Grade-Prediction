import requests
import json

# Define the API endpoint
url = "http://127.0.0.1:5000/predict"

# Define the payload (Student Data)
# Case: Student with 3 semesters, CGPA 7.4, performing well internally (12/20)
payload = {
    "age": 19,
    "studytime": 2,
    "absences": 4,
    "G1_G2_AVG": 12,
    "current_cgpa": 7.4,
    "completed_semesters": 3
}

print("--- Sending Request to Student Risk API ---")
print(f"URL: {url}")
print(f"Payload: {json.dumps(payload, indent=2)}")

try:
    # Send POST request
    response = requests.post(url, json=payload)

    # Check status code
    if response.status_code == 200:
        data = response.json()
        print("\n--- Success! API Response ---")
        print(json.dumps(data, indent=2))
        
        # Verification Assertions
        assert "risk_assessment" in data, "Missing 'risk_assessment' key"
        assert "academic_prediction" in data, "Missing 'academic_prediction' key"
        assert "model_probabilities" in data, "Missing 'model_probabilities' key"
        
        risk = data["risk_assessment"]
        acad = data["academic_prediction"]
        
        print("\n[VERIFICATION PASS]")
        print(f"Risk Level: {risk['risk_level']}")
        print(f"Predicted SGPA Range: {acad['predicted_sgpa_range']}")
        print(f"Projected CGPA: {acad['projected_cgpa']}")
        
    else:
        print(f"\n--- Error! Status Code: {response.status_code} ---")
        print(response.text)

except requests.exceptions.ConnectionError:
    print("\n[ERROR] Could not connect to the server. Is Flask running?")
except AssertionError as e:
    print(f"\n[FAILURE] Assertion Failed: {e}")
except Exception as e:
    print(f"\n[ERROR] An unexpected error occurred: {e}")
