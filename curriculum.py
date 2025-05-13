def load_curriculum(branch):
    curriculum_data = {
        "CSE": [
            ("Semester 1", ["Mathematics", "Physics", "C Programming"]),
            ("Semester 2", ["Data Structures", "Discrete Math"]),
            ("Semester 3", ["DBMS", "OS", "OOPs"]),
        ],
        "ECE": [
            ("Semester 1", ["Mathematics", "Basic Electronics"]),
            ("Semester 2", ["Signals and Systems", "Digital Logic"]),
            ("Semester 3", ["Microprocessors", "VLSI"]),
        ],
        "Mechanical": [
            ("Semester 1", ["Engineering Drawing", "Physics", "Mathematics"]),
            ("Semester 2", ["Mechanics", "Thermodynamics"]),
        ],
        "Civil": [
            ("Semester 1", ["Engineering Drawing", "Math", "Environment Science"]),
            ("Semester 2", ["Mechanics of Materials", "Surveying"]),
        ],
        "EEE": [
            ("Semester 1", ["Circuit Theory", "Engineering Physics"]),
            ("Semester 2", ["Electrical Machines", "Signals and Systems"]),
        ]
    }
    return curriculum_data.get(branch, [])