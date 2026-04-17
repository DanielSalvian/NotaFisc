from nf.calculo import NotaFiscal

def test_conta():
    nf = NotaFiscal()
    assert nf.calcularimposto(10) == 11