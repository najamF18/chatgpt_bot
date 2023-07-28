import openai
from chatbot.utils import generate_response


class ChatGptBotApi:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key
        self.prompts = []

    def create_prompt(self, prompt):
        user_prompt = {prompt: None}
        self.prompts.append(user_prompt)
        return self.prompts

    def get_response(self, prompt_index):
        prompt = self.prompts[prompt_index]
        keys = list(prompt.keys())
        user_prompt = keys[0]
        res = generate_response(openai, user_prompt)
        self.prompts[prompt_index][user_prompt] = res
        return prompt

    def update_prompt(self, prompt_index, new_prompt):
        self.prompts.pop(prompt_index)
        res = generate_response(openai, new_prompt)
        user_prompt = {new_prompt: res}

        self.prompts.append(user_prompt)
        return self.prompts

    def delete_prompt(self, prompt_index):
        self.prompts.pop(prompt_index)
        return self.prompts
