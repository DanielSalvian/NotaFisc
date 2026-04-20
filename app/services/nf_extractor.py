from pdf_reader import PDFReaderService

class nfExtractor:
    
    pdf = PDFReaderService()
    text = pdf.read_pdf("notafiscal.pdf")
    print(text)