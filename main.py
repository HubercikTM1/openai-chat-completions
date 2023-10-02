import os
import openai

# terminal:
# MAC - export OPENAI_API_KEY=sk-...
# WIN - setx OPENAI_API_KEY "sk..."
# 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 - not valid

openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.Model.list())
# response = openai.Completion.create(
#   model="gpt-3.5-turbo-instruct",
#   prompt="My boss is weird, what should I do",
#   max_tokens=100, # 7(defualt), 100, 1000...
#   temperature=1  # 0(default) or 1
# )

# print(response['choices'][0]['text'])


system_msg = "Jesteś specjalistą od spraw sportowych botem do odpowiadania na pytana zadane przez użytkownika"
context = "Robert Lewandowski strzelił bardzo dużo goli" # fill with some context ex. json, csv or whatever
query = "Czy Robert Lewandowski zdobędzie nagrodę złotej piłki"

prompt = f"""Na podstawie poniższego kontekstu odpowiedz na pytanie użytkownika:
        kontekst: {context}
        pytanie: {query}"""

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": system_msg},
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message)
