# Consolidador de Planilhas Excel
Este projeto em Python tem como objetivo consolidar múltiplas planilhas Excel (.xlsx) em um único relatório consolidado, adicionando contexto (como segmento e país) e facilitando análises posteriores.

## 📋 Funcionalidades
Leitura e consolidação de arquivos Excel (.xlsx) localizados na pasta de entrada.
Tratamento de erros com registro em log (log_erros.txt).
Adição de colunas contextuais como 'Segmento' e 'País' com base no nome dos arquivos.
Exportação do relatório consolidado em um novo arquivo Excel.
## 🗂️ Estrutura do Projeto
consolidando_planilhas/
│
├── planilhas/              # Pasta contendo as planilhas a serem consolidadas.
├── log_erros.txt           # Log de erros encontrados durante o processo.
├── script_consolidador.py  # Script principal do projeto.
└── Report-consolidado-DD-MM-AA.xlsx  # Arquivo gerado ao final do processo.

## 🛠️ Pré-requisitos
Python 3.x instalado.
Pacotes necessários:
pandas
openpyxl (driver para manipulação de arquivos Excel)
### Instale as dependências com o comando:
pip install pandas openpyxl

## 🚀 Como Utilizar
Organize os arquivos:
Coloque as planilhas Excel (.xlsx) na pasta consolidando_planilhas/planilhas.

### Formato do nome dos arquivos:
Use o padrão Segmento-País.xlsx (ex.: Varejo-Brasil.xlsx).
Assim, o script pode extrair corretamente as informações de 'Segmento' e 'País'.

## Executando o script:
### Navegue até a pasta do projeto no terminal e execute:
`python script_consolidador.py`

### Verifique o relatório:
O relatório consolidado será salvo como Report-consolidado-DD-MM-AA.xlsx.

### Verifique erros:
Se algum problema ocorrer, consulte o arquivo log_erros.txt.

## 📊 Estrutura do Relatório Consolidado
O relatório terá as seguintes colunas:

Coluna	Descrição
Segmento,
País,
Produto,
Qtde de Unidades Vendidas,
Preço Unitário,
Valor Total,
Desconto,
Valor Total c/ Desconto,
Custo Total,
Lucro,
Data,  
Mês,   
Ano.

## ⚠️ Tratamento de Erros
Arquivos inválidos: Arquivos que não são .xlsx serão ignorados e registrados no log_erros.txt.
Erro de leitura: Problemas na leitura de arquivos válidos também serão registrados no log.

## 📁 Exemplo de Uso
Entrada:
Planilhas na pasta planilhas/:

Varejo-Brasil.xlsx
Atacado-Argentina.xlsx
Saída:
O relatório consolidado será salvo como Report-consolidado-27-10-24.xlsx.

## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para sugerir melhorias, abrir issues, ou enviar pull requests.

## 📝 Licença
Este projeto está licenciado sob a MIT License.

## 📬 Contato
Se tiver dúvidas ou sugestões, entre em contato!

