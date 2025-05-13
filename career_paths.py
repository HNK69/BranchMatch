def get_career_paths(branch):
    paths = {
        "CSE": ["Software Engineer", "Data Scientist", "AI Engineer"],
        "ECE": ["Embedded Systems Engineer", "VLSI Designer", "IoT Engineer"],
        "Mechanical": ["Automobile Engineer", "Thermal Engineer", "Product Designer"],
        "Civil": ["Site Engineer", "Structural Designer", "Urban Planner"],
        "EEE": ["Electrical Design Engineer", "Power Systems Engineer"],
    }
    return paths.get(branch, [])