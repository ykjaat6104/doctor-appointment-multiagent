import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class LLMModel:
    def __init__(self, model_name="llama3-8b-8192"):
        if not model_name:
            raise ValueError("Model is not defined.")
        self.model_name = model_name
        # Initialize Groq model
        self.model = ChatGroq(
            model=self.model_name,
            temperature=0.7,
            max_tokens=1024,
            groq_api_key=os.getenv("GROQ_API_KEY")  # pulls from .env
        )
        
    def get_model(self):
        return self.model

if __name__ == "__main__":
    # You can choose any supported model
    # e.g., 'llama3-8b-8192', 'llama3-70b-8192', 'mixtral-8x7b-32768'
    llm_instance = LLMModel(model_name="llama3-8b-8192")  
    llm_model = llm_instance.get_model()
    
    response = llm_model.invoke("Hello, how are you?")
    print(response.content)  # Print just the text response