from dataclasses import dataclass

@dataclass
class NotaFiscal:
    numero: str | None = None
    data_emissao: str | None = None
    cnpj: str | None = None
    valor: float | None = None
    