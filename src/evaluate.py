import pandas as pd

df = pd.read_csv("data/sampled_responses.csv")

def score_response(text):
    score = 0
    keywords = ["ai", "intelligence", "learn", "data"]
    for k in keywords:
        if k in text.lower():
            score += 1
    if len(text.split()) > 6:
        score += 1
    return score

df["score"] = df["response"].apply(score_response)

best = df.loc[df.groupby("prompt")["score"].idxmax()]
best.to_csv("output/scored_responses.csv", index=False)

print("RLHF-style evaluation completed.")
