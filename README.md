# 🤖 FinIA — Assistente de Relacionamento Financeiro

Protótipo de um assistente virtual com IA generativa, desenvolvido para o Lab da DIO.

## Estrutura

```text
finia_assistente/
├── data/
│   ├── historico_atendimento.csv
│   ├── perfil_investidor.json
│   ├── produtos_financeiros.json
│   └── transacoes.csv
├── src/
│   └── app.py
├── .streamlit/
│   └── secrets.toml.example
├── .gitignore
└── requirements.txt
```

## Como executar

### 1. Criar ambiente virtual

```bash
python -m venv .venv
```

### 2. Ativar o ambiente

No Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar a chave da API

Copie `.streamlit/secrets.toml.example` para `.streamlit/secrets.toml` e preencha a chave da API Gemini.

**Nunca publique esse arquivo no GitHub.** O `.gitignore` já o protege.

### 5. Executar

```bash
streamlit run src/app.py
```

## Fluxo do sistema

```text
Pessoa usuária
      ↓
Interface Streamlit
      ↓
Python carrega CSV/JSON
      ↓
Python resume e organiza o contexto
      ↓
System Prompt + contexto + histórico
      ↓
Gemini
      ↓
Resposta contextualizada
```

## Tecnologias

- Python
- Streamlit
- Pandas
- Google GenAI SDK
- Gemini

## Observação sobre os dados

Os arquivos de dados são mockados para o desafio. Valores de rentabilidade e condições presentes nos arquivos não devem ser tratados como informações atuais de mercado.
