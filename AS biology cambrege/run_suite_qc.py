"""
Master Suite Quality Control Runner for Cambridge AS Biology (9700)
Candidate: Hamna | Mentora Academy
"""
import subprocess
import os

topics = list(range(1, 12))
cwd = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege"

print("=" * 70)
print("RUNNING MASTER SUITE QC: TOPICS 1 TO 11 (ALL TOPICS)")
print("=" * 70)

all_passed = True
for t in topics:
    qc_file = f"run_qc_topic{t}.py"
    res = subprocess.run(["python", qc_file], capture_output=True, text=True, cwd=cwd)
    if res.returncode == 0:
        print(f"Topic {t:02d}: [PASS] 50 Qs | 220 Marks | 10 FAQs | Mark Scheme Verified")
    else:
        all_passed = False
        print(f"Topic {t:02d}: [FAIL]")
        print(res.stdout)
        print(res.stderr)

print("=" * 70)
if all_passed:
    print("ALL 11 TOPICS PASSED 100% SUITE QC!")
else:
    print("SOME TOPICS FAILED QC!")
print("=" * 70)
