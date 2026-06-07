import os

folders = [
    'vault/Inbox', 
    'vault/Needs_Action', 
    'vault/Done', 
    'skills/file-triage'
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

skill_content = """# 🧠 Skill: Task Triage
1. Read the incoming request.
2. If it's a coding task, provide a code snippet.
3. If it's a writing task, provide a draft.
4. Always add a 'Next Steps' section at the end.
"""

with open('skills/file-triage/SKILL.md', 'w', encoding='utf-8') as f:
    f.write(skill_content)

print("✅ Folders and Skills ready!")