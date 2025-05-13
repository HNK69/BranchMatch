def get_salary_data():
    return {
        "CSE": 8.5,
        "ECE": 7.2,
        "EEE": 6.8,
        "Mechanical": 6.5,
        "Civil": 6.0,
    }

def get_job_growth_data():
    return {
        "CSE": "High",
        "ECE": "Moderate",
        "EEE": "Moderate",
        "Mechanical": "Stable",
        "Civil": "Low",
    }
import pandas as pd

def get_salary_chart_data():
    return pd.DataFrame({
        'Branch': ['CSE', 'ECE', 'EEE', 'Mechanical', 'Civil'],
        'Average Salary (LPA)': [8.5, 7.2, 6.8, 6.5, 6.0]
    }).set_index('Branch')

def get_growth_chart_data():
    return pd.DataFrame({
        'Branch': ['CSE', 'ECE', 'EEE', 'Mechanical', 'Civil'],
        'Growth Index': [9, 7, 6, 5, 4]  # You can customize these scores
    }).set_index('Branch')
