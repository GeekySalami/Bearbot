import google.generativeai as genai

class Summarizer:

	def __init__(self):
		genai.configure(api_key= 'AIzaSyAWGwQk4jJCRefGUfH-qa1Oh-qOTURlT9M')
		self.model = genai.GenerativeModel('gemini-pro')

	def resp(self, cde):
		response = self.model.generate_content('Please state the language and precise purpose of this code in atmost 10 words only no any special characters:'+ cde)
		return response.text
	

def gg():
	sum = Summarizer()
	print("summary = "+ sum.resp("printf('helloworld')"))

if __name__ == '__main__':
	gg()