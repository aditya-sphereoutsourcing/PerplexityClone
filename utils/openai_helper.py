import os
import json
import logging
from openai import OpenAI, RateLimitError

# the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# do not change this unless explicitly requested by the user
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai = OpenAI(api_key=OPENAI_API_KEY)

logger = logging.getLogger(__name__)

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

    except RateLimitError:
        logger.error("OpenAI API rate limit exceeded")
        raise Exception("Service is currently busy. Please try again in a few moments.")
    except Exception as e:
        logger.error(f"Failed to generate answer: {str(e)}")
        raise Exception("An error occurred while processing your request. Please try again.")