from deep_translator import GoogleTranslator
import argparse


def translate_text(text: str, source='ru', target='en') -> str:
    """
    text - original text to translate
    source - language from
    target - language to
    """
    translator = GoogleTranslator(source=source, target=target)
    translation = translator.translate(text)
    return translation


def translate_file(file_from: str, file_to: str):
    """
    file_from - name of file with russian text
    file_to - name of file with english text
    """
    with open(f'../responses/{file_from}', 'r', encoding='utf-8') as file:
        text_ru = file.read()
    text_eng = translate_text(text_ru)
    with open(f'../responses/{file_to}', 'w', encoding='utf-8') as file:
        file.write(text_eng)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_from', type=str, help='File name with russian text')
    parser.add_argument('file_to', type=str, help='File name with english text')
    args = parser.parse_args()
    translate_file(args.file_from, args.file_to)


if __name__ == "__main__":
    main()
