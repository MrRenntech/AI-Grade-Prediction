def project_cgpa(current_cgpa, completed_semesters, predicted_sgpa):
    """
    Projects CGPA after current semester using standard academic formula.
    
    Formula: ((current_cgpa * completed_semesters) + predicted_sgpa) / (completed_semesters + 1)
    """

    if completed_semesters <= 0:
        return round(predicted_sgpa, 2)

    projected = (
        (current_cgpa * completed_semesters) + predicted_sgpa
    ) / (completed_semesters + 1)

    return round(projected, 2)

def get_representative_sgpa(band):
    """
    Maps SGPA Band to a representative SGPA value for projection.
    
    Band 0 (<6)    -> 5.5
    Band 1 (6-7)   -> 6.5
    Band 2 (7-8)   -> 7.5
    Band 3 (8-9)   -> 8.5
    Band 4 (>=9)   -> 9.25
    """
    mapping = {
        0: 5.5,
        1: 6.5,
        2: 7.5,
        3: 8.5,
        4: 9.25
    }
    return mapping.get(band, 0.0) # Default to 0.0 if unknown
