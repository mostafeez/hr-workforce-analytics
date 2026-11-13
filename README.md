# HR Workforce & Employee Attrition Analytics

A descriptive people-analytics project exploring workforce composition, employee attrition patterns, compensation, tenure, and workplace indicators using Python and Pandas.

## Business questions

- What is the overall employee attrition rate in the sample?
- How does attrition vary across departments?
- How do overtime status and job-satisfaction ratings relate to attrition in this dataset?
- How does attrition vary across tenure groups?
- What does the salary distribution look like across the workforce?

## Key capabilities

- Generates a reproducible synthetic workforce dataset.
- Validates required data columns before analysis.
- Calculates workforce KPIs and department-level summaries.
- Compares attrition rates across overtime, satisfaction, and tenure groups.
- Visualizes department patterns, tenure patterns, and salary distribution.
- Exports analysis tables and charts.
- Includes unit tests for core metric calculations.

## Technology stack

Python · Pandas · NumPy · Matplotlib · Pytest

## Project structure

```text
02-hr-workforce-analytics/
├── data/
│   └── employees.csv
├── docs/
│   └── data_dictionary.md
├── outputs/
├── src/
│   ├── analysis.py
│   └── generate_data.py
├── tests/
│   └── test_analysis.py
├── run_analysis.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/hr-workforce-analytics.git
cd hr-workforce-analytics
```

### 2. Create and activate a virtual environment

**Windows**
```bash
py -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Generate data and run analysis

```bash
python run_analysis.py
```

The command generates `data/employees.csv`, calculates the metrics, and saves results to `outputs/`.

### 5. Run tests

```bash
pytest -q
```

## Outputs

- `kpi_summary.json`
- `department_summary.csv`
- `overtime_attrition.csv`
- `satisfaction_attrition.csv`
- `tenure_attrition.csv`
- `department_attrition.png`
- `overtime_attrition.png`
- `tenure_attrition.png`
- `salary_distribution.png`

## Interpretation and responsible use

This project is intended for descriptive learning and portfolio demonstration only.

- The dataset is synthetic and must not be represented as actual employee data.
- Group differences are descriptive associations in this generated sample; they do not establish cause and effect.
- Attrition patterns should not be used to make decisions about real employees.
- Salary currency is unspecified because the generated values are illustrative.
- The synthetic outcome generator intentionally creates patterns for analysis practice; it is not a validated prediction model.

## License

MIT.
