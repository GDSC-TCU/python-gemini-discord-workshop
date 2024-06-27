import google.generativeai as genai

class Gemini:
    def __init__(self, token=None):
        genai.configure(api_key=token)
        print([model.name for model in genai.list_models()])
        self.model = genai.GenerativeModel('gemini-pro')
        self.word_model = genai.GenerativeModel('gemini-1.5-pro', system_instruction='You are a knowledgeable teacher, please tell the meaning of the words I said in Japanese. Also, please provide example sentences in English.')

    def get_response(self, message):
        response = self.model.generate_content(message)
        return response.text
    
    def get_word_response(self, message):
        response = self.word_model.generate_content(message)
        return response.text