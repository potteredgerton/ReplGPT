import openai

#Made by Potter Edgerton using OpenAI's API
#Go away nerds, I didn't copy any of Unblocked-GPT's code.

print("ReplGPT")
print("Made by Potter Edgerton using OpenAI's API")
print("Source code: https://replit.com/@PotterE6/ReplGPT?v=1")
openai.api_key = "YOUR API KEY HERE"
print()

while True:
  prompt = input("Type your prompt on the line below\n")
  max_tokens = int(input("Enter the max number of tokens here\n"))
  resp = openai.Completion.create(
    model = "text-davinci-003",
    prompt = prompt,
    temperature = 0,
    max_tokens = max_tokens,
  )
  for choice in resp.choices:
    print(choice.text + "\n")
