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



# Plot the number of individual speakers for each gender
plt.figure(figsize=(8, 6))

# Plot: Distribution of Genders
gender_counts = vox_meta['Gender'].value_counts()
gender_counts.plot(kind='bar')
plt.title('Distribution of Genders')
plt.xlabel('Gender')
plt.ylabel('Number of Speakers')

plt.tight_layout()
plt.show()

set_counts = vox_meta['Set'].value_counts()
plt.figure(figsize=(8, 6))
set_counts.plot(kind='bar')
plt.title('Distribution of Speakers Across Sets')
plt.xlabel('Set')
plt.ylabel('Number of Speakers')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()


