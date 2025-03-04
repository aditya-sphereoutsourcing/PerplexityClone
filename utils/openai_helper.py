import os
import json
from openai import OpenAI

# the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# do not change this unless explicitly requested by the user
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai = OpenAI(api_key=OPENAI_API_KEY)

def generate_answer(question):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": """You are a helpful AI assistant that provides detailed answers with citations. 
                    Format your response as JSON with the following structure:
                    {
                        "answer": "your detailed answer here",
                        "sources": [
                            {"title": "source title", "url": "source url", "snippet": "relevant text"}
                        ]
                    }"""
                },
                {"role": "user", "content": question}
            ],
            response_format={"type": "json_object"}
        )
        
        result = json.loads(response.choices[0].message.content)
        return result
    
    except Exception as e:
        raise Exception(f"Failed to generate answer: {str(e)}")
