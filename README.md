# Software Requirement Engineering using Machine Learning Techniques

## Project Overview

This repository demonstrates the use of **Retrieval-Augmented Generation (RAG)** and **Prompt Engineering** to classify software requirements into functional (F) and non-functional requirements (NFRs). These techniques leverage Large Language Models (LLMs) to enhance classification accuracy by combining retrieval and context-aware generation.

---

## Features

### Prompt Engineering
Prompt Engineering uses optimized task-specific prompts with few-shot learning to guide the LLMs in understanding and classifying requirements effectively.

**Highlights:**
- Leverages representative examples for accurate predictions.
- Processes LLM responses with a parser for consistent output.

---

### Retrieval-Augmented Generation (RAG)
RAG improves classification by retrieving contextually relevant examples from a semantic vector database and integrating them into the prompt.

**Workflow:**
1. **Retrieve:** Use embeddings to find semantically similar examples from a database (e.g., Pinecone).
2. **Generate:** Append retrieved examples to the prompt and process through an LLM.
3. **Parse:** Ensure output aligns with predefined categories.

---

## Results

| Method                | Model                       | F1   | Accuracy |
|-----------------------|-----------------------------|------|----------|
| Prompt Engineering    | GPT-3.5-Turbo              | 96.03| 74.74    |
| RAG                   | GPT-3.5-Turbo (RAG)        | 96.63| 79.79    |

---

## Getting Started

### Prerequisites
- Python 3.x
- Jupyter Notebook
- Libraries: `transformers`, `pinecone`, `openai`, etc. (see `requirements.txt`)

## Dataset

The classification is performed using the PROMISE and PROMISE_exp datasets:

1. **PROMISE Dataset**: 
   - Contains 625 natural language software requirements.
   - Includes:
     - 255 functional requirements (F).
     - 370 non-functional requirements (NFRs) distributed across categories like security, usability, performance, etc.

2. **PROMISE_exp Dataset**:
   - An extended version of PROMISE with 969 requirements.
   - Includes:
     - 444 functional requirements (F).
     - 525 non-functional requirements (NFRs) distributed across additional categories like maintainability, scalability, and fault tolerance.

**Dataset Split**:
- Training: 80%
- Testing: 20%

**Non-Functional Categories in PROMISE_exp**:
| Category         | Count |
|-------------------|-------|
| Availability (A)  | 31    |
| Fault Tolerance (FT) | 18 |
| Legal (L)         | 15    |
| Look & Feel (LF)  | 49    |
| Maintainability (MN) | 24 |
| Operability (O)   | 77    |
| Performance (PE)  | 67    |
| Scalability (SC)  | 22    |
| Security (SE)     | 125   |
| Usability (US)    | 85    |
| Portability (PO)  | 12    |
| Total             | 969   |

The dataset provides a comprehensive basis for training and testing, ensuring diverse and real-world software requirement scenarios are covered.

## Model Architectures

![alt text](https://github.com/NimaMeghdadi/Software-Requirement-Engineering-using-Machine-Learning-Techniques/blob/main/rag_arcitecture.png)

---

## Usage
You can [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NimaMeghdadi/Software-Requirement-Engineering-using-Machine-Learning-Techniques/).

---
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
