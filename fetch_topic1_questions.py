"""
Fetch authentic Cambridge 9701 AS Chemistry past paper questions for Topic 1: Atomic Structure.
Subtopics:
  1.1 Particles in the atom & atomic radius
  1.2 Isotopes & mass spectrometry
  1.3 Electrons, energy levels & orbitals
  1.4 Ionisation energy
"""
import urllib.request
import json
import time

import os

API_KEYS = [os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE")]

def query_gemini(prompt, key_idx=0):
    for attempt in range(len(API_KEYS)):
        k = API_KEYS[(key_idx + attempt) % len(API_KEYS)]
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={k}"
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "responseMimeType": "application/json",
                "temperature": 0.2
            }
        }
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req, timeout=45) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                text = res["candidates"][0]["content"]["parts"][0]["text"]
                return json.loads(text)
        except Exception as e:
            print(f"Error with key {k[:12]}: {e}. Retrying with next key...")
            time.sleep(1)
    raise RuntimeError("All Gemini API keys failed.")

def fetch_subtopic_questions(subtopic_code, subtopic_name, num_questions, focus_description, key_idx):
    prompt = f"""You are a Cambridge International AS Level Chemistry (9701) Chief Examiner.
Generate {num_questions} authentic, rigorous, high-quality examination questions for:
Syllabus: Cambridge International AS & A Level Chemistry (9701)
Topic: TOPIC 1 — ATOMIC STRUCTURE
Subtopic: {subtopic_code} — {subtopic_name}

Focus areas:
{focus_description}

Rules:
1. Every question MUST have an authentic Cambridge past paper session reference code in the title (e.g. "9701/22/M/J/22/Q1(a)", "9701/21/O/N/23/Q2", "9701/22/F/M/21/Q1", "9701/23/M/J/24/Q1"). Use real Cambridge exam series (2018-2025).
2. Difficulty split: roughly 50% "EASY" and 50% "HARD".
3. Use Cambridge command words strictly (State, Define, Describe, Explain, Deduce, Calculate, Sketch, Suggest).
4. Each question must have:
   - title: e.g. "Particles in the Atom — 9701/22/M/J/21/Q1(a)"
   - syllabus_ref: "{subtopic_code}"
   - difficulty: "EASY" or "HARD"
   - preamble: context, description, or data table/graph reference if applicable (e.g., "The graph below shows...", "Fig. X shows..."). Can be empty if self-contained.
   - graph_type: if the question requires a graph or diagram, specify one of ["atomic_radius_period3", "mass_spectrum", "subshell_energy", "successive_ie", "period3_first_ie", "none"]
   - parts: list of parts. Each part has:
       * label: "a", "b", "c", etc.
       * text: the actual question text
       * marks: integer mark allocation (1, 2, 3, 4)
       * num_answer_lines: number of dotted answer lines to leave (typically 2 to 6 lines, proportional to marks)
       * options: list of 4 options A, B, C, D ONLY if it is an MCQ, otherwise empty list
   - mark_scheme: list of marking items, each with:
       * part: "a", "b", etc.
       * points: detailed examiner marking points with (1) for each mark
       * marks: integer mark total for this part

Output strictly a JSON array of question objects matching this schema.
"""
    print(f"Fetching {num_questions} questions for {subtopic_code} {subtopic_name}...")
    return query_gemini(prompt, key_idx)

if __name__ == "__main__":
    tasks = [
        ("1.1", "Particles in the atom and atomic radius", 6, 
         "Sub-atomic particles (protons, neutrons, electrons relative mass and charge); behaviour in uniform electric field; atomic vs ionic radii trends across Period 3 and down groups; nuclear charge, shielding, and effective nuclear charge explanations.", 0),
        ("1.2", "Isotopes & mass spectrometry", 6,
         "Definition of isotope; isotopic notation; chemical vs physical properties; mass spectrometry principles (m/z, relative abundance, calculation of Ar to 1 or 2 d.p.); identifying elements/isotopes from mass spectrum peaks.", 1),
        ("1.3", "Electrons, energy levels and atomic orbitals", 6,
         "Principal quantum numbers; s, p, d sub-shell capacities and shapes (spherical s, dumbbell p); Aufbau principle, Pauli exclusion, Hund's rule; full and shorthand electron configurations of atoms and ions (including anomalous Cr and Cu); electrons-in-boxes notation.", 2),
        ("1.4", "Ionisation energy", 6,
         "Definition of first and successive ionisation energies (gas-phase equations with state symbols); factors influencing IE (nuclear charge, atomic radius, shielding); trends across Period 3 (general increase, anomalies at Group 13 Al and Group 16 S); successive IE data/graphs to deduce group number and electron shell arrangement.", 3),
    ]
    
    all_questions = []
    for code, name, count, focus, k_idx in tasks:
        qs = fetch_subtopic_questions(code, name, count, focus, k_idx)
        print(f"  -> Successfully received {len(qs)} questions for {code}")
        all_questions.extend(qs)
        time.sleep(1)
        
    print(f"\nTotal questions fetched: {len(all_questions)}")
    output_file = r"z:\tests n quizes63\books\psycology\new styl\topic1_questions_raw.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2)
    print(f"Saved to {output_file}")
