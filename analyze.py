"""Student performance descriptive analysis (synthetic data)."""
from pathlib import Path
import json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

COLUMNS=['student_id','department','study_hours_week','attendance_percent','previous_score','assignment_score','final_score']
def analyze(input_file=Path('data/students.csv'),output_dir=Path('outputs')):
    df=pd.read_csv(input_file)
    missing=set(COLUMNS)-set(df.columns)
    if missing: raise ValueError(f'Missing columns: {sorted(missing)}')
    if df.empty or df[COLUMNS].isna().any().any() or df.student_id.duplicated().any():
        raise ValueError('Dataset empty, missing values, or duplicate student IDs')
    if (df['department'].astype(str).str.strip() == '').any():
        raise ValueError('Empty department names are not allowed')
    for c in COLUMNS[2:]: df[c]=pd.to_numeric(df[c],errors='raise')
    for c in COLUMNS[3:]:
        if not df[c].between(0,100).all(): raise ValueError(f'Invalid range: {c}')
    if not df.study_hours_week.between(0,168).all(): raise ValueError('Invalid study hours')
    output_dir=Path(output_dir);output_dir.mkdir(parents=True,exist_ok=True)
    by_dept=df.groupby('department',as_index=False).agg(students=('student_id','size'),average_score=('final_score','mean')).round(2)
    by_dept.to_csv(output_dir/'department_summary.csv',index=False)
    summary={'student_count':len(df),'average_score':round(float(df.final_score.mean()),2),'median_score':round(float(df.final_score.median()),2),'pass_rate_percent':round(float((df.final_score>=50).mean()*100),2),'study_hours_score_correlation':round(float(df.study_hours_week.corr(df.final_score)),3)}
    (output_dir/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    fig,ax=plt.subplots(figsize=(8,5));ax.hist(df.final_score,bins=12,edgecolor='white');ax.set(title='Distribution of final scores',xlabel='Final score',ylabel='Students');fig.tight_layout();fig.savefig(output_dir/'score_distribution.png',dpi=150);plt.close(fig)
    fig,ax=plt.subplots(figsize=(8,5));ax.scatter(df.study_hours_week,df.final_score,alpha=.6);ax.set(title='Study hours vs final score',xlabel='Study hours per week',ylabel='Final score');fig.tight_layout();fig.savefig(output_dir/'study_hours_vs_score.png',dpi=150);plt.close(fig)
    fig,ax=plt.subplots(figsize=(8,5));ax.bar(by_dept.department,by_dept.average_score);ax.set(title='Average score by department',ylabel='Average score',ylim=(0,100));ax.tick_params(axis='x',rotation=15);fig.tight_layout();fig.savefig(output_dir/'department_scores.png',dpi=150);plt.close(fig)
    return summary
if __name__=='__main__': print(json.dumps(analyze(),indent=2))
