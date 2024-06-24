from dotenv import load_dotenv

import google.generativeai as genai

load_dotenv()

genai.configure()
print([model.name for model in genai.list_models()])
model = genai.GenerativeModel('gemini-pro')
print(model.generate_content('こんにちは！').text)
