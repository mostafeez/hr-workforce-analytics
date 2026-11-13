# Data Dictionary

All rows in `data/employees.csv` are **synthetic demonstration records** generated with a fixed random seed. They do not represent real employees or an actual organization.

| Column | Description |
|---|---|
| employee_id | Synthetic unique employee key |
| department | Department grouping |
| job_role | Synthetic job title within department |
| hire_date | Generated hire date |
| tenure_years | Approximate tenure as of 2025-12-31 |
| annual_salary | Synthetic annual salary amount; currency is intentionally unspecified |
| overtime | Whether the employee is assigned overtime in the synthetic sample |
| job_satisfaction | Ordinal rating from 1 (low) to 5 (high) |
| work_life_balance | Ordinal rating from 1 (low) to 4 (high) |
| performance_rating | Ordinal rating from 1 to 4 |
| commute_distance_km | Synthetic one-way commute distance |
| attrition | Synthetic outcome label: Yes or No |

## Metric definitions

- **Attrition rate:** employees with `attrition = Yes` divided by all employees in the group.
- **Average salary:** arithmetic mean of annual_salary.
- **Tenure group:** descriptive band based on tenure_years.

The generator uses a deliberately simple probability mechanism to create variation in the outcome. This is not a validated HR model and does not establish causation.
