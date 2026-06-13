# Análise de dados sobre uso de tecnologia e dispositivos inteligentes na comunidade

Projeto de extensão desenvolvido na disciplina **Programação de Microcontroladores**, com foco na coleta, tratamento e análise de dados sobre o uso de tecnologia e dispositivos inteligentes em uma comunidade.

A proposta do projeto foi construir um diagnóstico simples e realista, dentro da realidade de um estudante EAD sem kit físico de hardware, conectando conceitos de Internet das Coisas (IoT), microcontroladores e análise de dados com uma demanda sociocomunitária.[file:1][file:21][file:23][file:22]

## Objetivo do projeto

O objetivo deste projeto é investigar como pessoas da comunidade utilizam tecnologia no dia a dia, quais dispositivos inteligentes possuem em casa, se conhecem o conceito de IoT e se percebem riscos de segurança relacionados a esses dispositivos.[file:1][file:22]

Além disso, o projeto busca transformar esses dados em informações organizadas por meio de Python, planilhas, limpeza de dados e visualizações gráficas, aproximando a disciplina de microcontroladores de uma aplicação social viável mesmo sem laboratório físico.[file:21][file:23][file:22]

## Problema investigado

Muitas pessoas utilizam dispositivos conectados e inteligentes no cotidiano, mas nem sempre conhecem o conceito de IoT, o papel dos microcontroladores nesses dispositivos ou os riscos relacionados à privacidade e à segurança digital.[file:1][file:18][file:19]

Diante disso, o projeto buscou levantar dados reais da comunidade para compreender esse cenário e gerar uma base para futuras ações educativas, como materiais explicativos, conscientização e oficinas introdutórias.[file:1][file:22]

## Metodologia

A pesquisa foi realizada com um formulário online criado no Google Forms, aplicado a participantes da comunidade por meios digitais, como redes sociais e contatos próximos.[file:21][file:23]

Após a coleta, os dados foram exportados para CSV e organizados em três etapas principais:[file:21][file:23][file:22]

1. **Exploração inicial dos dados**: leitura do arquivo bruto e entendimento das perguntas e respostas coletadas.[file:21]
2. **Limpeza e tratamento**: padronização dos nomes das colunas e preparação do arquivo final para análise.[file:23][file:26]
3. **Análise dos resultados**: geração de KPIs e gráficos para interpretar o perfil da amostra e o comportamento tecnológico dos participantes.[file:22]

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

No notebook `01_exploracao_inicial.ipynb`, foi feita a leitura do arquivo bruto gerado pelo Google Forms e a inspeção inicial das colunas, respostas e estrutura geral do conjunto de dados.[file:21]

### 2. Limpeza e tratamento

No notebook `02_limpeza_tratamento.ipynb`, as colunas do formulário foram renomeadas para nomes mais curtos e adequados ao uso em Python, gerando uma base tratada para as análises seguintes.[file:23][file:26]

### 3. Análise dos resultados

No notebook `03_analise_resultados.ipynb`, foram criados gráficos e indicadores para responder às perguntas centrais do projeto, como faixa etária predominante, uso de dispositivos, presença de dispositivos inteligentes, conhecimento sobre IoT, percepção de risco e participação em cursos de tecnologia.[file:22][file:1]

## Resultados principais

Com base nos dados coletados, observou-se que a amostra foi formada majoritariamente por participantes de 18 a 24 anos, com poucos respondentes em outras faixas etárias.[file:14][file:1]

Todos os participantes declararam ter acesso frequente à internet, o que mostra que a conectividade já faz parte da realidade do grupo pesquisado.[file:15][file:1]

Entre os dispositivos mais utilizados no dia a dia, o celular/smartphone apareceu com maior frequência, seguido por notebook/laptop e computador de mesa.[file:16][file:1]

Em relação aos dispositivos inteligentes em casa, a Smart TV foi o item mais comum, seguida por relógios inteligentes e caixas de som inteligentes, enquanto poucos participantes afirmaram não possuir nenhum dispositivo desse tipo.[file:17][file:1]

A análise também mostrou que a maioria dos participantes não conhece o conceito de IoT, mesmo utilizando tecnologias relacionadas a esse universo.[file:18][file:1]

Quanto à segurança, as respostas ficaram divididas, indicando que parte dos respondentes percebe riscos em dispositivos inteligentes, enquanto outra parte ainda não reconhece esse problema com clareza.[file:19][file:1]

Por fim, uma parcela significativa dos participantes afirmou já ter feito algum curso de tecnologia, informática ou programação.[file:20][file:1]

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
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

### 2. Criar e ativar um ambiente virtual

```bash
python -m venv venv
```

No Windows:

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

Os resultados deste projeto podem servir de base para ações futuras de extensão, como produção de material educativo sobre IoT, explicações introdutórias sobre microcontroladores, conscientização sobre segurança digital e novas coletas com públicos maiores ou mais específicos.[file:22][file:7]

## Evidências

As evidências do projeto incluem prints do formulário utilizado, divulgação da pesquisa em rede social, registros das respostas coletadas, gráficos gerados na análise e organização do repositório no GitHub.[file:21][file:22]

## Autor

Projeto desenvolvido por estudante de Ciência da Computação, no contexto da disciplina **Programação de Microcontroladores (EAD)**.
