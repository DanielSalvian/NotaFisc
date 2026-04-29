from pathlib import Path
from pypdf import PdfReader
from PIL import Image
import pytesseract
from pdf2image import convert_from_path


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
    
    def ocrread(self, file_name) -> str:
        # Configurar o caminho do executável do Tesseract, se necessário
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        try:
            # Converter cada página do PDF em imagem
            imagens = convert_from_path(file_name)
            texto_total = ""
            for imagem in imagens:
                texto_total += pytesseract.image_to_string(imagem, lang='por') + "\n"
            return texto_total
        except Exception as e:
            print(f"Erro ao processar OCR: {e}")
            return ""