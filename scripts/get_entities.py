import ollama
import argparse


def llm_request(prompt_template: str, medicine_text: str) -> dict:
    """
    prompt_template - file name with template of prompt to LLM
    medicine_text - file name with medicine recommendation text
    return response of LLM in JSON format
    """
    prompt = ""
    with open(f'../src/{prompt_template}', 'r') as file:
        prompt += file.read()
    with open(f'../responses/{medicine_text}', 'r') as file:
        prompt += file.read()
    response = ollama.chat(
        model='llama3',
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )
    return response


def save_response(response: dict, file_name: str):
    """
    response - response of LLM
    file_name - name of JSON file where the entities and relations will be saved
    """
    file_content = response['message']['content']
    with open(f'../responses/{file_name}', 'w') as file:
        file.write(file_content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('prompt_template', type=str, help='File name with template of prompt to LLM')
    parser.add_argument('medicine_text', type=str, help='File name with medicine recommendation')
    parser.add_argument('response', type=str, help='File name of response LLM')
    args = parser.parse_args()
    response = llm_request(args.prompt_template, args.medicine_text)
    save_response(response, args.response)


if __name__ == '__main__':
    main()
