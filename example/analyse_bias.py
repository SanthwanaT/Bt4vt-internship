import pandas as pd
import matplotlib.pyplot as plt

# Load the VoxCeleb metadata
vox_meta_file = "~/bias_tests_4_voice_tech/example/vox1_meta.csv"
vox_meta = pd.read_csv(vox_meta_file, sep="\t")

# Group the data by country and gender, then count the number of individual speakers
speaker_counts = vox_meta.groupby(["Nationality", "Gender"])["VoxCeleb1 ID"].nunique().reset_index()
speaker_counts.columns = ["Country", "Gender", "Speaker Count"]

# Plot the number of individual speakers for each country and gender
fig, ax = plt.subplots(figsize=(12, 6))
speaker_counts.pivot(index="Country", columns="Gender", values="Speaker Count").plot(kind="bar", ax=ax)
plt.title("Number of Individual Speakers by Country and Gender")
plt.xlabel("Country")
plt.ylabel("Number of Speakers")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Gender")
plt.tight_layout()
plt.show()
