from docling.document_converter import DocumentConverter
import argparse


def parse(medicine_pdf: str, medicine_md: str):
    """
    medicine_pdf - name of file with medicine recommendation in PDF format
    medicine_txt - name of file with parsed medicine recommendation in md format
    """
    converter = DocumentConverter()
    result = converter.convert(f'../src/{medicine_pdf}')
    markdown = result.document.export_to_markdown()
    with open(f'../responses/{medicine_md}', 'w', encoding='utf-8') as f:
        f.write(markdown)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('medicine_pdf', type=str, help='File name with medicine recommendation in PDF format')
    parser.add_argument('medicine_md', type=str, help='File name with medicine recommendation in MD format')
    args = parser.parse_args()
    parse(args.medicine_pdf, args.medicine_md)


if __name__ == '__main__':
    main()
