import os
import json
import logging
import time
from openai import OpenAI, RateLimitError

logger = logging.getLogger(__name__)

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

def generate_answer(question, max_retries=3, initial_retry_delay=1):
    retry_count = 0
    while retry_count <= max_retries:
        try:
            response = client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": "https://replit.com",
                    "X-Title": "AI Q&A Assistant",
                },
                model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
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
                logger.error("OpenRouter API rate limit exceeded after retries")
                raise Exception("Service is experiencing high traffic. Please try again in a few minutes.")

            # Exponential backoff
            delay = initial_retry_delay * (2 ** (retry_count - 1))
            logger.warning(f"Rate limit hit, retrying in {delay} seconds...")
            time.sleep(delay)
            continue

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON response: {str(e)}")
            raise Exception("An error occurred while processing the response. Please try again.")

        except Exception as e:
            logger.error(f"Failed to generate answer: {str(e)}")
            raise Exception("An error occurred while processing your request. Please try again.")