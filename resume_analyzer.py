# resume_analyzer.py

# Sample expected keywords
skills_keywords = ['python', 'java', 'html', 'css', 'communication', 'teamwork', 'problem solving', 'project', 'leadership', 'sql']
score = 0

print("AI Resume Analyzer 🤖")
print("Paste your resume text below. Type 'END' to finish:\n")

lines = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

resume_text = " ".join(lines).lower()  # Convert to lowercase for uniform comparison

print("\nAnalyzing resume...\n")

found_keywords = []

for word in skills_keywords:
    if word in resume_text:
        found_keywords.append(word)
        score += 10

print(f"✓ Detected Skills: {', '.join(found_keywords)}")
print(f"✍️ Resume Score: {score}/100")

# Basic feedback
if score >= 70:
    print("✅ Great resume! You're showcasing a lot of in-demand skills.")
elif score >= 40:
    print("⚠️ Decent resume. You can improve it by adding more technical and soft skills.")
else:
    print("❗You need to include more relevant skills and keywords to stand out.")

# Tips
print("\n💡 Tips to Improve:")
if "communication" not in found_keywords:
    print("- Mention soft skills like 'Communication' or 'Leadership'")
if "project" not in found_keywords:
    print("- Include past projects or team-based activities")
if "python" not in found_keywords and "java" not in found_keywords:
    print("- Technical skills like Python, Java can boost your profile")

print("\nThank you for using Resume Analyzer!")
