import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.cm import Greens

# Create a dictionary for the data
data = {
    "Tested parameter": [
        "num-agents", "num-agents", "num-agents", "num-agents",
        "Percentage of influencers [%]", "Percentage of influencers [%]", "Percentage of influencers [%]", "Percentage of influencers [%]", "Percentage of influencers [%]",
        "Price", "Price", "Price", "Price", "Price",
        "Quality", "Quality", "Quality", "Quality", "Quality",
        "Attribute value", "Attribute value", "Attribute value", "Attribute value", "Attribute value", "Attribute value", "Attribute value",
        "campaign-freq", "campaign-freq", "campaign-freq", "campaign-freq",
        "Reach of campaigns [%]", "Reach of campaigns [%]", "Reach of campaigns [%]", "Reach of campaigns [%]", "Reach of campaigns [%]"
    ],
    "Parameter value": [
        250, 500, 750, 1000,
        1, 2, 3, 4, 5,
        20, 40, 60, 80, 100,
        20, 40, 60, 80, 100,
        33, 44, 55, 66, 77, 88, 99,
        500, 1000, 2500, 5000,
        2, 4, 6, 8, 10
    ],
    "% of green": [
        10.49, 22.02, 30.5, 37.28,
        8.24, 15.54, 22.15, 27.07, 31.82,
        18.82, 20.69, 22.76, 26.76, 28.33,
        18.79, 20.18, 22.74, 26.99, 26.96,
        19.13, 21.47, 22.68, 23.19, 24.63, 27.06, 28.01,
        31.5, 24.95, 21.82, 21.71,
        21.71, 21.75, 22.3, 21.99, 22.91
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define markers and marker size
markers = ['o', 's', '^', 'D', 'v', 'p', '*', 'h', 'x']
marker_size = 170

# Define font properties
font_properties = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 18}

# Plot 1: num-agents
fig, ax = plt.subplots(figsize=(8, 6))
subset1 = df[df["Tested parameter"] == "num-agents"]
for i, param in enumerate(subset1["Tested parameter"].unique()):
    subset = subset1[subset1["Tested parameter"] == param]
    ax.scatter(subset["Parameter value"], subset["% of green"], marker=markers[i % len(markers)], s=marker_size, color=Greens(0.7), label=f"{param} - % of green", zorder=5)

ax.set_xlabel("Number of agents", fontdict=font_properties)
ax.set_ylabel("Percentage of green agents [%]", fontdict=font_properties)
#ax.set_title("% of Green by Tested Parameter (num-agents)", fontdict=font_properties)
#ax.legend()
ax.tick_params(axis='both', which='major', labelsize=14)
ax.grid(True)
plt.tight_layout()
plt.savefig('num_agents.png')
plt.show()
plt.close()

# Plot 2: %-of-influencers, campaign-reach
fig, ax = plt.subplots(figsize=(8, 6))
subset2 = df[df["Tested parameter"].isin(["Percentage of influencers [%]", "Reach of campaigns [%]"])]
for i, param in enumerate(subset2["Tested parameter"].unique()):
    subset = subset2[subset2["Tested parameter"] == param]
    ax.scatter(subset["Parameter value"], subset["% of green"], marker=markers[i % len(markers)], s=marker_size, color=Greens(0.7), label=f"{param}",zorder=5)

ax.set_xlabel("Parameter value", fontdict=font_properties)
ax.set_ylabel("Percentage of green agents [%]", fontdict=font_properties)
#ax.set_title("% of Green by Tested Parameter (%-of-influencers, campaign-reach)", fontdict=font_properties)
ax.legend(prop={'size': 16})
ax.tick_params(axis='both', which='major', labelsize=14)
ax.grid(True)
plt.tight_layout()
plt.savefig('influencers_campaign_reach.png')
plt.show()
plt.close()

# Plot 3: price, quality, attr-value
fig, ax = plt.subplots(figsize=(8, 6))
subset3 = df[df["Tested parameter"].isin(["Price", "Quality", "Attribute value"])]
for i, param in enumerate(subset3["Tested parameter"].unique()):
    subset = subset3[subset3["Tested parameter"] == param]
    ax.scatter(subset["Parameter value"], subset["% of green"], marker=markers[i % len(markers)], s=marker_size, color=Greens(0.7), label=f"{param}",zorder=5)

ax.set_xlabel("Parameter value", fontdict=font_properties)
ax.set_ylabel("Percentage of green agents [%]", fontdict=font_properties)
#ax.set_title("% of Green by Tested Parameter (price, quality, attr-value)", fontdict=font_properties)
ax.legend(prop={'size': 16})
ax.tick_params(axis='both', which='major', labelsize=14)
ax.grid(True)
plt.tight_layout()
plt.savefig('price_quality_attr_value.png')
plt.show()
plt.close()

# Plot 4: campaign-freq
fig, ax = plt.subplots(figsize=(8, 6))
subset4 = df[df["Tested parameter"] == "campaign-freq"]
for i, param in enumerate(subset4["Tested parameter"].unique()):
    subset = subset4[subset4["Tested parameter"] == param]
    ax.scatter(subset["Parameter value"], subset["% of green"], marker=markers[i % len(markers)], s=marker_size, color=Greens(0.7), label=f"{param} - % of green",zorder=5)

ax.set_xlabel("Frequency of campaigns", fontdict=font_properties)
ax.set_ylabel("Percentage of green agents [%]", fontdict=font_properties)
#ax.set_title("% of Green by Tested Parameter (campaign-freq)", fontdict=font_properties)
#ax.legend()
ax.tick_params(axis='both', which='major', labelsize=14)
ax.grid(True)
plt.tight_layout()
plt.savefig('campaign_freq.png')
plt.show()
plt.close()
