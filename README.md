# LifeOS AI - Personal Student Life Analyzer

## 1. Project Overview

LifeOS AI is a beginner-friendly command-line application for students to record selected daily-life data and receive simple productivity reports and rule-based trend insights.

The project is built for the VIT Python Essentials course and demonstrates Python fundamentals through a modular application.

## 2. Main Features

1. Daily Data Entry
   - Sleep
   - Study time
   - Screen time
   - Exercise
   - Mood
   - Stress
   - Planned and completed tasks

2. Productivity Analysis
   - Calculates a score out of 100.
   - Shows a component-wise score breakdown.
   - Displays configured notes based on the entered values.

3. Reports
   - View previous records.
   - Generate a report using the most recent seven records.

4. AI Insights
   - Uses simple rule-based pattern detection on the user's own logged numbers.
   - Does not use an external AI model or make medical diagnoses.

## 3. Technologies Used

- Python 3
- CSV file storage
- Python standard library
- unittest for validation tests
- Git/GitHub for version control

No external Python packages are required to run the application.

## 4. Project Structure

```text
LifeOS_AI_Project/
│
├── main.py
├── data_manager.py
├── productivity.py
├── analysis.py
├── reports.py
├── insights.py
├── utils.py
├── daily_data.csv
├── statement.md
├── requirements.txt
├── .gitignore
├── tests/
│   └── test_lifeos.py
└── docs/
    ├── architecture.png
    ├── workflow.png
    ├── use_case.png
    ├── sequence.png
    ├── component.png
    └── er_diagram.png
```

## 5. Installation

### Step 1: Install Python

Install Python 3.10 or a newer Python 3 version.

Check the installation:

```bash
python --version
```

On some systems use:

```bash
python3 --version
```

### Step 2: Download or clone the repository

```bash
git clone <YOUR_PUBLIC_GITHUB_REPOSITORY_URL>
cd LifeOS_AI_Project
```

### Step 3: Install dependencies

The project uses only Python's standard library, so there are no third-party packages to install.

You can still run:

```bash
pip install -r requirements.txt
```

## 6. Run the Project

From the project root:

```bash
python main.py
```

Choose an option from the menu.

## 7. Run Tests

From the project root:

```bash
python -m unittest discover -s tests -v
```

## 8. Data Storage

The application stores daily records in:

```text
daily_data.csv
```

The CSV file is created automatically if it does not exist.

## 9. Important Design Note

The name "AI Insights" refers to the rule-based pattern analysis module in this version. It does not claim to use a trained machine-learning model.

## 10. Limitations

- The application is command-line based.
- Data is stored locally in CSV format.
- Insights are based on fixed rules.
- No external prediction model is used.

## 11. Future Enhancements

Possible future work includes a graphical interface, richer visualizations, more flexible analytics, database storage, and optional machine-learning features.
