import PyPDF2
import argparse
import json
import sys

def fill_pdf_form(input_pdf, output_pdf, field_values):
    with open(input_pdf, "rb") as infile:
        reader = PyPDF2.PdfReader(infile)
        writer = PyPDF2.PdfWriter()
        if reader.get_fields():
            writer.append_pages_from_reader(reader)
            writer.update_page_form_field_values(writer.pages[0], field_values)
            with open(output_pdf, "wb") as outfile:
                writer.write(outfile)
            print(f"Filled PDF saved to {output_pdf}")
        else:
            print("No form fields found in PDF.")

def merge_pdfs(pdf_list, output_pdf):
    writer = PyPDF2.PdfWriter()
    for path in pdf_list:
        with open(path, "rb") as infile:
            reader = PyPDF2.PdfReader(infile)
            for page in reader.pages:
                writer.add_page(page)
    with open(output_pdf, "wb") as outfile:
        writer.write(outfile)
    print(f"Merged PDF saved to {output_pdf}")

def main():
    parser = argparse.ArgumentParser(description="PDF Form Filler and Merger Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Fill command
    fill_parser = subparsers.add_parser("fill", help="Fill PDF form fields")
    fill_parser.add_argument("input_pdf", help="Input PDF file with form fields")
    fill_parser.add_argument("output_pdf", help="Output PDF file")
    fill_parser.add_argument("field_json", help="JSON file with field values")

    # Merge command
    merge_parser = subparsers.add_parser("merge", help="Merge multiple PDFs")
    merge_parser.add_argument("output_pdf", help="Output PDF file")
    merge_parser.add_argument("pdfs", nargs="+", help="List of PDF files to merge")

    args = parser.parse_args()

    if args.command == "fill":
        try:
            with open(args.field_json, "r") as f:
                field_values = json.load(f)
        except Exception as e:
            print(f"Error loading field values: {e}")
            sys.exit(1)
        fill_pdf_form(args.input_pdf, args.output_pdf, field_values)
    elif args.command == "merge":
        merge_pdfs(args.pdfs, args.output_pdf)

if __name__ == "__main__":
    main()
