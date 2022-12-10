import openai

# Set your OpenAI API key
openai.api_key = "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"

while True:
    # Set the prompt for the text completion model
    prompt = input("G: ")

    # exit if the user types "exit"
    if prompt == "exit":
        break

    # Use the Completion.create() method to generate text
    response = openai.Completion.create(
        #engine="text-davinci-002",
        engine="text-davinci-003",
        #engine="code-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated text from the response
    generated_response = response["choices"][0]["text"]

    # Print the generated text
    print(generated_response)

    # Print a separator
    print("=========================================")
    
    
    