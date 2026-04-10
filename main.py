from nf.nfread import NotaFiscal

def main():
    nf = NotaFiscal()
    valor = nf.imposto(50)
    print(f"Valor com imposto: {valor}")

if __name__ == "__main__":
    main()