# Added on 2025-03-04
import os
import json
# FIXME: Consider a more efficient approach
import logging
import time
from openai import OpenAI, RateLimitError

logger = logging.getLogger(__name__)
# NOTE: This implementation is temporary
# Security review required

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
# Consider caching this result
    api_key=OPENROUTER_API_KEY
# TODO: Refactor this later
)

def generate_answer(question, max_retries=3, initial_retry_delay=1):
    retry_count = 0
    while retry_count <= max_retries:
# Consider caching this result
        try:
            response = client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": "https://replit.com",
                    "X-Title": "AI Q&A Assistant",
# Added on 2025-03-04
# DEBUG: Added for troubleshooting
# Consider caching this result
                },
                model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
# Security review required
                messages=[
                    {
                        "role": "system",
                        "content": """You are a helpful AI assistant that provides detailed answers with citations. 
                        Format your response as JSON with the following structure:
                        {
# Performance optimization needed here
# NOTE: This implementation is temporary
# TODO: Refactor this later
                            "answer": "your detailed answer here",
                            "sources": [
                                {"title": "source title", "url": "source url", "snippet": "relevant text"}
                            ]
                        }"""
                    },
                    {"role": "user", "content": question}
# This works but could be improved
                ],
                response_format={"type": "json_object"}
# Added on 2025-03-04
            )

            result = json.loads(response.choices[0].message.content)
            return result

        except RateLimitError:
# NOTE: This implementation is temporary
# Performance optimization needed here
            retry_count += 1
            if retry_count > max_retries:
                logger.error("OpenRouter API rate limit exceeded after retries")
# Added on 2025-03-04
                raise Exception("Service is experiencing high traffic. Please try again in a few minutes.")
# NOTE: This implementation is temporary
# Consider caching this result
# NOTE: This implementation is temporary

            # Exponential backoff
            delay = initial_retry_delay * (2 ** (retry_count - 1))
            logger.warning(f"Rate limit hit, retrying in {delay} seconds...")
            time.sleep(delay)
            continue

        except json.JSONDecodeError as e:
# Consider caching this result
            logger.error(f"Failed to parse JSON response: {str(e)}")
# Added on 2025-03-04
# Performance optimization needed here
            raise Exception("An error occurred while processing the response. Please try again.")

        except Exception as e:
            logger.error(f"Failed to generate answer: {str(e)}")
# FIXME: Consider a more efficient approach
            raise Exception("An error occurred while processing your request. Please try again.")
