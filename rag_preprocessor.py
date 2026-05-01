from pypdf import PdfReader

def get_text_lines_from_pdf(reader):
    pages_text = []
    for page in reader.pages:
        pages_text.append(page.extract_text())
    full_text = "\n".join(pages_text)
    lines = full_text.split("\n")
    return lines

def my_custom_chunking(lines):
    chunks = []
    chunk = ""
    for line in lines:
        if line.startswith("§"):
            chunks.append(chunk)
            chunk = line
        else:
            chunk = chunk + " " + line
    chunks.append(chunk)
    return chunks

if __name__ == '__main__':
    reader = PdfReader("web_scraper/law404.pdf")
    lines = get_text_lines_from_pdf(reader)
    chunks = my_custom_chunking(lines)
    print(chunks[1])






