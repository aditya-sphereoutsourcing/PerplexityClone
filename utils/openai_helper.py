import os
import json
import logging
import time
from openai import OpenAI, RateLimitError

# the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# do not change this unless explicitly requested by the user
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai = OpenAI(api_key=OPENAI_API_KEY)

logger = logging.getLogger(__name__)

def generate_answer(question, max_retries=3, initial_retry_delay=1):
    retry_count = 0
    while retry_count <= max_retries:
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
            retry_count += 1
            if retry_count > max_retries:
                logger.error("OpenAI API rate limit exceeded after retries")
                raise Exception("Service is experiencing high traffic. Please try again in a few minutes.")

            # Exponential backoff
            delay = initial_retry_delay * (2 ** (retry_count - 1))
            logger.warning(f"Rate limit hit, retrying in {delay} seconds...")
            time.sleep(delay)
            continue

        except Exception as e:
            logger.error(f"Failed to generate answer: {str(e)}")
            raise Exception("An error occurred while processing your request. Please try again.")