from nf.nfread import NotaFiscal

def main():
    nf = NotaFiscal()
    valor = nf.calcularimposto(50)
    valornf = nf.calcularvalornotafiscal(10)
    print(f"Valor com imposto: {valor}")
    print(f"Valor com imposto: {valornf}")

if __name__ == "__main__":
    main()