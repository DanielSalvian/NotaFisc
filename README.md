# Projeto Leitor de Nota Fiscal

Este projeto tem como objetivo **ler um arquivo PDF de nota fiscal**, **extrair informações importantes** e **retornar esses dados no arquivo principal (`main.py`)**, inicialmente por `print`.

---

## Objetivo do projeto

A ideia principal é:

1. Receber uma nota fiscal em PDF
2. Ler o conteúdo do arquivo
3. Extrair os dados importantes
4. Retornar essas informações na aplicação principal

Exemplos de dados que podem ser extraídos:
- número da nota
- data de emissão
- CNPJ do emissor
- razão social
- valor total
- impostos
- outros campos que existirem no documento

---

# Estrutura do projeto

```bash
NOTAFISCAL/
├── .github/
├── app/
│   ├── models/
│   │   └── nota_fiscal.py
│   ├── services/
│   │   ├── nf_extractor.py
│   │   └── pdf_reader.py
│   └── main.py
├── pdfs/
├── venv/
├── .gitignore
├── README.md
└── requirements.txt
Explicação de cada pasta e arquivo
.github/

Essa pasta é usada para configurações do GitHub, principalmente automações.

Normalmente ela pode conter:

workflows de CI/CD
testes automáticos
validações ao fazer push ou pull request

Exemplo:

rodar testes automaticamente no GitHub Actions

Se você ainda não estiver usando automações, ela pode ficar vazia ou ser usada no futuro.

app/

Essa é a pasta principal da aplicação.

Ela concentra o código Python do projeto.

A ideia dela é organizar melhor o sistema, separando:

modelos
serviços
ponto de entrada da aplicação
app/models/

Essa pasta guarda as models do sistema.

Uma model representa a estrutura dos dados que você quer manipular.

No seu caso, a model serve para representar os dados de uma nota fiscal de forma organizada.

app/models/nota_fiscal.py

Esse arquivo define a estrutura de uma nota fiscal em Python.

Exemplo de dados que ele pode ter:

número
data de emissão
CNPJ
razão social
valor total

Ou seja, em vez de trabalhar com várias variáveis soltas, você agrupa tudo em um único objeto.

Exemplo conceitual:

nota.numero
nota.valor_total
nota.data_emissao

Isso ajuda a deixar o código mais limpo e organizado.

app/services/

Essa pasta guarda os serviços da aplicação.

Serviços são classes ou funções responsáveis pela lógica do sistema.

No seu projeto, essa pasta separa bem duas responsabilidades:

ler o PDF
extrair os dados da nota
app/services/pdf_reader.py

Esse arquivo é responsável por ler o PDF.

Função dele:

localizar o arquivo PDF
abrir o PDF
extrair o texto bruto das páginas
devolver esse texto para o restante do sistema

Ele não deve decidir quais campos da nota serão usados.
A função dele é só ler o documento.

Resumo:

entrada: arquivo PDF
saída: texto extraído do PDF
app/services/nf_extractor.py

Esse arquivo é responsável por extrair os dados importantes do texto da nota fiscal.

Depois que o pdf_reader.py lê o PDF e retorna o texto, o nf_extractor.py pega esse conteúdo e procura informações específicas, como:

número da nota
data
CNPJ
valor total

Ele pode usar:

regex
busca por palavras-chave
validações
tratamento de texto

Resumo:

entrada: texto bruto extraído do PDF
saída: dados organizados da nota fiscal

Esse arquivo é onde fica a regra de negócio da extração.

app/main.py

Esse é o ponto de entrada da aplicação.

É o arquivo principal que executa o fluxo do projeto.

Ele normalmente será responsável por:

chamar o leitor do PDF
receber o texto extraído
chamar o extrator da nota
receber os dados organizados
exibir o resultado com print

Ou seja, o main.py não deve conter toda a lógica.
Ele deve apenas orquestrar o processo.

Exemplo do fluxo:

ler pdf -> extrair dados -> mostrar resultado
pdfs/

Essa pasta armazena os arquivos PDF que serão lidos pelo sistema.

Por exemplo:

notas fiscais de teste
documentos reais para processamento
arquivos usados durante o desenvolvimento

Exemplo:

pdfs/notafiscal.pdf

A ideia é deixar os PDFs separados do código-fonte.

venv/

Essa pasta é o ambiente virtual do Python.

Ela serve para instalar as dependências do projeto sem misturar com o Python global da sua máquina.

Dentro dela ficam:

bibliotecas instaladas
executáveis do ambiente
configurações do ambiente virtual

Normalmente:

você usa, mas não edita manualmente
ela não deve ser enviada para o GitHub
.gitignore

Esse arquivo diz ao Git quais arquivos e pastas ele não deve versionar.

No seu projeto, ele é importante para ignorar coisas como:

venv/
__pycache__/
arquivos temporários
arquivos locais do sistema

Exemplo comum:

venv/
__pycache__/
*.pyc

Isso evita subir arquivos desnecessários para o repositório.

README.md

Esse é o arquivo de documentação principal do projeto.

Ele serve para explicar:

o que o projeto faz
como ele está organizado
como executar
quais dependências instalar
qual é o fluxo da aplicação

Esse arquivo é importante para você e para qualquer outra pessoa entender rapidamente o projeto.

requirements.txt

Esse arquivo lista as bibliotecas que o projeto precisa para funcionar.

Exemplo:

pypdf

Se no futuro você usar outras bibliotecas, elas também entrarão aqui.

Para instalar as dependências, normalmente usa:

pip install -r requirements.txt
Fluxo do projeto

O funcionamento esperado é:

PDF da nota fiscal
    ↓
pdf_reader.py lê o arquivo
    ↓
nf_extractor.py extrai os campos importantes
    ↓
nota_fiscal.py organiza os dados em uma model
    ↓
main.py imprime os resultados
Exemplo da responsabilidade de cada parte
pdf_reader.py

Responsável por:

abrir o PDF
ler páginas
transformar em texto
nf_extractor.py

Responsável por:

procurar número da nota
procurar valor total
procurar data
montar os dados extraídos
nota_fiscal.py

Responsável por:

representar os dados da nota em um objeto
main.py

Responsável por:

executar o fluxo todo