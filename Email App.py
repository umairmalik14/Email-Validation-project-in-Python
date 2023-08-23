import openai

#Define openAi API key
openai.api_key = "Your_API_key_Here"

#Set Up the model and Prompt
model_engine = "Text_davinci-003"
prompt = input("Enter your Prompt : ")

#Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)