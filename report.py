from models import Session, JobMatch

def generate_report():
    session = Session()
    # Query all matches saved in the database
    matches = session.query(JobMatch).order_by(JobMatch.timestamp.desc()).all()
    
    print(f"\n--- 📊 AI-SCOUT INTELLIGENCE REPORT ---")
    print(f"{'TIMESTAMP':<20} | {'COMPANY':<30} | {'SCORE':<7}")
    print("-" * 65)
    
    for m in matches:
        time_str = m.timestamp.strftime("%Y-%m-%d %H:%M")
        print(f"{time_str:<20} | {m.company:<30} | {m.score:>5.1f}%")

if __name__ == "__main__":
    generate_report()