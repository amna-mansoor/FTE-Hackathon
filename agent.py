from openai import OpenAI
import os
import time


API_KEY = "--------------" 

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=API_KEY,
)

def process_task(file_path):
    file_name = os.path.basename(file_path)
    if "Untitled" in file_name or "ACTION_" in file_name:
        return 

    print(f"\n📂 1. File detected: {file_name}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            task_content = f.read().strip()
        
        if not task_content:
            return

        base_dir = os.path.dirname(os.path.abspath(__file__))
        skill_path = os.path.join(base_dir, 'skills', 'file-triage', 'SKILL.md')
        
        skill_logic = "Provide a professional response."
        if os.path.exists(skill_path):
            with open(skill_path, 'r', encoding='utf-8') as f:
                skill_logic = f.read()

        models_to_try = [
            "meta-llama/llama-3.3-70b-instruct:free", 
            "google/gemini-2.0-flash-exp:free",     
            "mistralai/mistral-small-24b-instruct-2501:free", 
            "openrouter/free"                     
        ]

        response_text = None
        for model_id in models_to_try:
            try:
                print(f"📡 2. Trying model: {model_id}...")
                completion = client.chat.completions.create(
                    extra_headers={
                        "HTTP-Referer": "http://localhost",
                        "X-Title": "Agent Factory",
                    },
                    model=model_id,
                    messages=[
                        {"role": "system", "content": skill_logic},
                        {"role": "user", "content": task_content}
                    ],
                    timeout=45 
                )
                response_text = completion.choices[0].message.content
                print(f"✅ 3. {model_id} responded!")
                break 
            except Exception as model_err:
                print(f"⚠️ {model_id} failed or timed out.")
                continue

        if not response_text:
            print("❌ All models failed. 1. Check Internet. 2. Verify API Key. 3. Check for VPN/Firewall.")
            return

        output_filename = f"ACTION_{file_name}"
        output_path = os.path.join(base_dir, 'vault', 'Needs_Action', output_filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(response_text)
        
        print(f"🎉 4. SUCCESS! Saved to: {output_path}")

    except Exception as e:
        print(f"❌ ERROR: {e}")