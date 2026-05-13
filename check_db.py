from models import Session, JobMatch

session = Session()
results = session.query(JobMatch).all()

print(f"\n--- 📊 SCOUT DATABASE REPORT ({len(results)} entries) ---")
for row in results:
    print(f"[{row.timestamp.strftime('%H:%M')}] {row.company} | Score: {row.score}% | Skills: {row.keywords_found}")