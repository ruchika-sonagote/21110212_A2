import pandas as pd
import os
import matplotlib.pyplot as plt

main_folder = "/home/ruchika/Lab_7_8"
repos = ["redis-py", "chatgpt", "imgaug"]
df_cwe = pd.DataFrame()

for repo in repos:
    csv_path = os.path.join(main_folder, repo, "bandit_cwe_report.csv")
    if os.path.exists(csv_path):
        try:
            df = pd.read_csv(csv_path, on_bad_lines="skip")
            df = df.dropna(subset=["Unique CWEs"])
            df["Unique CWEs"] = df["Unique CWEs"].astype(str).str.split(",")
            df = df.explode("Unique CWEs")
            df["Unique CWEs"] = df["Unique CWEs"].str.strip()
            df["Unique CWEs"] = pd.to_numeric(df["Unique CWEs"], errors="coerce")
            cwe_counts = df["Unique CWEs"].value_counts().reset_index()
            cwe_counts.columns = ["Unique CWEs", "Frequency"]
            df_cwe = pd.concat([df_cwe, cwe_counts], ignore_index=True)
        except Exception as e:
            print(f"Error processing {repo}: {e}")

if not df_cwe.empty:
    df_cwe = df_cwe.groupby("Unique CWEs", as_index=False).sum()
    df_cwe = df_cwe.sort_values(by="Frequency", ascending=False)
    output = os.path.join(main_folder, "CWE_Frequency.csv")
    df_cwe.to_csv(output, index=False)
    print(f"CWE frequency report saved to: {output}")
    plt.figure(figsize=(10, 6))
    bars = plt.bar(df_cwe["Unique CWEs"].astype(str), df_cwe["Frequency"], color="skyblue")
    plt.xticks(rotation=45)
    plt.xlabel("CWE ID")
    plt.ylabel("Frequency")
    plt.title("CWE Frequency across Repositories")
    plt.tight_layout()

    for bar in bars:
        plt.text(
            bar.get_x() + bar.get_width() / 2 - 0.1,
            bar.get_height() + 0.1,
            f"{int(bar.get_height())}",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
            color="black",
        )
    plot_output = os.path.join(main_folder, "RQ3.png")
    plt.savefig(plot_output)
    print(f"CWE frequency plot saved to: {plot_output}")

else:
    print("No valid data found across repositories.")
