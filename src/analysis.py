"""Reusable descriptive analytics for workforce data."""
from pathlib import Path
import json
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

REQUIRED_COLUMNS = {
    "employee_id", "department", "job_role", "hire_date", "tenure_years",
    "annual_salary", "overtime", "job_satisfaction", "work_life_balance",
    "performance_rating", "commute_distance_km", "attrition"
}

def load_data(data_path="data/employees.csv"):
    df = pd.read_csv(data_path, parse_dates=["hire_date"])
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")
    return df

def calculate_kpis(df):
    total = len(df)
    exits = int(df["attrition"].eq("Yes").sum())
    return {
        "employee_count": total,
        "attrition_count": exits,
        "attrition_rate_pct": round(exits / total * 100, 2) if total else 0,
        "average_annual_salary": round(float(df["annual_salary"].mean()), 2) if total else 0,
        "average_tenure_years": round(float(df["tenure_years"].mean()), 2) if total else 0,
        "overtime_share_pct": round(df["overtime"].eq("Yes").mean() * 100, 2) if total else 0
    }

def department_summary(df):
    summary = (df.groupby("department", as_index=False)
                 .agg(employee_count=("employee_id", "count"),
                      attrition_count=("attrition", lambda s: s.eq("Yes").sum()),
                      average_salary=("annual_salary", "mean"),
                      average_tenure=("tenure_years", "mean")))
    summary["attrition_rate_pct"] = (
        summary["attrition_count"] / summary["employee_count"] * 100
    ).round(2)
    return summary.sort_values("attrition_rate_pct", ascending=False)

def segment_summary(df, column):
    result = (df.groupby(column, as_index=False)
                .agg(employee_count=("employee_id", "count"),
                     attrition_count=("attrition", lambda s: s.eq("Yes").sum())))
    result["attrition_rate_pct"] = (
        result["attrition_count"] / result["employee_count"] * 100
    ).round(2)
    return result.sort_values("attrition_rate_pct", ascending=False)

def run_analysis(data_path="data/employees.csv", output_dir="outputs"):
    df = load_data(data_path)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    kpis = calculate_kpis(df)
    departments = department_summary(df)
    overtime = segment_summary(df, "overtime")
    satisfaction = segment_summary(df, "job_satisfaction")
    tenure = df.copy()
    tenure["tenure_group"] = pd.cut(
        tenure["tenure_years"], bins=[-0.01, 1, 3, 5, 10, float("inf")],
        labels=["0–1 years", "1–3 years", "3–5 years", "5–10 years", "10+ years"]
    )
    tenure_summary = segment_summary(tenure, "tenure_group")

    (out / "kpi_summary.json").write_text(json.dumps(kpis, indent=2), encoding="utf-8")
    departments.to_csv(out / "department_summary.csv", index=False)
    overtime.to_csv(out / "overtime_attrition.csv", index=False)
    satisfaction.to_csv(out / "satisfaction_attrition.csv", index=False)
    tenure_summary.to_csv(out / "tenure_attrition.csv", index=False)

    plt.figure(figsize=(10, 5))
    plt.bar(departments["department"], departments["attrition_rate_pct"])
    plt.title("Employee Attrition Rate by Department")
    plt.xlabel("Department"); plt.ylabel("Attrition rate (%)")
    plt.xticks(rotation=30, ha="right"); plt.tight_layout()
    plt.savefig(out / "department_attrition.png", dpi=160); plt.close()

    plt.figure(figsize=(7, 5))
    plt.bar(overtime["overtime"].astype(str), overtime["attrition_rate_pct"])
    plt.title("Attrition Rate by Overtime Status")
    plt.xlabel("Overtime"); plt.ylabel("Attrition rate (%)")
    plt.tight_layout(); plt.savefig(out / "overtime_attrition.png", dpi=160); plt.close()

    plt.figure(figsize=(8, 5))
    plt.bar(tenure_summary["tenure_group"].astype(str), tenure_summary["attrition_rate_pct"])
    plt.title("Attrition Rate by Tenure Group")
    plt.xlabel("Tenure"); plt.ylabel("Attrition rate (%)")
    plt.xticks(rotation=20, ha="right"); plt.tight_layout()
    plt.savefig(out / "tenure_attrition.png", dpi=160); plt.close()

    plt.figure(figsize=(8, 5))
    plt.hist(df["annual_salary"], bins=24)
    plt.title("Annual Salary Distribution")
    plt.xlabel("Annual salary (synthetic currency units)"); plt.ylabel("Employee count")
    plt.tight_layout(); plt.savefig(out / "salary_distribution.png", dpi=160); plt.close()

    return kpis, departments, overtime, satisfaction, tenure_summary

if __name__ == "__main__":
    metrics, *_ = run_analysis()
    print("Analysis complete. KPI summary:")
    for key, value in metrics.items():
        print(f"- {key}: {value}")
