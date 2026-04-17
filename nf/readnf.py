from pypdf import PdfReader

reader = PdfReader()

for i, page in enumerate(reader.pages):
    texto = page.extract_text()
    print(f"\n--- Página {i + 1} ---\n")
    print(texto)