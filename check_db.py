from database import SessionLocal
from models import JobMatch
db=SessionLocal()


results = db.query(JobMatch).all()

print(f"\n--- 📊 SCOUT DATABASE REPORT ({len(results)} entries) ---")
for row in results:
    print(f"[{row.timestamp.strftime('%H:%M')}] {row.company} | Score: {row.score}% | Skills: {row.keywords_found}")