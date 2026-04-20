from pathlib import Path
from pypdf import PdfReader


class PDFReaderService:
    def read_pdf(self, file_name) -> str:
        pdf_path = Path(__file__).resolve().parent.parent.parent / "pdfs" / file_name

        reader = PdfReader(str(pdf_path))
        texto_completo = ""

        for page in reader.pages:
            texto = page.extract_text()
            if texto:
                texto_completo += texto + "\n"

        return texto_completo