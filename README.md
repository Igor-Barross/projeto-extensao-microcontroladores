# Análise de dados sobre uso de tecnologia e dispositivos inteligentes na comunidade

Projeto de extensão desenvolvido na disciplina **Programação de Microcontroladores**, com foco na coleta, tratamento e análise de dados sobre o uso de tecnologia e dispositivos inteligentes em uma comunidade.

A proposta do projeto foi construir um diagnóstico simples e realista, dentro da realidade de um estudante EAD sem kit físico de hardware, conectando conceitos de Internet das Coisas (IoT), microcontroladores e análise de dados com uma demanda sociocomunitária.

## Objetivo do projeto

O objetivo deste projeto é investigar como pessoas da comunidade utilizam tecnologia no dia a dia, quais dispositivos inteligentes possuem em casa, se conhecem o conceito de IoT e se percebem riscos de segurança relacionados a esses dispositivos.

Além disso, o projeto busca transformar esses dados em informações organizadas por meio de Python, planilhas, limpeza de dados e visualizações gráficas, aproximando a disciplina de microcontroladores de uma aplicação social viável mesmo sem laboratório físico.

## Problema investigado

Muitas pessoas utilizam dispositivos conectados e inteligentes no cotidiano, mas nem sempre conhecem o conceito de IoT, o papel dos microcontroladores nesses dispositivos ou os riscos relacionados à privacidade e à segurança digital.

Diante disso, o projeto buscou levantar dados reais da comunidade para compreender esse cenário e gerar uma base para futuras ações educativas, como materiais explicativos, conscientização e oficinas introdutórias.

## Metodologia

A pesquisa foi realizada com um formulário online criado no Google Forms, aplicado a participantes da comunidade por meios digitais, como redes sociais e contatos próximos.

Após a coleta, os dados foram exportados para CSV e organizados em três etapas principais:

1. **Exploração inicial dos dados**: leitura do arquivo bruto e entendimento das perguntas e respostas coletadas
2. **Limpeza e tratamento**: padronização dos nomes das colunas e preparação do arquivo final para análise
3. **Análise dos resultados**: geração de KPIs e gráficos para interpretar o perfil da amostra e o comportamento tecnológico dos participantes.

## Estrutura do projeto

```text
.
├── data/
│   ├── raw/
│   │   └── respostas_google_forms.csv
│   └── processed/
│       └── respostas_tratadas.csv
├── docs/
├── evidences/
├── notebooks/
│   ├── 01_exploracao_inicial.ipynb
│   ├── 02_limpeza_tratamento.ipynb
│   └── 03_analise_resultados.ipynb
├── outputs/
├── src/
│   ├── config.py
│   ├── load_data.py
│   ├── clean_data.py
│   ├── analyze_data.py
│   ├── visualize_data.py
│   └── main.py
└── README.md
```

## Etapas dos notebooks

### 1. Exploração inicial

No notebook `01_exploracao_inicial.ipynb`, foi feita a leitura do arquivo bruto gerado pelo Google Forms e a inspeção inicial das colunas, respostas e estrutura geral do conjunto de dados

### 2. Limpeza e tratamento

No notebook `02_limpeza_tratamento.ipynb`, as colunas do formulário foram renomeadas para nomes mais curtos e adequados ao uso em Python, gerando uma base tratada para as análises seguintes.

### 3. Análise dos resultados

No notebook `03_analise_resultados.ipynb`, foram criados gráficos e indicadores para responder às perguntas centrais do projeto, como faixa etária predominante, uso de dispositivos, presença de dispositivos inteligentes, conhecimento sobre IoT, percepção de risco e participação em cursos de tecnologia.

## Resultados principais

Com base nos dados coletados, observou-se que a amostra foi formada majoritariamente por participantes de 18 a 24 anos, com poucos respondentes em outras faixas etárias.

Todos os participantes declararam ter acesso frequente à internet, o que mostra que a conectividade já faz parte da realidade do grupo pesquisado.

Entre os dispositivos mais utilizados no dia a dia, o celular/smartphone apareceu com maior frequência, seguido por notebook/laptop e computador de mesa.

Em relação aos dispositivos inteligentes em casa, a Smart TV foi o item mais comum, seguida por relógios inteligentes e caixas de som inteligentes, enquanto poucos participantes afirmaram não possuir nenhum dispositivo desse tipo.

A análise também mostrou que a maioria dos participantes não conhece o conceito de IoT, mesmo utilizando tecnologias relacionadas a esse universo.

Quanto à segurança, as respostas ficaram divididas, indicando que parte dos respondentes percebe riscos em dispositivos inteligentes, enquanto outra parte ainda não reconhece esse problema com clareza.

Por fim, uma parcela significativa dos participantes afirmou já ter feito algum curso de tecnologia, informática ou programação.

## Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook
- Google Forms
- CSV

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Igor-Barross/projeto-extensao-microcontroladores.git
cd projeto-extensao-microcontroladores
```

### 2. Criar e ativar um ambiente virtual

```bash
python -m venv venv
```

* [ ] No Windows:

```bash
venv\Scripts\activate
```

No Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install pandas matplotlib seaborn jupyter
```

### 4. Executar o pipeline principal

```bash
python src/main.py
```

### 5. Abrir os notebooks

```bash
jupyter notebook
```

## Possíveis desdobramentos

Os resultados deste projeto podem servir de base para ações futuras de extensão, como produção de material educativo sobre IoT, explicações introdutórias sobre microcontroladores, conscientização sobre segurança digital e novas coletas com públicos maiores ou mais específicos.

## Evidências

* [ ] As evidências do projeto incluem prints do formulário utilizado, divulgação da pesquisa em rede social, registros das respostas coletadas, gráficos gerados na análise e organização do repositório no GitHub.

## Autor

Projeto desenvolvido por estudante de Ciência da Computação, no contexto da disciplina **Programação de Microcontroladores (EAD)**.
