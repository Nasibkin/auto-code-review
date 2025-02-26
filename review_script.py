import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

def review_code(code):
    """
    Sends code to ChatGPT for review and returns the feedback.
    """
    try:
        print("API Key:", os.getenv("OPENAI_API_KEY"))  # Debugging
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[
                {"role": "system", "content": "You are a helpful code reviewer."},
                {"role": "user", "content": f"Review the following code and provide feedback:\n\n{code}"},
            ],
            max_tokens=500,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error during code review: {str(e)}"

def main():
    # Example code to review (replace this with actual code from your project)
    code_to_review = """
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
    """

    print("Starting code review...")
    feedback = review_code(code_to_review)
    print("Code Review Feedback:\n", feedback)

if __name__ == "__main__":
    main()