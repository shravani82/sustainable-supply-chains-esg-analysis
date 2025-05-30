from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Select features related to ESG scores (replace with your actual columns)
features = ['Environmental_Score', 'Social_Score', 'Governance_Score']

X = df[features]

# Scale features for clustering
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Find optimal number of clusters with elbow method
sse = []
for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    sse.append(kmeans.inertia_)

plt.figure(figsize=(8,4))
plt.plot(range(1,10), sse, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('SSE')
plt.title('Elbow Method for Optimal k')
plt.show()

# Assume optimal k=3
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Visualize clusters (2D scatter of two ESG scores)
sns.scatterplot(x='Environmental_Score', y='Social_Score', hue='Cluster', data=df, palette='Set2')
plt.title('ESG Clusters')
plt.show()

# Now label clusters manually based on domain knowledge:
# For example, cluster 0 = Sustainable Leaders, cluster 1 = Moderate, cluster 2 = High-Risk
