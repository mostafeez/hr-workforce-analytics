"""Generate deterministic synthetic workforce data."""
from pathlib import Path
import numpy as np
import pandas as pd

SEED = 73

def generate_dataset(output_dir="data", n_employees=1200):
    rng = np.random.default_rng(SEED)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    departments = ["Engineering", "Sales", "Marketing", "Finance", "Operations", "Customer Support", "Human Resources"]
    roles = {
        "Engineering": ["Software Engineer", "QA Analyst", "Data Analyst", "Team Lead"],
        "Sales": ["Sales Executive", "Account Manager", "Sales Manager"],
        "Marketing": ["Marketing Specialist", "Content Strategist", "Marketing Manager"],
        "Finance": ["Financial Analyst", "Accountant", "Finance Manager"],
        "Operations": ["Operations Associate", "Process Analyst", "Operations Manager"],
        "Customer Support": ["Support Specialist", "Support Lead"],
        "Human Resources": ["HR Specialist", "Recruiter", "HR Manager"],
    }
    dept = rng.choice(departments, n_employees,
                      p=[.25, .17, .12, .10, .16, .13, .07])
    hire_dates = pd.to_datetime("2017-01-01") + pd.to_timedelta(
        rng.integers(0, 3200, n_employees), unit="D"
    )
    tenure = ((pd.Timestamp("2025-12-31") - hire_dates).days / 365.25).clip(0, None)
    overtime = rng.choice(["No", "Yes"], n_employees, p=[.72, .28])
    satisfaction = rng.choice([1, 2, 3, 4, 5], n_employees, p=[.07, .14, .30, .34, .15])
    work_life = rng.choice([1, 2, 3, 4], n_employees, p=[.08, .20, .48, .24])
    performance = rng.choice([1, 2, 3, 4], n_employees, p=[.08, .34, .43, .15])
    commute = rng.integers(1, 61, n_employees)
    salary = []
    job_role = []
    for d in dept:
        role = rng.choice(roles[d])
        job_role.append(role)
        base_salary = {
            "Engineering": 68000, "Sales": 52000, "Marketing": 50000,
            "Finance": 61000, "Operations": 47000,
            "Customer Support": 39000, "Human Resources": 48000
        }[d]
        salary.append(max(26000, rng.normal(base_salary, base_salary * .22)))

    # A transparent synthetic outcome mechanism; it is not a real-world causal model.
    logit = (-2.35
             + 0.75 * (overtime == "Yes")
             + 0.38 * (satisfaction <= 2)
             + 0.28 * (work_life <= 2)
             + 0.18 * (tenure < 1.5)
             - 0.12 * (tenure > 5)
             + 0.12 * (commute > 35))
    probability = 1 / (1 + np.exp(-logit))
    attrition = np.where(rng.random(n_employees) < probability, "Yes", "No")

    df = pd.DataFrame({
        "employee_id": [f"E{i:05d}" for i in range(1, n_employees + 1)],
        "department": dept,
        "job_role": job_role,
        "hire_date": hire_dates,
        "tenure_years": tenure.round(1),
        "annual_salary": np.round(salary, 0).astype(int),
        "overtime": overtime,
        "job_satisfaction": satisfaction,
        "work_life_balance": work_life,
        "performance_rating": performance,
        "commute_distance_km": commute,
        "attrition": attrition
    })
    df.to_csv(out / "employees.csv", index=False, date_format="%Y-%m-%d")
    return df

if __name__ == "__main__":
    generate_dataset()
    print("Synthetic workforce dataset generated in ./data")
