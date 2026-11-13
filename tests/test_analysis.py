import pandas as pd
from src.analysis import calculate_kpis, department_summary, segment_summary

def sample_employees():
    return pd.DataFrame({
        "employee_id": ["E1", "E2", "E3", "E4"],
        "department": ["Sales", "Sales", "IT", "IT"],
        "job_role": ["Rep", "Rep", "Analyst", "Analyst"],
        "hire_date": pd.to_datetime(["2021-01-01"] * 4),
        "tenure_years": [4.0, 3.0, 2.0, 1.0],
        "annual_salary": [40000, 42000, 60000, 62000],
        "overtime": ["Yes", "No", "Yes", "No"],
        "job_satisfaction": [2, 4, 3, 5],
        "work_life_balance": [2, 3, 3, 4],
        "performance_rating": [3, 4, 3, 4],
        "commute_distance_km": [10, 20, 30, 40],
        "attrition": ["Yes", "No", "No", "No"]
    })

def test_kpis():
    kpis = calculate_kpis(sample_employees())
    assert kpis["employee_count"] == 4
    assert kpis["attrition_count"] == 1
    assert kpis["attrition_rate_pct"] == 25.0

def test_department_summary_counts():
    result = department_summary(sample_employees())
    assert result["employee_count"].sum() == 4
    assert set(result["department"]) == {"Sales", "IT"}

def test_segment_summary_rate():
    result = segment_summary(sample_employees(), "overtime")
    yes_rate = result.loc[result["overtime"].eq("Yes"), "attrition_rate_pct"].iloc[0]
    assert yes_rate == 50.0
