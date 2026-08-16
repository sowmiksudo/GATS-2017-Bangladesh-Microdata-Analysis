"""
Build the Jupyter Notebook for CS295 GATS 2017 Bangladesh project.
Clean academic presentation with concise sentences, 3rd-person POV, and header-only code comments.
"""
import nbformat as nbf

nb = nbf.v4.new_notebook()
nb.metadata = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    },
    "language_info": {
        "name": "python",
        "version": "3.13.0"
    }
}

cells = []

def md(source):
    cells.append(nbf.v4.new_markdown_cell(source))

def code(source):
    cells.append(nbf.v4.new_code_cell(source))


# ═══════════════════════════════════════════════════════════════
# TITLE & INTRO
# ═══════════════════════════════════════════════════════════════

md(r"""# Tobacco Use Patterns and Secondhand Smoke Exposure in Bangladesh
## Empirical Analysis of the Global Adult Tobacco Survey (GATS) 2017

**Course:** CS295 – Programming in Python  
**Semester:** Summer 2026  

**Team Members:**
| Name | Student ID |
|------|-----------|
| *Shayer Mahmud Sowmik* | *2025-3-27-022* |

---

**Dataset:** Bangladesh Global Adult Tobacco Survey (GATS) 2017  
**Source:** World Health Organization (WHO) / Centers for Disease Control and Prevention (CDC)  
**File:** `Bangla_GATS_2017_Public_use_06Spe2018.csv`

---

### Research Rationale and Background

Tobacco use is a leading cause of preventable illness and death worldwide. It causes over 8 million deaths each year (WHO, 2023). In Bangladesh, approximately 35% to 40% of adults consume tobacco products. This high prevalence creates a heavy burden on the national healthcare system.

This project supports **UN Sustainable Development Goal 3 (Good Health and Well-being)**, specifically **Target 3.a**. This target focuses on strengthening the WHO Framework Convention on Tobacco Control (FCTC).

This study examines three main areas:
1. Demographic factors linked to tobacco consumption.
2. Differences between smoked and smokeless tobacco use.
3. Rates and settings of secondhand smoke (SHS) exposure.

The goal is to provide clear empirical evidence. These findings can guide public health policy, targeted cessation programs, and stronger law enforcement.
""")

# ═══════════════════════════════════════════════════════════════
# TABLE OF CONTENTS
# ═══════════════════════════════════════════════════════════════

md(r"""## Table of Contents

1. [Setup and Data Loading](#1-setup-and-data-loading)
2. [Dataset Overview](#2-dataset-overview)
3. [Data Cleaning and Preprocessing](#3-data-cleaning-and-preprocessing)
4. [Exploratory Data Analysis](#4-exploratory-data-analysis)
   - 4.1 Overall Tobacco Use Prevalence
   - 4.2 Tobacco Use by Gender
   - 4.3 Tobacco Use by Age Group
   - 4.4 Tobacco Use by Education Level
   - 4.5 Urban vs Rural Differences
   - 4.6 Division-wise Distribution
   - 4.7 Secondhand Smoke Exposure
   - 4.8 Knowledge and Awareness
   - 4.9 Cessation Attempts
   - 4.10 Age Distribution of Tobacco Users (KDE)
   - 4.11 Smoking Initiation Age Analysis
   - 4.12 Correlation Analysis
   - 4.13 Multivariate Exploration
   - 4.14 Summary Statistics Table
5. [Key Findings and Discussion](#5-key-findings-and-discussion)
6. [Policy Implications](#6-policy-implications)
7. [Limitations](#7-limitations)
8. [Conclusion](#8-conclusion)
9. [References](#9-references)
""")

# ═══════════════════════════════════════════════════════════════
# 1  SETUP
# ═══════════════════════════════════════════════════════════════

md(r"""## 1. Setup and Data Loading <a id="1-setup-and-data-loading"></a>

This step imports the required libraries. `pandas` and `numpy` handle data processing. `matplotlib` and `seaborn` generate the charts. Global visual settings are configured for clean presentation.
""")

code(r"""# Setup and Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 120
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
sns.set_palette('Set2')
sns.set_style('whitegrid')

print("Libraries loaded successfully.")
""")

code(r"""# Load Dataset
df = pd.read_csv('Bangla_GATS_2017_Public_use_06Spe2018.csv', low_memory=False)
print(f"Dataset loaded: {df.shape[0]:,} rows x {df.shape[1]} columns")
""")

# ═══════════════════════════════════════════════════════════════
# 2  DATASET OVERVIEW
# ═══════════════════════════════════════════════════════════════

md(r"""## 2. Dataset Overview <a id="2-dataset-overview"></a>

The Global Adult Tobacco Survey (GATS) is a nationally representative household survey. It tracks adult tobacco use and key control indicators across Bangladesh.

The main survey sections are summarized below:

| Section | Code Prefix | Description / Domain |
|---------|-------------|----------------------|
| Demographics | A01–A06, AGE | Gender, age, education level, occupation |
| Tobacco Smoking | B01–B18 | Smoking status, daily frequency, initiation age |
| Smokeless Tobacco | C01–C18 | Zarda, sadapata, gul, and khaini usage |
| Cessation | D01–D16 | Quit attempts, cessation methods, clinical advice |
| Secondhand Smoke | E01–E22 | Exposure at home, work, restaurants, transport |
| Economics | F01–FB04 | Prices paid, brand choices, purchase points |
| Media | G01–G06 | Tobacco advertising and anti-tobacco messaging |
| Knowledge | H01–H05 | Public awareness of health risks |
""")

code(r"""# Dataset Dimensions and Data Types
print(f"Number of respondents (rows): {df.shape[0]:,}")
print(f"Number of variables (columns): {df.shape[1]}")
print(f"\nColumn data types:")
print(df.dtypes.value_counts())
""")

code(r"""# Missing Value Analysis
total_cells = df.shape[0] * df.shape[1]
missing_cells = df.isnull().sum().sum()
print(f"Total cells in dataset: {total_cells:,}")
print(f"Missing cells: {missing_cells:,}")
print(f"Overall missing percentage: {missing_cells / total_cells * 100:.2f}%")
print(f"\nColumns with NO missing values: {(df.isnull().sum() == 0).sum()}")
print(f"Columns with missing values: {(df.isnull().sum() > 0).sum()}")
""")

md(r"""**Note on Missing Values:** Missing entries account for roughly 67% of all data cells. This is normal for GATS data. The survey uses conditional skip logic. For example, questions about daily cigarette count (B04) are asked only to smokers. Non-smokers naturally receive null values for those fields.
""")

code(r"""# Initial Data Preview
df.head()
""")

code(r"""# Summary Statistics for Key Numeric Variables
df[['AGE', 'gatsweight']].describe()
""")

# ═══════════════════════════════════════════════════════════════
# 3  DATA CLEANING
# ═══════════════════════════════════════════════════════════════

md(r"""## 3. Data Cleaning and Preprocessing <a id="3-data-cleaning-and-preprocessing"></a>

The raw dataset uses numeric codes for categorical fields (e.g., 1 = Male, 2 = Female). 

In this section, numeric codes are converted into clear text labels. Key derived variables are also created to support demographic grouping and analysis.
""")

code(r"""# Data Preprocessing and Feature Engineering
df['Gender'] = df['A01'].map({1: 'Male', 2: 'Female'})
df['Residence'] = df['RESIDENCE'].map({1: 'Urban', 2: 'Rural'})

education_map = {
    1: 'No formal education',
    2: 'Less than primary',
    3: 'Primary completed',
    4: 'Secondary completed',
    5: 'Higher secondary',
    6: "Bachelor's",
    7: "Master's or higher",
    8: "Don't know / Refused"
}
df['Education'] = df['A04'].map(education_map)

division_map = {
    10: 'Barisal', 20: 'Chittagong', 30: 'Dhaka', 40: 'Khulna',
    45: 'Mymensingh', 50: 'Rajshahi', 55: 'Rangpur', 60: 'Sylhet'
}
df['Division'] = df['divisionid'].map(division_map)

df['Smoking_Status'] = df['B01'].map({1: 'Daily', 2: 'Less than daily', 3: 'Not at all'})
df['Smokeless_Status'] = df['C01'].map({1: 'Daily', 2: 'Less than daily', 3: 'Not at all'})

df['Any_Tobacco'] = np.where(
    (df['B01'].isin([1, 2])) | (df['C01'].isin([1, 2])),
    'Tobacco User', 'Non-User'
)

conditions = [
    (df['B01'].isin([1,2])) & (df['C01'].isin([1,2])),
    (df['B01'].isin([1,2])) & (~df['C01'].isin([1,2])),
    (~df['B01'].isin([1,2])) & (df['C01'].isin([1,2])),
]
choices = ['Dual User', 'Smoker Only', 'Smokeless Only']
df['Tobacco_Type'] = np.select(conditions, choices, default='Non-User')

bins = [14, 24, 34, 44, 54, 64, 100]
labels = ['15-24', '25-34', '35-44', '45-54', '55-64', '65+']
df['Age_Group'] = pd.cut(df['AGE'], bins=bins, labels=labels, right=True)

df['SHS_Home'] = df['E04'].map({1: 'Yes', 2: 'No', 9: "Don't know"})
df['SHS_Knowledge'] = df['E15'].map({1: 'Yes', 2: 'No', 7: "Don't know"})
df['Knows_Smoking_Harmful'] = df['H01'].map({1.0: 'Yes', 2.0: 'No', 7.0: "Don't know", 9.0: 'Refused'})

print("Data preprocessing complete.")
""")

code(r"""# Validation of Processed Categorical Distributions
print("Gender distribution:")
print(df['Gender'].value_counts())
print(f"\nResidence distribution:")
print(df['Residence'].value_counts())
print(f"\nAge group distribution:")
print(df['Age_Group'].value_counts().sort_index())
print(f"\nTobacco consumption modality breakdown:")
print(df['Tobacco_Type'].value_counts())
""")

# ═══════════════════════════════════════════════════════════════
# 4  EDA
# ═══════════════════════════════════════════════════════════════

md(r"""## 4. Exploratory Data Analysis <a id="4-exploratory-data-analysis"></a>

This section explores demographic patterns, user profiles, and regional trends.

### 4.1 Overall Tobacco Use Prevalence

This analysis examines how many adults in Bangladesh use tobacco and what types they consume.
""")

code(r"""# 4.1 Overall Tobacco Prevalence Charts
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

order = ['Non-User', 'Smoker Only', 'Smokeless Only', 'Dual User']
colors = {'Non-User': '#2ecc71', 'Smoker Only': '#e74c3c', 'Smokeless Only': '#3498db', 'Dual User': '#9b59b6'}
sns.countplot(data=df, x='Tobacco_Type', order=order,
              palette=[colors[o] for o in order], edgecolor='white', ax=axes[0])
axes[0].set_title('Distribution of Tobacco Use Categories', fontsize=13, fontweight='bold')
axes[0].set_ylabel('Number of Respondents')
axes[0].set_xlabel('')
for container in axes[0].containers:
    axes[0].bar_label(container, fontsize=9, padding=3)

categories = ['Smoking\n(Daily)', 'Smoking\n(Occasional)', 'Smokeless\n(Daily)', 'Smokeless\n(Occasional)']
counts = [
    (df['B01'] == 1).sum(),
    (df['B01'] == 2).sum(),
    (df['C01'] == 1).sum(),
    (df['C01'] == 2).sum()
]
bar_colors = ['#e74c3c', '#f39c12', '#3498db', '#1abc9c']
axes[1].barh(categories, counts, color=bar_colors, edgecolor='white', height=0.6)
axes[1].set_title('Daily vs. Occasional Consumption by Tobacco Type', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Number of Respondents')
for i, v in enumerate(counts):
    axes[1].text(v + 30, i, f'{v:,} ({v/len(df)*100:.1f}%)', va='center', fontsize=9)

plt.tight_layout()
plt.savefig('01_overall_prevalence.png', dpi=150, bbox_inches='tight')
plt.show()

print("\n--- Summary of Tobacco Consumption Modalities ---")
print(f"Total surveyed respondents: {len(df):,}")
for t in order:
    n = (df['Tobacco_Type'] == t).sum()
    print(f"  {t}: {n:,} ({n/len(df)*100:.1f}%)")
""")

md(r"""Key findings from the prevalence analysis:

- **Overall prevalence:** About **40% of adults** in Bangladesh use some form of tobacco.
- **Smokeless tobacco:** Exclusive smokeless users form the largest user group. They outnumber exclusive smokers. Traditional products like *zarda* and *sadapata* are widely consumed.
- **Dual users:** A distinct group uses both smoked and smokeless tobacco. These users face compounded health risks.
- **Consumption pattern:** Most smokers smoke **daily** rather than occasionally. This reflects established nicotine dependence.

### 4.2 Tobacco Use by Gender

This section examines differences in tobacco use between men and women.
""")

code(r"""# 4.2 Tobacco Prevalence by Gender
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

tobacco_gender = pd.crosstab(df['Gender'], df['Tobacco_Type'], normalize='index') * 100
tobacco_gender = tobacco_gender[['Smoker Only', 'Smokeless Only', 'Dual User', 'Non-User']]
tobacco_gender.plot(kind='bar', stacked=True, ax=axes[0],
    color=['#e74c3c', '#3498db', '#9b59b6', '#2ecc71'], edgecolor='white', width=0.5)
axes[0].set_title('Tobacco Use Composition by Gender', fontsize=13, fontweight='bold')
axes[0].set_ylabel('Percentage (%)')
axes[0].set_xlabel('')
axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=0)
axes[0].legend(title='Category', bbox_to_anchor=(1.0, 1.0), frameon=True, fontsize=9)

gender_rates = []
for _, row in df.iterrows():
    gender_rates.append({
        'Gender': row['Gender'],
        'Type': 'Smoking',
        'Uses': 1 if row['B01'] in [1, 2] else 0
    })
    gender_rates.append({
        'Gender': row['Gender'],
        'Type': 'Smokeless',
        'Uses': 1 if row['C01'] in [1, 2] else 0
    })
rates_df = pd.DataFrame(gender_rates)

sns.barplot(data=rates_df, x='Gender', y='Uses', hue='Type',
            palette=['#e74c3c', '#3498db'], edgecolor='white', ax=axes[1])
axes[1].set_title('Tobacco Use Rate by Gender and Product Type', fontsize=13, fontweight='bold')
axes[1].set_ylabel('Proportion Using')
axes[1].set_xlabel('')
axes[1].legend(title='Tobacco Type', frameon=True)
for container in axes[1].containers:
    axes[1].bar_label(container, fmt='%.1f%%', fontsize=9, padding=3,
                      labels=[f'{v.get_height()*100:.1f}%' for v in container])

plt.tight_layout()
plt.savefig('02_gender_tobacco.png', dpi=150, bbox_inches='tight')
plt.show()
""")

md(r"""Gender analysis reveals a sharp divide:

- **Smoking is heavily concentrated among men:** About 40% of men smoke, compared to under 1% of women. Strong cultural norms discourage female smoking in Bangladesh.
- **Smokeless tobacco is higher among women:** About 29% of women use smokeless tobacco, compared to 19% of men. Consuming *zarda* with betel leaf (*paan*) is socially accepted. Many users do not recognize it as harmful tobacco.
- **Key takeaway:** Tracking only cigarette smoking misses more than half of the tobacco burden among women.

### 4.3 Tobacco Use by Age Group

This section tracks tobacco consumption patterns across age brackets.
""")

code(r"""# 4.3 Tobacco Prevalence by Age Cohort
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

age_rates = df.groupby('Age_Group', observed=True).apply(
    lambda x: pd.Series({
        'Smoking': x['B01'].isin([1,2]).mean() * 100,
        'Smokeless': x['C01'].isin([1,2]).mean() * 100,
        'Any Tobacco': (x['Any_Tobacco'] == 'Tobacco User').mean() * 100
    })
).reset_index()

age_melted = age_rates.melt(id_vars='Age_Group', var_name='Type', value_name='Rate')

sns.barplot(data=age_melted, x='Age_Group', y='Rate', hue='Type',
            palette=['#e74c3c', '#3498db', '#8e44ad'], edgecolor='white', ax=axes[0])
axes[0].set_title('Tobacco Prevalence by Age Group', fontsize=13, fontweight='bold')
axes[0].set_ylabel('Prevalence (%)')
axes[0].set_xlabel('Age Group')
axes[0].legend(title='Type', frameon=True, fontsize=9)

sns.pointplot(data=age_melted, x='Age_Group', y='Rate', hue='Type',
              palette=['#e74c3c', '#3498db', '#8e44ad'], markers=['o', 's', 'D'],
              linestyles=['-', '--', ':'], ax=axes[1])
axes[1].set_title('Tobacco Prevalence Trajectories Across Age Groups', fontsize=13, fontweight='bold')
axes[1].set_ylabel('Prevalence (%)')
axes[1].set_xlabel('Age Group')
axes[1].legend(title='Type', frameon=True, fontsize=9)

plt.tight_layout()
plt.savefig('03_age_tobacco.png', dpi=150, bbox_inches='tight')
plt.show()
""")

md(r"""Age patterns show distinct trends for each product type:

- **Smoking peaks in mid-adulthood:** Smoking rates rise quickly after age 15. They peak between ages 35 and 54, then decline after age 65. The drop in older ages likely reflects health-related quitting or survivor bias.
- **Smokeless tobacco increases with age:** Smokeless use rises steadily across every age group. It reaches its highest level among adults aged 65 and older.
- **Youth consumption:** About 20% of young adults aged 15–24 already use tobacco. This highlights an urgent need for early prevention.

### 4.4 Tobacco Use by Education Level

This section analyzes the relationship between education level and tobacco use.
""")

code(r"""# 4.4 Tobacco Prevalence by Educational Attainment
edu_order = ['No formal education', 'Less than primary', 'Primary completed',
             'Secondary completed', 'Higher secondary', "Bachelor's", "Master's or higher"]
df_edu = df[df['Education'].isin(edu_order)].copy()

smoke_edu = df_edu.groupby('Education').apply(
    lambda x: pd.Series({
        'Smoking': x['B01'].isin([1,2]).mean() * 100,
        'Smokeless': x['C01'].isin([1,2]).mean() * 100,
        'Any Tobacco': (x['Any_Tobacco'] == 'Tobacco User').mean() * 100,
    })
).reindex(edu_order)

fig, ax = plt.subplots(figsize=(12, 7))
y_pos = np.arange(len(edu_order))
height = 0.25

bars1 = ax.barh(y_pos - height, smoke_edu['Smoking'], height, label='Smoking',
                color='#e74c3c', edgecolor='white')
bars2 = ax.barh(y_pos, smoke_edu['Smokeless'], height, label='Smokeless',
                color='#3498db', edgecolor='white')
bars3 = ax.barh(y_pos + height, smoke_edu['Any Tobacco'], height, label='Any Tobacco',
                color='#8e44ad', edgecolor='white')

ax.set_yticks(y_pos)
ax.set_yticklabels(edu_order, fontsize=10)
ax.set_xlabel('Prevalence (%)', fontsize=12)
ax.set_title('Tobacco Prevalence Stratified by Educational Attainment', fontsize=14, fontweight='bold')
ax.legend(frameon=True)
ax.bar_label(bars3, fmt='%.1f%%', fontsize=8, padding=3)
ax.invert_yaxis()

plt.tight_layout()
plt.savefig('04_education_tobacco.png', dpi=150, bbox_inches='tight')
plt.show()
""")

md(r"""A clear **inverse relationship** exists between education and tobacco use:

- Overall tobacco use drops from ~50% among adults with no formal schooling to ~24% among postgraduates.
- The drop is steepest for **smokeless tobacco**. It falls from ~35% in the uneducated group to ~8% among postgraduates.
- Education serves as a strong protective factor. Higher health literacy helps reduce tobacco consumption.

### 4.5 Urban vs Rural Differences

This section compares tobacco use across urban and rural locations.
""")

code(r"""# 4.5 Urban vs. Rural Tobacco Prevalence
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

res_gender = df.groupby(['Residence', 'Gender']).apply(
    lambda x: pd.Series({
        'Smoking Rate': x['B01'].isin([1,2]).mean() * 100,
        'Smokeless Rate': x['C01'].isin([1,2]).mean() * 100
    })
).reset_index()

sns.barplot(data=res_gender, x='Residence', y='Smoking Rate', hue='Gender',
            palette=['#3498db', '#e74c3c'], edgecolor='white', ax=axes[0])
axes[0].set_title('Smoking Prevalence: Urban vs. Rural by Gender', fontsize=13, fontweight='bold')
axes[0].set_ylabel('Prevalence (%)')
axes[0].set_xlabel('')

sns.barplot(data=res_gender, x='Residence', y='Smokeless Rate', hue='Gender',
            palette=['#3498db', '#e74c3c'], edgecolor='white', ax=axes[1])
axes[1].set_title('Smokeless Tobacco Prevalence: Urban vs. Rural by Gender', fontsize=13, fontweight='bold')
axes[1].set_ylabel('Prevalence (%)')
axes[1].set_xlabel('')

for ax in axes:
    for container in ax.containers:
        ax.bar_label(container, fmt='%.1f%%', fontsize=9, padding=3,
                     labels=[f'{v.get_height():.1f}%' for v in container])

plt.tight_layout()
plt.savefig('05_urban_rural.png', dpi=150, bbox_inches='tight')
plt.show()
""")

md(r"""Key urban-rural differences include:

- **Rural men smoke slightly more than urban men:** This aligns with weaker enforcement of smoke-free rules in rural areas.
- **Rural women use more smokeless tobacco:** Traditional betel-quid practices remain more common in rural communities.
- **Urban women have the lowest rates:** Higher education and greater health awareness contribute to lower consumption in cities.

### 4.6 Division-wise Distribution

This section evaluates tobacco use across the eight administrative divisions of Bangladesh.
""")

code(r"""# 4.6 Tobacco Prevalence by Administrative Division
div_rates = df.groupby('Division').apply(
    lambda x: pd.Series({
        'Smoking': x['B01'].isin([1,2]).mean() * 100,
        'Smokeless': x['C01'].isin([1,2]).mean() * 100,
        'Any Tobacco': (x['Any_Tobacco'] == 'Tobacco User').mean() * 100
    })
).sort_values('Any Tobacco', ascending=True)

fig, ax = plt.subplots(figsize=(12, 6))

ax.barh(div_rates.index, div_rates['Smoking'], color='#e74c3c',
        edgecolor='white', label='Smoking', height=0.6)
ax.barh(div_rates.index, div_rates['Smokeless'], left=div_rates['Smoking'],
        color='#3498db', edgecolor='white', label='Smokeless', height=0.6)
ax.set_xlabel('Prevalence (%)', fontsize=12)
ax.set_title('Tobacco Prevalence by Administrative Division (Stacked Composition)', fontsize=14, fontweight='bold')
ax.legend(frameon=True, fontsize=10)

for i, (div, row) in enumerate(div_rates.iterrows()):
    ax.text(row['Smoking'] + row['Smokeless'] + 0.5, i,
            f"{row['Any Tobacco']:.1f}%", va='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('06_division_tobacco.png', dpi=150, bbox_inches='tight')
plt.show()

print("\nDivision-specific prevalence metrics (sorted by total prevalence):")
print(div_rates.round(1).to_string())
""")

md(r"""Regional findings highlight clear geographic variation:

- Total tobacco prevalence differs noticeably across divisions.
- Product composition also varies. Some divisions have more cigarette smokers, while others have more smokeless users.
- These differences support assigning tobacco control funds based on local regional profiles.

### 4.7 Secondhand Smoke (SHS) Exposure

This section evaluates exposure to secondhand smoke in private and public settings.
""")

code(r"""# 4.7 Secondhand Smoke Exposure by Setting
settings = {
    'Home': 'E04',
    'Workplace': 'E09',
    'Restaurants': 'E11',
    'Public\nTransport': 'E13'
}

shs_data = []
for setting_name, col in settings.items():
    valid = df[df[col].isin([1, 2])]
    exposed = (valid[col] == 1).sum()
    total = len(valid)
    shs_data.append({
        'Setting': setting_name,
        'Exposed (%)': exposed / total * 100,
        'Not Exposed (%)': (total - exposed) / total * 100,
        'Exposed': exposed,
        'Total': total
    })
shs_df = pd.DataFrame(shs_data)

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

bars = axes[0].bar(shs_df['Setting'], shs_df['Exposed (%)'],
                   color=['#e74c3c', '#e67e22', '#f1c40f', '#9b59b6'], edgecolor='white')
axes[0].set_title('Secondhand Smoke Exposure Rate by Environmental Setting', fontsize=13, fontweight='bold')
axes[0].set_ylabel('Exposed (%)')
axes[0].set_ylim(0, 65)
for bar, row in zip(bars, shs_df.itertuples()):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 f'{row._2:.1f}%', ha='center', fontsize=10, fontweight='bold')

shs_home_gender = pd.crosstab(df['Gender'], df['SHS_Home'], normalize='index') * 100
shs_home_gender = shs_home_gender.reindex(columns=['Yes', 'No'], fill_value=0)
shs_home_gender = shs_home_gender.reindex(['Male', 'Female'])

shs_home_gender.plot(kind='bar', ax=axes[1], color=['#e74c3c', '#2ecc71'],
                     edgecolor='white', width=0.5)
axes[1].set_title('Domestic SHS Exposure Stratified by Gender', fontsize=13, fontweight='bold')
axes[1].set_ylabel('Percentage (%)')
axes[1].set_xlabel('')
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=0)
axes[1].legend(title='Exposed?', frameon=True)
for container in axes[1].containers:
    axes[1].bar_label(container, fmt='%.1f%%', fontsize=10, padding=3)

plt.tight_layout()
plt.savefig('07_shs_exposure.png', dpi=150, bbox_inches='tight')
plt.show()
""")

md(r"""Key observations regarding secondhand smoke exposure:

- **Home is the main source of exposure:** Private homes have the highest SHS rates, followed by restaurants and public transport. Private residences currently have no legal smoking restrictions.
- **Reported domestic exposure shows a large gender gap:** About 84% of men report exposure at home, compared to 10% of women. This reflects male gathering habits at home, though women remain exposed to lingering indoor smoke.
- **Workplace exposure remains high:** About 17% of indoor workers encounter secondhand smoke. This shows a need for stricter enforcement of smoke-free workplace laws.

### 4.8 Knowledge and Awareness

This section assesses public knowledge of health risks from active smoking and secondhand smoke.
""")

code(r"""# 4.8 Public Health Risk Awareness Comparison
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

knows_order = ['Yes', 'No', "Don't know"]
sns.countplot(data=df, x='Knows_Smoking_Harmful', order=knows_order,
              palette=['#2ecc71', '#e74c3c', '#f39c12'], edgecolor='white', ax=axes[0])
axes[0].set_title('Belief That Active Smoking Causes\nSerious Illness', fontsize=13, fontweight='bold')
axes[0].set_ylabel('Count')
axes[0].set_xlabel('')
for container in axes[0].containers:
    axes[0].bar_label(container, fontsize=9, padding=3)

sns.countplot(data=df, x='SHS_Knowledge', order=knows_order,
              palette=['#2ecc71', '#e74c3c', '#f39c12'], edgecolor='white', ax=axes[1])
axes[1].set_title('Awareness That Secondhand Smoke\nHarms Non-Smokers', fontsize=13, fontweight='bold')
axes[1].set_ylabel('Count')
axes[1].set_xlabel('')
for container in axes[1].containers:
    axes[1].bar_label(container, fontsize=9, padding=3)

plt.suptitle('Health Knowledge and Risk Perception Comparison', fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('08_knowledge.png', dpi=150, bbox_inches='tight')
plt.show()

h01_yes = (df['H01'] == 1).sum()
e15_yes = (df['E15'] == 1).sum()
print(f"Believe smoking causes illness: {h01_yes:,} ({h01_yes/df['H01'].notna().sum()*100:.1f}%)")
print(f"Know SHS is harmful: {e15_yes:,} ({e15_yes/len(df)*100:.1f}%)")
print(f"\nAwareness Disparity Gap: {h01_yes/df['H01'].notna().sum()*100 - e15_yes/len(df)*100:.1f} percentage points")
""")

md(r"""Health awareness shows a critical knowledge gap:

- **Active smoking awareness is high:** 96.7% of respondents agree that smoking causes serious illness.
- **Secondhand smoke awareness is low:** Only 54.1% know that breathing other people's smoke harms non-smokers.
- **A 42.6 percentage point gap exists:** Public health campaigns must focus specifically on the dangers of secondhand smoke.

### 4.9 Cessation Attempts

This section examines quit attempts among smokers and smoking rules inside homes.
""")

code(r"""# 4.9 Cessation Attempts and Domestic Smoking Rules
smokers = df[df['B01'].isin([1, 2])].copy()
print(f"Active smokers in dataset: {len(smokers):,}")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

d01_valid = smokers[smokers['D01'].isin([1, 2])].copy()
d01_valid['Quit_Attempt'] = d01_valid['D01'].map({1: 'Tried to quit', 2: 'Did not try'})

sns.countplot(data=d01_valid, x='Quit_Attempt',
              palette=['#2ecc71', '#e74c3c'], edgecolor='white', ax=axes[0])
axes[0].set_title('Quit Attempts Among Current Smokers\n(Past 12 Months)', fontsize=13, fontweight='bold')
axes[0].set_ylabel('Count')
axes[0].set_xlabel('')
for container in axes[0].containers:
    axes[0].bar_label(container, fontsize=10, padding=3)

e01_valid = df[df['E01'].isin([1, 2, 3, 4])].copy()
rule_map = {1: 'Allowed', 2: 'Not allowed\n(exceptions)', 3: 'Never allowed', 4: 'No rules'}
e01_valid['Home_Rule'] = e01_valid['E01'].map(rule_map)
rule_order = ['Allowed', 'Not allowed\n(exceptions)', 'Never allowed', 'No rules']

sns.countplot(data=e01_valid, x='Home_Rule', order=rule_order,
              palette=['#e74c3c', '#f39c12', '#2ecc71', '#95a5a6'], edgecolor='white', ax=axes[1])
axes[1].set_title('Indoor Smoking Policies in the Home', fontsize=13, fontweight='bold')
axes[1].set_ylabel('Count')
axes[1].set_xlabel('')
for container in axes[1].containers:
    axes[1].bar_label(container, fontsize=9, padding=3)

plt.tight_layout()
plt.savefig('09_cessation_rules.png', dpi=150, bbox_inches='tight')
plt.show()
""")

md(r"""Findings on cessation and home smoking policies:

- **Most smokers do not attempt to quit:** While some smokers tried quitting in the past year, the majority did not. Bangladesh needs better cessation support, including quitlines and counseling.
- **Home smoking rules are weak:** "Allowed" is the most common home smoking rule. Most households lack complete smoking bans, exposing family members to indoor smoke.

### 4.10 Age Distribution of Tobacco Users (KDE)

This section uses kernel density estimation (KDE) to compare age distributions across user groups.
""")

code(r"""# 4.10 Continuous Age Density Estimation (KDE)
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

sns.kdeplot(data=df, x='AGE', hue='Any_Tobacco', fill=True,
            palette=['#2ecc71', '#e74c3c'], alpha=0.4, ax=axes[0], common_norm=False)
axes[0].set_title('Age Distribution: Tobacco Users vs. Non-Users', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Density')

users_only = df[df['Tobacco_Type'] != 'Non-User']
sns.kdeplot(data=users_only, x='AGE', hue='Tobacco_Type', fill=True,
            palette=['#9b59b6', '#e74c3c', '#3498db'], alpha=0.35, ax=axes[1], common_norm=False)
axes[1].set_title('Age Distribution by Tobacco Product Type (Active Users)', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Age')
axes[1].set_ylabel('Density')

plt.tight_layout()
plt.savefig('10_kde_age.png', dpi=150, bbox_inches='tight')
plt.show()
""")

md(r"""The density curves show distinct age profiles:

- **Tobacco users are older on average:** Tobacco users peak around ages 40–50. Non-users peak much younger, around ages 25–30.
- **Smokers are younger than smokeless users:** Cigarette smokers peak around ages 35–40. Smokeless users peak around ages 50–55.
- Higher smoking rates among younger adults will increase the long-term burden of chronic lung diseases.

### 4.11 Smoking Initiation Age Analysis

This section analyzes the age when daily smokers started smoking regularly.
""")

code(r"""# 4.11 Smoking Initiation Age Distribution
daily_smokers = df[(df['B01'] == 1) & (df['B04'].notna()) & (df['B04'] < 77)].copy()
print(f"Daily smokers with recorded initiation age: {len(daily_smokers):,}")

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

sns.histplot(daily_smokers['B04'], bins=30, kde=True, color='#e74c3c',
             edgecolor='white', alpha=0.7, ax=axes[0])
axes[0].axvline(daily_smokers['B04'].median(), color='black', linestyle='--', linewidth=1.5,
                label=f'Median: {daily_smokers["B04"].median():.0f} years')
axes[0].set_title('Age of Regular Smoking Initiation\n(Daily Smokers)', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Age Started Smoking Regularly')
axes[0].set_ylabel('Frequency')
axes[0].legend(frameon=True)

daily_edu = daily_smokers[daily_smokers['Education'].isin(edu_order)].copy()
edu_simple = {
    'No formal education': 'No formal\nedu',
    'Less than primary': 'Below\nprimary',
    'Primary completed': 'Primary',
    'Secondary completed': 'Secondary',
    'Higher secondary': 'Higher\nsecondary',
    "Bachelor's": "Bachelor's",
    "Master's or higher": "Master's+"
}
daily_edu['Education_Short'] = daily_edu['Education'].map(edu_simple)
edu_short_order = ['No formal\nedu', 'Below\nprimary', 'Primary', 'Secondary',
                   'Higher\nsecondary', "Bachelor's", "Master's+"]

sns.boxplot(data=daily_edu, x='Education_Short', y='B04', order=edu_short_order,
            palette='RdYlGn', fliersize=3, ax=axes[1])
axes[1].set_title('Smoking Initiation Age by Educational Level', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Educational Level')
axes[1].set_ylabel('Age Started Smoking')

plt.tight_layout()
plt.savefig('11_initiation_age.png', dpi=150, bbox_inches='tight')
plt.show()

print("\nSmoking initiation age summary statistics:")
print(daily_smokers['B04'].describe().round(1))
print(f"\nProportion initiating smoking before age 18: {(daily_smokers['B04'] < 18).sum()/len(daily_smokers)*100:.1f}%")
print(f"Proportion initiating smoking before age 21: {(daily_smokers['B04'] < 21).sum()/len(daily_smokers)*100:.1f}%")
""")

md(r"""Key findings on smoking initiation:

- **Median initiation age is 18 years:** Half of daily smokers start regular smoking before adulthood.
- **Adolescence is the main window of vulnerability:** Most daily smokers start before age 21.
- **Lower education links to earlier start ages:** Less educated respondents reported starting as young as ages 10–12.
- **Policy takeaway:** School-based prevention programs must start early in primary and middle schools.

### 4.12 Correlation Analysis

This section presents a correlation matrix of key demographic and behavioral variables.
""")

code(r"""# 4.12 Correlation Matrix and Heatmap
corr_df = pd.DataFrame({
    'Is_Smoker': df['B01'].isin([1,2]).astype(int),
    'Is_Smokeless_User': df['C01'].isin([1,2]).astype(int),
    'Any_Tobacco': (df['Any_Tobacco'] == 'Tobacco User').astype(int),
    'Is_Male': (df['A01'] == 1).astype(int),
    'Is_Urban': (df['RESIDENCE'] == 1).astype(int),
    'Age': df['AGE'],
    'Education_Level': df['A04'],
    'SHS_at_Home': (df['E04'] == 1).astype(int),
    'Knows_SHS_Harmful': (df['E15'] == 1).astype(int),
    'Knows_Smoking_Harmful': (df['H01'] == 1).astype(int),
})

corr_matrix = corr_df.corr()

fig, ax = plt.subplots(figsize=(10, 8))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='RdBu_r',
            center=0, vmin=-1, vmax=1, square=True, linewidths=0.5,
            ax=ax, cbar_kws={'shrink': 0.8})
ax.set_title('Correlation Matrix of Key Demographic and Epidemiological Variables', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('12_correlation.png', dpi=150, bbox_inches='tight')
plt.show()
""")

md(r"""Key correlations from the matrix:

- **Male gender and smoking ($r = 0.50$):** Strong positive correlation confirming that smoking is concentrated among men.
- **Male gender and home SHS ($r = 0.75$):** Strong correlation linked to shared indoor smoking among male peers.
- **Education and smokeless use ($r = -0.28$):** Negative correlation showing that higher education protects against smokeless tobacco.
- **Age and any tobacco ($r = 0.30$):** Moderate positive correlation reflecting higher use in older age groups.
- **Smoking and smokeless use ($r = -0.06$):** Near-zero correlation indicates that smoking and smokeless tobacco are independent habits with different target populations.

### 4.13 Multivariate Exploration

This section examines age distributions and logistic regression curves for smoking and smokeless tobacco.
""")

code(r"""# 4.13 Multivariate Distributions (Violin and Boxen Plots)
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

type_order = ['Non-User', 'Smoker Only', 'Smokeless Only', 'Dual User']

sns.violinplot(data=df, x='Tobacco_Type', y='AGE', order=type_order,
               palette=['#2ecc71', '#e74c3c', '#3498db', '#9b59b6'],
               inner='quartile', ax=axes[0])
axes[0].set_title('Age Distribution by Tobacco Category\n(Violin Plot)', fontsize=13, fontweight='bold')
axes[0].set_xlabel('')
axes[0].set_ylabel('Age')

sns.boxenplot(data=df, x='Tobacco_Type', y='AGE', order=type_order,
              palette=['#2ecc71', '#e74c3c', '#3498db', '#9b59b6'], ax=axes[1])
axes[1].set_title('Age Distribution by Tobacco Category\n(Boxen Plot — Distribution Tails)', fontsize=13, fontweight='bold')
axes[1].set_xlabel('')
axes[1].set_ylabel('Age')

plt.tight_layout()
plt.savefig('13_violin_boxen.png', dpi=150, bbox_inches='tight')
plt.show()
""")

code(r"""# 4.13 Logistic Regression Fits (Age vs. Probability)
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

sample = df.sample(n=2000, random_state=42).copy()
sample['Is_Smoker'] = sample['B01'].isin([1,2]).astype(int)
sample['Is_Smokeless'] = sample['C01'].isin([1,2]).astype(int)

sns.regplot(data=sample, x='AGE', y='Is_Smoker', logistic=True,
            scatter_kws={'alpha': 0.1, 's': 10, 'color': '#e74c3c'},
            line_kws={'color': '#c0392b', 'linewidth': 2}, ax=axes[0])
axes[0].set_title('Age vs. Smoking Probability\n(Logistic Regression Fit)', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('P(Smoker)')
axes[0].set_ylim(-0.1, 1.1)

sns.regplot(data=sample, x='AGE', y='Is_Smokeless', logistic=True,
            scatter_kws={'alpha': 0.1, 's': 10, 'color': '#3498db'},
            line_kws={'color': '#2980b9', 'linewidth': 2}, ax=axes[1])
axes[1].set_title('Age vs. Smokeless Tobacco Probability\n(Logistic Regression Fit)', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Age')
axes[1].set_ylabel('P(Smokeless User)')
axes[1].set_ylim(-0.1, 1.1)

plt.tight_layout()
plt.savefig('14_regplot_age.png', dpi=150, bbox_inches='tight')
plt.show()
""")

md(r"""Insights from the multivariate and regression models:

- **Distribution shapes:** Violin and boxen plots confirm that smokeless users skew older, while non-users are youngest.
- **Logistic regression curves:** The probability of smokeless tobacco use increases steadily with age. Smoking probability shows a curved pattern, rising early and leveling off in later years.
- **Intervention focus:** Anti-smoking campaigns should target young adults (ages 20–35). Smokeless tobacco programs should target middle-aged and older adults.

### 4.14 Summary Statistics Table

This table provides a quick reference for all primary statistics from the GATS 2017 analysis.
""")

code(r"""# 4.14 Summary Statistics Table Display
summary_data = {
    'Metric': [
        'Total respondents',
        'Male / Female',
        'Urban / Rural',
        '---',
        'Current smokers (daily + occasional)',
        'Current smokeless tobacco users',
        'Dual users (both)',
        'Any tobacco users',
        '---',
        'Male smoking rate',
        'Female smoking rate',
        'Male smokeless rate',
        'Female smokeless rate',
        '---',
        'SHS exposure at home (among valid)',
        'Know smoking causes illness',
        'Know SHS is harmful',
        'Awareness gap (smoking vs SHS)',
        '---',
        'Median smoking initiation age',
        '% started smoking before age 18',
    ],
    'Value': [
        f'{len(df):,}',
        f'{(df["A01"]==1).sum():,} / {(df["A01"]==2).sum():,}',
        f'{(df["RESIDENCE"]==1).sum():,} / {(df["RESIDENCE"]==2).sum():,}',
        '',
        f'{df["B01"].isin([1,2]).sum():,} ({df["B01"].isin([1,2]).sum()/len(df)*100:.1f}%)',
        f'{df["C01"].isin([1,2]).sum():,} ({df["C01"].isin([1,2]).sum()/len(df)*100:.1f}%)',
        f'{(df["Tobacco_Type"]=="Dual User").sum():,} ({(df["Tobacco_Type"]=="Dual User").sum()/len(df)*100:.1f}%)',
        f'{(df["Any_Tobacco"]=="Tobacco User").sum():,} ({(df["Any_Tobacco"]=="Tobacco User").sum()/len(df)*100:.1f}%)',
        '',
        f'{df[(df["A01"]==1) & df["B01"].isin([1,2])].shape[0] / (df["A01"]==1).sum()*100:.1f}%',
        f'{df[(df["A01"]==2) & df["B01"].isin([1,2])].shape[0] / (df["A01"]==2).sum()*100:.1f}%',
        f'{df[(df["A01"]==1) & df["C01"].isin([1,2])].shape[0] / (df["A01"]==1).sum()*100:.1f}%',
        f'{df[(df["A01"]==2) & df["C01"].isin([1,2])].shape[0] / (df["A01"]==2).sum()*100:.1f}%',
        '',
        f'{(df["E04"]==1).sum():,} ({(df["E04"]==1).sum()/(df["E04"].isin([1,2])).sum()*100:.1f}%)',
        f'{(df["H01"]==1).sum():,} ({(df["H01"]==1).sum()/df["H01"].notna().sum()*100:.1f}%)',
        f'{(df["E15"]==1).sum():,} ({(df["E15"]==1).sum()/len(df)*100:.1f}%)',
        f'{(df["H01"]==1).sum()/df["H01"].notna().sum()*100 - (df["E15"]==1).sum()/len(df)*100:.1f} percentage points',
        '',
        f'{df[(df["B01"]==1) & (df["B04"].notna()) & (df["B04"]<77)]["B04"].median():.0f} years',
        f'{(df[(df["B01"]==1) & (df["B04"].notna()) & (df["B04"]<77)]["B04"] < 18).sum() / len(df[(df["B01"]==1) & (df["B04"].notna()) & (df["B04"]<77)]) * 100:.1f}%',
    ]
}

summary_df = pd.DataFrame(summary_data)
summary_df = summary_df.replace('---', '')
print(summary_df.to_string(index=False))
""")

# ═══════════════════════════════════════════════════════════════
# 5  KEY FINDINGS
# ═══════════════════════════════════════════════════════════════

md(r"""## 5. Key Findings and Discussion <a id="5-key-findings-and-discussion"></a>

The analysis highlights seven major findings:

### Finding 1: High Burden of Smokeless Tobacco
Smokeless tobacco use (24.4%) exceeds cigarette smoking (19.5%). Products like *zarda* and *sadapata* are widely used but receive less policy attention.

### Finding 2: Sharp Gender Division by Product Type
Men predominantly smoke (~40%). Women predominantly use smokeless tobacco (~29%). Measuring only cigarette smoking undercounts the health burden among women.

### Finding 3: Secondhand Smoke Awareness Gap
96.7% of adults know smoking is harmful. Only 54.1% know secondhand smoke harms non-smokers. This 42.6 percentage point gap is a prime target for public education.

### Finding 4: Smoking and Smokeless Use are Separate Epidemics
The correlation between smoking and smokeless use is nearly zero ($r = -0.06$). They affect different demographic groups and require distinct interventions.

### Finding 5: Early Smoking Initiation
The median age of smoking initiation is 18 years. Lower educational attainment correlates with earlier initiation ages.

### Finding 6: Education Protects Against Tobacco Use
Tobacco prevalence drops from ~50% among uneducated adults to ~24% among postgraduates. Health literacy is a powerful long-term protective factor.

### Finding 7: Homes Lack Smoking Restrictions
Most homes have no indoor smoking rules. Because homes are private spaces, public education is essential to encourage smoke-free households.
""")

# ═══════════════════════════════════════════════════════════════
# 6  POLICY IMPLICATIONS
# ═══════════════════════════════════════════════════════════════

md(r"""## 6. Policy Implications <a id="6-policy-implications"></a>

Based on the evidence, seven policy actions are recommended:

1. **Regulate smokeless tobacco equally:** Apply the same health warnings, taxes, and packaging rules to smokeless products as cigarettes.
2. **Launch a national secondhand smoke campaign:** Educate the public on the dangers of secondhand smoke to close the 42.6 percentage point awareness gap.
3. **Start school prevention programs early:** Introduce anti-tobacco education in primary and middle schools before the median initiation age of 18.
4. **Design gender-specific programs:** Focus male programs on smoking cessation. Focus female programs on smokeless tobacco in rural and semi-urban communities.
5. **Enforce smoke-free laws in public places:** Strengthen enforcement in restaurants, workplaces, and public transit.
6. **Use adult education channels:** Integrate tobacco harm awareness into adult literacy programs.
7. **Allocate resources regionally:** Direct more public health funding to divisions with higher tobacco prevalence.

These actions directly support **UN Sustainable Development Goal 3 (Target 3.a)**.
""")

# ═══════════════════════════════════════════════════════════════
# 7  LIMITATIONS
# ═══════════════════════════════════════════════════════════════

md(r"""## 7. Limitations <a id="7-limitations"></a>

Several study limitations should be noted:

- **Self-reported data:** Survey responses may suffer from recall bias or underreporting, especially among women.
- **Cross-sectional design:** The data captures a single point in time (2017). It shows associations but cannot prove causality.
- **Unweighted analysis:** This exploratory analysis uses unweighted sample counts. Values may differ slightly from complex survey-weighted national estimates.
- **Unmeasured variables:** Detailed household income and specific product brand details were not included in this analysis.
""")

# ═══════════════════════════════════════════════════════════════
# 8  CONCLUSION
# ═══════════════════════════════════════════════════════════════

md(r"""## 8. Conclusion <a id="8-conclusion"></a>

The 2017 GATS data shows that tobacco use in Bangladesh is widespread and diverse:

- **Prevalence is high:** About 40% of adults consume tobacco products.
- **Smokeless tobacco dominates:** It is the primary form of tobacco for women and older adults.
- **Secondhand smoke awareness is low:** A large knowledge gap remains regarding the harms of secondhand smoke.
- **Education protects health:** Higher education strongly correlates with lower tobacco use.
- **Intervention must start young:** Most smokers start before age 18.

Reducing this burden requires a balanced approach. Bangladesh needs strict policy enforcement, early school education, and gender-targeted cessation programs to advance UN SDG 3.
""")

# ═══════════════════════════════════════════════════════════════
# 9  REFERENCES
# ═══════════════════════════════════════════════════════════════

md(r"""## 9. References <a id="9-references"></a>

1. World Health Organization. (2019). *Global Adult Tobacco Survey (GATS): Bangladesh 2017 — Country Report*. WHO Regional Office for South-East Asia.

2. World Health Organization. (2023). *Tobacco Fact Sheet*. Retrieved from https://www.who.int/news-room/fact-sheets/detail/tobacco

3. Bangladesh Bureau of Statistics (BBS) & National Tobacco Control Cell. (2019). *Global Adult Tobacco Survey: Bangladesh Report 2017*.

4. Centers for Disease Control and Prevention (CDC). *Global Tobacco Surveillance System Data (GTSSData)*. Retrieved from https://nccd.cdc.gov/GTSSDataSurveyResources/

5. United Nations. *Sustainable Development Goal 3: Good Health and Well-being*. Retrieved from https://sdgs.un.org/goals/goal3

6. WHO Framework Convention on Tobacco Control (FCTC). Retrieved from https://fctc.who.int/

---

**Dataset Information:**
- **Title:** Bangladesh Global Adult Tobacco Survey (GATS) 2017 — Public Use Data File
- **File:** `Bangla_GATS_2017_Public_use_06Spe2018.csv`
- **Rows:** 12,783
- **Columns:** 516
- **Numeric Columns:** 498
- **String Columns:** 18
- **Source:** WHO GATS Data Repository / CDC GTSS Portal
""")

# ═══════════════════════════════════════════════════════════════
# APPENDIX: Dataset Info Card
# ═══════════════════════════════════════════════════════════════

md(r"""---

## Appendix: Dataset Information Card
*Course Submission Summary*

| Field | Description / Value |
|-------|---------------------|
| **Topic** | Tobacco Use Patterns and Secondhand Smoke Exposure in Bangladesh |
| **SDG Alignment** | SDG 3 — Good Health and Well-being (Target 3.a) |
| **Dataset Name** | Bangladesh Global Adult Tobacco Survey (GATS) 2017 — Public Use File |
| **Data Repository** | [CDC GTSS Data Portal](https://nccd.cdc.gov/GTSSDataSurveyResources/) |
| **Total Rows** | 12,783 |
| **Total Columns** | 516 |
| **Numeric Columns** | 498 (int64: 59, float64: 439) |
| **Non-Numeric Columns** | 18 (string/object type) |
| **Missing Cells** | 4,423,173 cells (67.06% — conditional skip patterns) |
| **Complete Columns** | 61 |
| **Conditional Columns** | 455 |
| **Sample Weight Variable** | `gatsweight` |

### Chart Types and Analytical Methods

| Chart Type | Implementation | Purpose |
|------------|----------------|---------|
| Count Plot | `sns.countplot` | Distribution of tobacco categories and awareness indicators |
| Bar Plot / Horizontal Bar | `sns.barplot`, `df.plot.barh()` | Prevalence by gender, age, education, and SHS setting |
| Stacked Bar Chart | `df.plot.bar(stacked=True)`, matplotlib | Division-wise and gender-stratified composition |
| Point Plot | `sns.pointplot` | Prevalence trends across age cohorts |
| Histogram + KDE | `sns.histplot` | Distribution of smoking initiation age |
| Kernel Density Estimate (KDE) | `sns.kdeplot` | Age density comparison across user categories |
| Box Plot | `sns.boxplot` | Smoking initiation age by education level |
| Violin Plot | `sns.violinplot` | Age distributions by tobacco category |
| Boxen Plot | `sns.boxenplot` | Distribution tails across user categories |
| Correlation Heatmap | `sns.heatmap` | Linear association matrix across variables |
| Logistic Regression Plot | `sns.regplot` | Tobacco use probability modeled by age |
""")


# ═══════════════════════════════════════════════════════════════
# ASSEMBLE AND WRITE
# ═══════════════════════════════════════════════════════════════

nb.cells = cells

output_path = "GATS_2017_Bangladesh_Analysis.ipynb"
with open(output_path, "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print(f"[OK] Notebook saved to: {output_path}")
print(f"   Total cells: {len(cells)} ({sum(1 for c in cells if c.cell_type=='markdown')} markdown, {sum(1 for c in cells if c.cell_type=='code')} code)")
