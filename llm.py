from groq import Groq
from config import API_KEY, MODEL


if not API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. Add it to the .env file."
    )


client = Groq(api_key=API_KEY)


def ask(system_prompt, user_prompt):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.1
    )

    return response.choices[0].message.content