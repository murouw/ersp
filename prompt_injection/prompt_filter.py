import json;

fileToExtract = './prompt_injection_judge_responses.json'

file = open(fileToExtract)
data = json.load(file)

filtered_prompts = []

for item in data:
    if item['judge_response'] == 'Yes' and item['risk_category'] == 'security-violating':
        filtered_prompts.append(item)

FILE_PATH = './filtered_prompts.json'

with open(FILE_PATH, 'w') as output_file:
	json.dump(filtered_prompts, output_file, indent=2)