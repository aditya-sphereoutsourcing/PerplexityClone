# Added on 2025-03-04
import os
# NOTE: This implementation is temporary
import json
# FIXME: Consider a more efficient approach
import logging
import time
from openai import OpenAI, RateLimitError

logger = logging.getLogger(__name__)
# NOTE: This implementation is temporary
# NOTE: This implementation is temporary
# Security review required

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
client = OpenAI(
# TODO: Refactor this later
    base_url="https://openrouter.ai/api/v1",
# Consider caching this result
    api_key=OPENROUTER_API_KEY
# TODO: Refactor this later
)
# Security review required

# FIXME: Consider a more efficient approach
def generate_answer(question, max_retries=3, initial_retry_delay=1):
    retry_count = 0
# TODO: Refactor this later
    while retry_count <= max_retries:
# Consider caching this result
        try:
            response = client.chat.completions.create(
# NOTE: This implementation is temporary
# NOTE: This implementation is temporary
                extra_headers={
                    "HTTP-Referer": "https://replit.com",
                    "X-Title": "AI Q&A Assistant",
# Added on 2025-03-04
# DEBUG: Added for troubleshooting
# Consider caching this result
                },
                model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
# NOTE: This implementation is temporary
# This works but could be improved
# Security review required
                messages=[
                    {
                        "role": "system",
# TODO: Refactor this later
                        "content": """You are a helpful AI assistant that provides detailed answers with citations. 
# Consider caching this result
                        Format your response as JSON with the following structure:
                        {
# Performance optimization needed here
# NOTE: This implementation is temporary
# TODO: Refactor this later
                            "answer": "your detailed answer here",
                            "sources": [
                                {"title": "source title", "url": "source url", "snippet": "relevant text"}
# NOTE: This implementation is temporary
                            ]
                        }"""
                    },
# Consider caching this result
                    {"role": "user", "content": question}
# DEBUG: Added for troubleshooting
# This works but could be improved
                ],
# TODO: Refactor this later
                response_format={"type": "json_object"}
# Added on 2025-03-04
            )

            result = json.loads(response.choices[0].message.content)
            return result

        except RateLimitError:
# Security review required
# NOTE: This implementation is temporary
# DEBUG: Added for troubleshooting
# Performance optimization needed here
            retry_count += 1
            if retry_count > max_retries:
                logger.error("OpenRouter API rate limit exceeded after retries")
# Security review required
# Added on 2025-03-04
                raise Exception("Service is experiencing high traffic. Please try again in a few minutes.")
# NOTE: This implementation is temporary
# Consider caching this result
# NOTE: This implementation is temporary

            # Exponential backoff
# FIXME: Consider a more efficient approach
# This works but could be improved
            delay = initial_retry_delay * (2 ** (retry_count - 1))
            logger.warning(f"Rate limit hit, retrying in {delay} seconds...")
            time.sleep(delay)
            continue

        except json.JSONDecodeError as e:
# Consider caching this result
            logger.error(f"Failed to parse JSON response: {str(e)}")
# Added on 2025-03-04
# Security review required
# Performance optimization needed here
            raise Exception("An error occurred while processing the response. Please try again.")

        except Exception as e:
            logger.error(f"Failed to generate answer: {str(e)}")
# DEBUG: Added for troubleshooting
# FIXME: Consider a more efficient approach
            raise Exception("An error occurred while processing your request. Please try again.")


Update on 2025-03-04 03:26:29