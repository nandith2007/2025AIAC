def extract_student_info(student_dict):
    """
    Extracts full name, branch, and SGPA from a nested student dictionary.

    Args:
        student_dict (dict): Nested dictionary with student information.

    Returns:
        tuple: (full_name, branch, sgpa)
    """
    personal = student_dict["student"]["personal_info"]
    academic = student_dict["student"]["academic"]
    full_name = f"{personal['first_name']} {personal['last_name']}"
    branch = academic["branch"]
    sgpa = academic["results"]["SGPA"]
    return (full_name, branch, sgpa)

if __name__ == "__main__":
    # Example: prompt user for input
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    branch = input("Enter branch: ")
    sgpa = float(input("Enter SGPA: "))

    student_dict = {
        "student": {
            "personal_info": {
                "first_name": first_name,
                "last_name": last_name
            },
            "academic": {
                "branch": branch,
                "results": {
                    "SGPA": sgpa
                }
            }
        }
    }

    result = extract_student_info(student_dict)
    print("Extracted Info:", result)
