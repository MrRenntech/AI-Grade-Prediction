from src.cgpa_projection import project_cgpa, get_representative_sgpa

def test_logic():
    print("--- Testing CGPA Projection Logic ---")
    
    # Test Case 1: User Example
    # Completed Semesters: 3, Current CGPA: 7.4, Predicted SGPA Band: 2 (7-8 -> 7.5)
    current_cgpa = 7.4
    semesters = 3
    band = 2 
    predicted_sgpa = get_representative_sgpa(band)
    
    projected = project_cgpa(current_cgpa, semesters, predicted_sgpa)
    
    print(f"Test Case 1:")
    print(f"  Current CGPA: {current_cgpa}")
    print(f"  Semesters: {semesters}")
    print(f"  Predicted SGPA Band: {band} -> {predicted_sgpa}")
    print(f"  Projected CGPA: {projected}")
    print(f"  Expected: ~7.425 -> 7.43 (rounded)")
    
    # Manual Calc: ((7.4 * 3) + 7.5) / 4 = (22.2 + 7.5) / 4 = 29.7 / 4 = 7.425
    
    assert projected == 7.43, f"Expected 7.43, got {projected}"
    print("  [PASS]")

    # Test Case 2: First Semester Student
    semesters = 0
    current_cgpa = 0
    band = 3 # 8.5
    predicted_sgpa = get_representative_sgpa(band)
    projected = project_cgpa(current_cgpa, semesters, predicted_sgpa)
    print(f"\nTest Case 2 (First Sem):")
    print(f"  Projected: {projected}")
    assert projected == 8.5, f"Expected 8.5, got {projected}"
    print("  [PASS]")

    print("\nAll tests passed.")

if __name__ == "__main__":
    test_logic()
