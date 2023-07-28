def generate_response(api, prompt):
    response = api.Completion.create(engine="davinci", prompt=prompt, max_tokens=100)
    bot_response = response["choices"][0]["text"].strip()
    return bot_response
