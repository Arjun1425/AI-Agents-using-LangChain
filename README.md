# LangChain Learning Repository

A hands-on learning repository covering the core concepts of [LangChain](https://www.langchain.com/) — from basic LLM calls to building production-style Retrieval-Augmented Generation (RAG) systems and autonomous AI agents.

Each numbered folder is a self-contained module that builds on the previous one. Code is organized as Jupyter notebooks (for step-by-step exploration) and standalone Python scripts (for runnable demos and UIs).

## Table of Contents

1. [LLMs](#1-llms) — Basic LLM usage
2. [Chat Models](#2-chat-models) — OpenAI and Hugging Face chat models
3. [Embedding Models](#3-embedding-models) — Text embeddings and document similarity
4. [Prompts](#4-prompts) — Prompt templates and a Streamlit prompt UI
5. [Structured Output](#5-structured-output) — Typed outputs with TypedDict / Pydantic
6. [Chains](#6-chains) — Composing LLM calls into pipelines
7. [Runnables](#7-runnables) — The LangChain Expression Language (LCEL)
8. [RAG](#8-rag) — Document loaders, text splitters, vector stores, and retrievers
9. [AI Agents](#9-ai-agents) — Tools, tool calling, and autonomous agents

## Tech Stack

- **LangChain** (core, community, integrations)
- **LLM Providers**: OpenAI, Anthropic, Google Gemini, Hugging Face
- **Vector Store**: Chroma
- **Utilities**: NumPy, scikit-learn, python-dotenv
- **Notebooks**: Jupyter

## Repository Structure

```
LangChain/
├── 1. LLMs/                      # Vanilla LLM demo
├── 2. ChatModels/                # OpenAI + Hugging Face chat models
├── 3. EmbeddedModels/            # Embeddings and similarity search
├── 4. Prompts/                   # Prompt templates and Streamlit UI
├── 5. Structured_Output/         # Typed LLM outputs
├── 6. Chains/                    # Chaining LLM calls
├── 7. Runnables/                 # LCEL runnables
├── 8. RAG/                       # Retrieval-Augmented Generation
│   ├── 1. DocumentLoader.ipynb
│   ├── 2. TextSplitters.ipynb
│   ├── 3. VectorDatabase.ipynb
│   ├── 4. Retriever.ipynb
│   └── Youtube_chat_RAG_application_using_langchain.ipynb
├── 9. AI_agents/                 # Tools and agents
├── chatbot.ipynb                 # End-to-end chatbot example
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/LangChain.git
cd LangChain
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root with your API keys:

```env
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
GOOGLE_API_KEY=your_google_key_here
HUGGINGFACEHUB_API_TOKEN=your_hf_token_here
```

> **Note:** Never commit your `.env` file. It is listed in `.gitignore`.

### 5. Run a notebook

```bash
jupyter notebook
```

Open any notebook under the numbered folders and run the cells top to bottom.

## Module Overview

### 1. LLMs
Shows how to instantiate and call a base LLM using LangChain's `LLM` interface.

### 2. Chat Models
Demonstrates chat-oriented models (messages with roles) using both OpenAI's API and Hugging Face's inference endpoints.

### 3. Embedding Models
Covers generating embeddings for queries and documents, comparing OpenAI embeddings with locally-run Hugging Face models, and computing document similarity.

### 4. Prompts
Introduces prompt templates, few-shot prompting, and includes a small Streamlit UI (`prompt_ui.py`) that lets you experiment with prompt parameters interactively.

Run the UI with:
```bash
streamlit run "4. Prompts/prompt_ui.py"
```

### 5. Structured Output
Uses `TypedDict` and Pydantic to force the LLM to return structured, schema-validated JSON — useful for downstream parsing and tool-use scenarios.

### 6. Chains
Shows how to compose multiple LLM calls into sequential and parallel pipelines.

### 7. Runnables
Deep dive into the LangChain Expression Language (LCEL) — the composable, declarative way to build chains using `|` operators and `RunnableSequence` / `RunnableParallel`.

### 8. RAG
Walks through the full Retrieval-Augmented Generation pipeline:
- **Document Loader** — loading PDFs, text, and CSV files
- **Text Splitters** — chunking strategies
- **Vector Database** — storing embeddings in Chroma
- **Retriever** — semantic search over stored documents
- **YouTube Chat RAG** — a full application that answers questions about a YouTube video's transcript

### 9. AI Agents
Covers LangChain tools, tool calling, and building an agent that can decide which tool to use to answer a query.

## Chatbot Example

`chatbot.ipynb` at the project root ties many of these concepts together into a simple conversational chatbot with memory.

## Contributing

This is a personal learning repository, but suggestions, fixes, and additional examples are welcome. Feel free to open an issue or submit a pull request.

## License

This project is released under the MIT License. See `LICENSE` for details.

## Acknowledgements

- The [LangChain](https://github.com/langchain-ai/langchain) team for the framework and excellent documentation
- OpenAI, Anthropic, Google, and Hugging Face for their model APIs
