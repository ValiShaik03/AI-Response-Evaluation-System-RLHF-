import pandas as pd

# Load Kaggle dataset
df = pd.read_csv("data/kaggle_raw.csv")

# Use question1 as prompt
df = df.rename(columns={"question1": "prompt"})

# Keep only prompt column
df = df[["prompt"]].dropna().head(10)

responses = []

for _, row in df.iterrows():
    prompt = row["prompt"]

    responses.append([prompt, 1, f"{prompt} explained using AI concepts"])
    responses.append([prompt, 2, "Short definition related to AI"])
    responses.append([prompt, 3, "Unrelated response"])

out = pd.DataFrame(
    responses,
    columns=["prompt", "response_id", "response"]
)

out.to_csv("data/sampled_responses.csv", index=False)

print("✅ Data prepared successfully.")
