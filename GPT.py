import json

import openai


def get_gpt_ans(prompt_quest, template_name):
    openai.api_key = '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'
    with open('parametrs.json', 'r') as file:
        data = json.load(file)

        prompt = data['templates'].get(template_name)
        prompt = prompt.replace('[prompt]', prompt_quest)

        print(prompt)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        temperature=0
    )
    return response['choices'][0]['text']


def add_pattern(pattern_name, pattern):
    print(pattern_name, pattern)

    with open('parametrs.json', 'r') as file:
        data = json.load(file)

    with open('parametrs.json', 'w') as file:
        data['templates'][pattern_name] = pattern

        json.dump(data, file)


def get_pattern_list():
    with open('parametrs.json', 'r') as file:
        data = json.load(file)
        pattern_list = list(data['templates'].keys())
        pattern_list.append('+ add new template')

        return pattern_list
