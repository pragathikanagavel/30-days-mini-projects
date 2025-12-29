import re
import os

# ---------- CONFIG ----------
SKILLS_DB = {
    "python", "java", "c++", "sql", "html", "css", "javascript",
    "machine learning", "data analysis", "excel", "power bi",
    "git", "github", "communication", "teamwork"
}

WEAK_WORDS = ["responsible", "worked on", "helped", "good", "basic"]

JOB_ROLE_SKILLS = {
    "data analyst": {"python", "sql", "excel", "power bi"},
    "python developer": {"python", "git", "github"},
    "web developer": {"html", "css", "javascript"}
}


# ---------- FUNCTIONS ----------
def load_resume(filename):
    # Add .txt extension if not present
    if not filename.endswith('.txt'):
        filename = filename + '.txt'
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read().lower()
    except FileNotFoundError:
        print(f"\nError: File '{filename}' not found in the current directory.")
        print(f"Current directory: {os.getcwd()}")
        print("\nPlease ensure:")
        print("1. The file exists in the current directory")
        print("2. The filename is spelled correctly")
        print("3. The file has .txt extension (or will be added automatically)")
        return None
    except Exception as e:
        print(f"\nError reading file: {e}")
        return None


def detect_sections(text):
    sections = ["education", "skills", "projects", "experience", "certification"]
    found = [s for s in sections if s in text]
    return found


def extract_skills(text):
    found = set()
    for skill in SKILLS_DB:
        if skill in text:
            found.add(skill)
    return found


def resume_length_check(text):
    words = len(text.split())
    if words < 250:
        return words, "Too short"
    elif words > 800:
        return words, "Too long"
    else:
        return words, "Ideal"


def contact_validation(text):
    email = bool(re.search(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", text))
    phone = bool(re.search(r"\b\d{10}\b", text))
    linkedin = "linkedin" in text
    github = "github" in text
    return email, phone, linkedin, github


def weak_word_check(text):
    return [word for word in WEAK_WORDS if word in text]


def experience_level(text):
    if "internship" in text or "fresher" in text:
        return "Fresher / Intern"
    elif "experience" in text:
        return "Experienced"
    else:
        return "Unknown"


def calculate_score(sections, skills):
    score = 0
    breakdown = {}

    breakdown["Sections"] = len(sections)
    score += len(sections)

    breakdown["Skills"] = len(skills)
    score += len(skills)

    return score, breakdown


def job_match(text):
    role = input("Enter job role: ").lower()
    if role not in JOB_ROLE_SKILLS:
        print("Role not in database.")
        return

    required = JOB_ROLE_SKILLS[role]
    present = {s for s in required if s in text}
    missing = required - present

    print("\nMatched Skills:", ", ".join(present))
    print("Missing Skills:", ", ".join(missing))


def generate_report(data):
    with open("resume_report.txt", "w") as file:
        file.write(data)
    print("\nReport saved as resume_report.txt")


# ---------- MAIN PROGRAM ----------
def main():
    filename = input("Enter resume file name (txt): ")
    text = load_resume(filename)
    
    if text is None:
        print("\nExiting due to file error.")
        return

    while True:
        print("\n--- Resume Analyzer ---")
        print("1. Analyze Resume")
        print("2. Job Role Skill Match")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            sections = detect_sections(text)
            skills = extract_skills(text)
            word_count, length_status = resume_length_check(text)
            email, phone, linkedin, github = contact_validation(text)
            weak_words = weak_word_check(text)
            level = experience_level(text)
            score, breakdown = calculate_score(sections, skills)

            report = f"""
Resume Analysis Report
---------------------
Sections Found: {sections}
Skills Found: {', '.join(skills)}

Word Count: {word_count}
Length Status: {length_status}

Email Present: {email}
Phone Present: {phone}
LinkedIn: {linkedin}
GitHub: {github}

Experience Level: {level}
Weak Words Found: {weak_words}

Score: {score}
Score Breakdown: {breakdown}
"""

            print(report)
            generate_report(report)

        elif choice == "2":
            job_match(text)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
