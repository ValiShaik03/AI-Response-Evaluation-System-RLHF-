# AI Response Evaluation (RLHF Simulation)

This project demonstrates a simplified Reinforcement Learning from Human Feedback (RLHF)
evaluation workflow using a real-world Kaggle NLP dataset.

Instead of training a model, the focus is on **human-style evaluation of AI-generated responses**,
which is a core responsibility in AI data and RLHF roles.

---

## 📌 Project Overview

Large Language Models often generate multiple responses for a given prompt.
Human feedback is required to evaluate these responses for quality, correctness, and relevance.

This project:
- Uses real questions from a Kaggle dataset (Quora Question Pairs)
- Simulates multiple AI-generated responses per prompt
- Applies rule-based scoring to represent human judgment
- Selects the best response per prompt

---

## 📂 Dataset

- Source: Kaggle (Quora Question Pairs – public dataset)
- Column used: `question1`
- Only a small sample of the dataset is used for demonstration

---

## ⚙️ Workflow

1. Load real-world prompts from Kaggle
2. Simulate multiple AI responses per prompt
3. Score responses based on relevance and clarity
4. Select the highest-quality response (human preference simulation)
5. Save evaluated outputs

---

## 🛠 Tools & Technologies

- Python
- Pandas
- CSV-based data processing

---

## 📁 Folder Structure

```
ai_response_evaluation/
│
├── data/
│ ├── kaggle_raw.csv
│ └── sampled_responses.csv
│
├── src/
│ ├── prepare_data.py
│ └── evaluate.py
│
├── output/
│ └── scored_responses.csv
│
├── requirements.txt
└── README.md
```


---

## 🚀 How to Run

```bash
pip install pandas
python src/prepare_data.py
python src/evaluate.py
```

🎯 Key Learning Outcomes

Understanding RLHF-style evaluation pipelines

Handling real-world dataset schema issues

Applying structured human feedback to AI outputs

Ensuring data quality and consistency
