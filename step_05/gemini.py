import google.generativeai as genai

class Gemini:
    def __init__(self, token=None):
        genai.configure(api_key=token)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def get_response(self, message):
        response = self.model.generate_content(message)
        return response.text