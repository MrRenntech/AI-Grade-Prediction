import urllib.request
import json
import time

BASE_URL = "http://127.0.0.1:5000"

def test_prediction_step_a():
    url = f"{BASE_URL}/predict"
    
    # Payload with NEW academic fields
    data = {
        "age": 17,
        "studytime": 2,
        "absences": 4,
        "G1_G2_AVG": 12,
        "previous_sgpa": 7.2,
        "current_cgpa": 7.4,
        "completed_semesters": 3,
        "mid_sem_score": 62
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            print("\n--- Step A Verification ---")
            print(f"Input: {data}")
            pred = result['prediction']
            print(f"Risk Level: {pred['risk_level']}")
            print(f"Confidence: {pred['confidence']}")
            print("Status: SUCCESS - New inputs accepted, Model predicted successfully.")
    except Exception as e:
        print(f"Error testing Step A: {e}")

if __name__ == "__main__":
    # Give server a moment to start
    time.sleep(2) 
    test_prediction_step_a()
