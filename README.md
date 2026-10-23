# Student Performance Analysis and Visualization

**Portfolio owner:** Muhammad Awais  
**Tools:** Python, pandas, matplotlib  
**Focus:** Descriptive statistics and exploratory data analysis

## Project overview
This beginner-friendly project explores **200 synthetic student records** to understand final-score distributions, study habits, and department-level differences. The data is generated for learning and demonstration: **no real student data is used**.

## Research questions
- What is the average and median final score?
- What percentage of students achieve a score of at least 50?
- How do final scores vary across departments?
- What association appears between study hours and final score?

## How to run
Install Python 3.10 or newer. In the project folder, run:

```bash
python -m pip install -r requirements.txt
python -m src.analyze
```

Run the tests:

```bash
python -m unittest discover -s tests -v
```

On Windows, use `py` in place of `python` if necessary.

## Dataset fields
`data/students.csv` includes `student_id`, `department`, `study_hours_week`, `attendance_percent`, `previous_score`, `assignment_score`, and `final_score`. Scores and attendance use a 0–100 scale. The pass threshold of **50** is an illustrative assumption, not an official university policy.

## Output files
- `outputs/summary.json` — overall metrics
- `outputs/department_summary.csv` — average scores by department
- `outputs/score_distribution.png` — score histogram
- `outputs/study_hours_vs_score.png` — scatter plot
- `outputs/department_scores.png` — department comparison

![Score distribution](outputs/score_distribution.png)

![Study hours versus score](outputs/study_hours_vs_score.png)

![Department comparison](outputs/department_scores.png)

## Results from the included dataset
- **200** synthetic student records
- Average final score: **56.19**
- Median final score: **55.15**
- Pass rate (score >= 50): **66%**
- Study-hours/final-score correlation: **0.285** (weak positive association in this simulated dataset)

## Findings and limitations
This project reports descriptive statistics and correlation, not causal effects. Because the dataset is synthetic, its patterns cannot be generalized to real student populations. The generated data deliberately includes relationships between variables.

## Next steps
I plan to experiment with attendance bands, data-cleaning rules, and a real publicly documented dataset.

## About this portfolio project
**Muhammad Awais** — BS Computer Science graduate interested in data analytics, Python and SQL. This is a guided, tool-assisted learning project. Before academic submission, I will run the code, verify the outputs, and document the improvements I personally make.
