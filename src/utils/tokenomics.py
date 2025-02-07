import os
import matplotlib.pyplot as plt

# Data
categories = ["Marketing", "Development", "Liquidity", "Reserve Fund", "Team Allocation"]
values = [20, 30, 25, 15, 10]
colors = ["#00ffee", "#0000ee", "#ffea00", "#00ff00", "#ff0043"]

# Base directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Assets directory
assets_dir = os.path.join(base_dir, "assets")

# Ensure the assets directory exists
os.makedirs(assets_dir, exist_ok=True)

# Path to save the chart
save_path = os.path.join(assets_dir, "mariaai_tokenomics_chart_doughnut.png")

# Create a doughnut chart
fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(
    values,
    labels=categories,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(width=0.4, edgecolor='w'),
    colors=colors,
    textprops=dict(color="black")
)

# Add a central label
ax.text(0, 0, "MariaAI\nTokenomics", ha='center', va='center', fontsize=14, fontweight='bold', color="#333")

# Customize text appearance
plt.setp(autotexts, size=10, weight="bold")
ax.set_title("MariaAI Tokenomics", fontsize=16, fontweight='bold', color="#333")

# Equal aspect ratio ensures the chart is circular
ax.axis('equal')

# Save the chart
plt.savefig(save_path, dpi=300, bbox_inches='tight')
print(f"Tokenomics doughnut chart saved to {save_path}")

