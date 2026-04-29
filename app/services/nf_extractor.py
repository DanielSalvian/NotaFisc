from services.pdf_reader import PDFReaderService
from models.nota_fiscal import NotaFiscal
import re

class NFExtractor:
    
    def extract(self, pdf_path: str) -> NotaFiscal:
        pdf = PDFReaderService()
        text_raw = pdf.read_pdf(pdf_path)
        
        if not text_raw or text_raw.strip() == "":
            text_raw = pdf.ocrread(pdf_path)

        # Se ainda não houver texto, retorna NotaFiscal vazio
        if not text_raw or text_raw.strip() == "":
            return NotaFiscal()

        def extrair(pattern, texto):
            match = re.search(pattern, texto, re.MULTILINE)
            return match.group(1).strip() if match else None

        numero = extrair(r"Numero\s*[:\-]?\s*(\d+)", text_raw)
        cnpj = extrair(r"CNPJ\s*[:\-]?\s*([0-9]{2}\.?[0-9]{3}\.?[0-9]{3}/?[0-9]{4}-?[0-9]{2})", text_raw)
        data_emissao = extrair(r"Data[\s_]*Emissao\s*[:\-]?\s*([0-9/\-]+)", text_raw)
        valor = extrair(r"Valor\s*[:\-]?\s*([0-9.,]+)", text_raw)
        
        if valor:
            valor = valor.replace('.', '').replace(',', '.')
            try:
                valor = float(valor)
            except ValueError:
                valor = None

        nf = NotaFiscal(
            numero=numero,
            cnpj=cnpj,
            data_emissao=data_emissao,
            valor=valor
        )
        return nf