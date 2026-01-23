import urllib.request
import json
import time

BASE_URL = "http://127.0.0.1:5000"

def test_prediction(name, data):
    url = f"{BASE_URL}/predict"
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            print(f"\n--- {name} ---")
            print(f"Input: {data}")
            pred = result['prediction']
            print(f"Risk Level: {pred['risk_level']}")
            print(f"Risk Score: {pred['risk_score']}")
            print(f"Confidence: {pred['confidence']}")
            print(f"Recommendation: {pred['recommended_action']}")
            print(f"Probabilities: {result['probabilities']}")
            return pred['risk_level']
    except Exception as e:
        print(f"Error testing {name}: {e}")
        return None

def main():
    # Wait for server to be ready? (Assuming it is running)
    try:
        urllib.request.urlopen(BASE_URL)
        print("Server is up!")
    except Exception as e:
        print(f"Server check failed: {e}")
        return

    # Test 1: Low Risk
    low_data = {"age": 17, "studytime": 4, "absences": 0, "G1_G2_AVG": 15}
    test_prediction("Low Risk Test", low_data)

    # Test 2: Medium Risk
    # Adjust inputs if needed to hit medium. 
    # Based on previous context: 
    # Low: G1_G2_AVG high, Absences low
    # High: G1_G2_AVG low, Absences high
    # Medium: Somewhere in between
    med_data = {"age": 17, "studytime": 2, "absences": 6, "G1_G2_AVG": 11}
    test_prediction("Medium Risk Test", med_data)

    # Test 3: High Risk
    high_data = {"age": 19, "studytime": 1, "absences": 15, "G1_G2_AVG": 8}
    test_prediction("High Risk Test", high_data)

if __name__ == "__main__":
    main()
