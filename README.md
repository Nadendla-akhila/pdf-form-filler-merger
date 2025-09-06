# PDF Form Filler and Merger Tool

A Python tool for filling PDF forms and merging multiple PDFs, built with [PyPDF2](https://pypdf2.readthedocs.io/en/latest/).

## Features

- **Fill PDF Forms:** Enter values for form fields and generate a filled PDF.
- **Merge PDFs:** Combine multiple PDF files into one.

## Requirements

- Python 3.7+
- PyPDF2 (`pip install PyPDF2`)

## Usage

Run the tool:

```bash
python pdf_tool.py
```

Follow the menu to:
- Fill a PDF form by entering field names and values.
- Merge PDFs by specifying the files to merge.

## Example

**Fill Form:**
1. Choose option 1.
2. Enter path to your PDF form.
3. Enter output file path.
4. Specify field names and values.

**Merge PDFs:**
1. Choose option 2.
2. Enter number of PDFs to merge.
3. Enter each file path.
4. Specify output file.

---

## Limitations

- Form filling works with AcroForms only (not XFA forms).
- GUI not included; command-line only.

## License

MIT
