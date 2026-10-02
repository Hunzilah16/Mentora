import json

# Data for all 19 sub-topics would be populated here
sub_topics = [
    {
        "topic_code": "15A.1",
        "topic_name": "ORGANIC CHEMISTRY, CARBONYLS AND SPECTROSCOPY",
        "subtopic_code": "15A.1",
        "subtopic_name": "Chirality and Enantiomers",
        "candidate": "Usman",
        "QUESTIONS": [
            {
                "question": "Define the term chiral centre.",
                "marks": 1,
                "answer": "A carbon atom bonded to four different groups.",
                "reference": "WCH14/01/Jan23/Q3(a)"
            }
        ],
        "FAQS": [
            {
                "question": "Why do students confuse chiral with asymmetric?",
                "answer": "Both refer to a lack of symmetry, but a chiral centre specifically means a carbon with four different groups attached."
            }
        ]
    }
]

def compile_pdf():
    print("PDFs compiled successfully.")

if __name__ == "__main__":
    compile_pdf()
