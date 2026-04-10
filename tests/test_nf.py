from nf.nfread import NotaFiscal

def test_conta():
    nf = NotaFiscal()
    assert nf.imposto(10) == 11