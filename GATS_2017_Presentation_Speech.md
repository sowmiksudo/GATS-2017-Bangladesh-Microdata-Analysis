# GATS 2017 Bangladesh Analysis — Complete 10-Minute Presentation Speech Script

**Course:** CS295 – Programming in Python  
**Presenter:** Shayer Mahmud Sowmik (Student ID: 2025-3-27-022)  
**Total Allocated Time:** 10:00 Minutes (600 Seconds)  
**Slide Deck:** `GATS_2017_Presentation.html` (16 Slides)

---

## ⏱️ Master Pacing & Timing Dashboard

| Slide # | Slide Title | Target Time | Cumulative Time | Pace & Focus |
| :---: | :--- | :---: | :---: | :--- |
| **1** | Title Slide & SDG 3 Alignment | 0:30 | 0:30 | Formal opening & research context |
| **2** | Dataset Architecture & Hygiene | 0:35 | 1:05 | Justify 67% skip logic nulls |
| **3** | Feature Engineering (Python/Pandas) | 0:25 | 1:30 | Prove clean, vectorized code |
| **4** | Overall Tobacco Consumption | 0:35 | 2:05 | Weighted vs raw sampling reality |
| **5** | Gender Disparity: Modality Inversion | 0:50 | 2:55 | **⭐ Core Insight 1: Men smoke, Women SLT** |
| **6** | Smoking Initiation Across Cohorts | 0:40 | 3:35 | Median 18y & adolescent window |
| **7** | Age Trajectories: Smoked vs. Smokeless | 0:45 | 4:20 | **⭐ Core Insight 2: Peak vs. Linear Rise** |
| **8** | Socioeconomic Gradients (Education) | 0:40 | 5:00 | Education as a protective shield |
| **9** | Daily Consumption Intensity | 0:35 | 5:35 | 15–20 sticks/day heavy habit |
| **10** | Geographic & Residential Disparities | 0:35 | 6:10 | Rural burden & regional variance |
| **11** | Secondhand Smoke (SHS) Exposure | 0:45 | 6:55 | **⭐ Core Insight 3: Domestic passive smoke** |
| **12** | Multivariate Correlation Matrix | 0:35 | 7:30 | Statistically independent habits |
| **13** | Public Awareness & Pathology Knowledge | 0:35 | 8:05 | The 42.6% SHS knowledge gap |
| **14** | Cessation Attempts & Clinical Advice | 0:35 | 8:40 | Missed physician interventions |
| **15** | Actionable Policy Levers (SDG 3.a) | 0:45 | 9:25 | 3 concrete regulatory reforms |
| **16** | Conclusion & Limitations | 0:35 | **10:00** | Cross-sectional caveats & final Q&A |

---

## 🎙️ Slide-by-Slide Verbatim Speech Script

---

### Slide 1: Title Slide
**Time:** `0:00 – 0:30` (30s) | **Cumulative:** `0:30`

> "Good [morning/afternoon], respected faculty members and colleagues. 
>
> Today, I am presenting our empirical data science investigation on **'Tobacco Use Patterns and Secondhand Smoke Exposure in Bangladesh'**, conducted using the Global Adult Tobacco Survey (GATS) 2017 microdata.
>
> This research is directly anchored to **United Nations Sustainable Development Goal 3**, specifically **Target 3.a**, which mandates strengthening the implementation of the WHO Framework Convention on Tobacco Control. Over the next ten minutes, I will walk you through our data architecture, statistical findings, and evidence-based policy recommendations."
>
> *[Action: Click Next Slide]*

---

### Slide 2: Dataset Architecture & Hygiene
**Time:** `0:30 – 1:05` (35s) | **Cumulative:** `1:05`

> "To establish analytical rigor, let's first look at the dataset architecture. We analyzed 12,783 nationally representative household surveys across 516 individual attributes.
>
> An initial audit reveals an apparent 67.06% missing data rate. However, we must strongly emphasize that this is **not** data attrition or survey loss. It is driven entirely by **structural survey skip logic**.
>
> For instance, non-smokers correctly bypass detailed stick-count and brand economics questions. Preserving these structural nulls—rather than applying synthetic imputation—was essential to safeguard the empirical integrity of our downstream analysis."
>
> *[Transition:] "Let's look at how we transformed these raw survey codes into analytical features in Python..."*  
> *[Action: Click Next Slide]*

---

### Slide 3: Feature Engineering (Python & Pandas)
**Time:** `1:05 – 1:30` (25s) | **Cumulative:** `1:30`

> "Our data preprocessing pipeline in Pandas focused on clean, vectorized feature engineering. 
>
> We mapped demographic response codes, segmented continuous age into standard demographic cohorts using `pd.cut`, and implemented vectorized conditional logic with NumPy’s `np.select`. 
>
> This allowed us to categorize every respondent into four mutually exclusive modalities: **Dual Users, Smoker Only, Smokeless Only, and Non-Users**. This engineered classification serves as the backbone for all our comparative models."
>
> *[Transition:] "Now, applying this classification alongside national sample weights, let's examine overall consumption..."*  
> *[Action: Click Next Slide]*

---

### Slide 4: Overall Tobacco Consumption
**Time:** `1:30 – 2:05` (35s) | **Cumulative:** `2:05`

> "Looking at overall consumption, our primary finding is the dominance of **Smokeless Tobacco (SLT)** over combustible smoking across Bangladesh. 
>
> Crucially, we incorporated the GATS complex survey weights (`gatsweight`) to account for the multi-stage stratified cluster sampling design. 
>
> As shown in the chart, unweighted raw counts overestimate combustible smoking. Applying sampling weights reveals the true national picture: smokeless tobacco consumption represents the single largest burden of tobacco use in the country."
>
> *[Transition:] "When we break this consumption down by gender, a striking behavioral divide emerges..."*  
> *[Action: Click Next Slide]*

---

### Slide 5: Gender Disparity: Modality Inversion ⭐
**Time:** `2:05 – 2:55` (50s) | **Cumulative:** `2:55`

> "This slide illustrates one of our most critical demographic revelations: a complete **Gender Inversion** in tobacco modality.
>
> Among adult males, tobacco use stands at approximately 40%, dominated heavily by combustible products like cigarettes and bidis. 
>
> Among females, combustible smoking is under 2% due to strong cultural stigmatization. However, approximately 29% of women actively consume smokeless tobacco—such as Zarda, Sadapata, and Gul—often culturally embedded through betel leaf chewing.
>
> **The public health implication is profound:** Traditional anti-tobacco campaigns that focus exclusively on cigarette smoking completely miss the high-risk female population."
>
> *[Transition:] "To understand when these habits form, we investigated the age of initiation..."*  
> *[Action: Click Next Slide]*

---

### Slide 6: Smoking Initiation Across Age Cohorts
**Time:** `2:55 – 3:35` (40s) | **Cumulative:** `3:35`

> "Examining the initiation age distributions across age brackets, we find a remarkably consistent **median initiation age of 18 years**.
>
> The Kernel Density Estimates demonstrate generational narrowing: while older cohorts reported a wider span of initiation ages, younger generations begin smoking almost exclusively within a sharp window between ages 15 and 19.
>
> This empirically confirms that secondary school and adolescent years are the primary vulnerability window, proving that preventive interventions must be targeted before age 18."
>
> *[Transition:] "Tracking users across their lifespan shows fundamentally divergent trajectories for smoked versus smokeless tobacco..."*  
> *[Action: Click Next Slide]*

---

### Slide 7: Age Trajectories: Smoked vs. Smokeless ⭐
**Time:** `3:35 – 4:20` (45s) | **Cumulative:** `4:20`

> "Our logistic regression trajectories reveal starkly different life-course patterns for both products.
>
> **Combustible smoking** follows an inverted curve: probability rises rapidly through early adulthood, peaks between ages 35 to 45, and then plateaus and declines due to mid-life cessation or health mortality.
>
> In sharp contrast, **Smokeless tobacco use scales almost linearly with age**, reaching its highest prevalence among senior citizens aged 65 and above. This highlights the deep domestic normalization of smokeless tobacco among aging populations."
>
> *[Transition:] "Beyond age and gender, socioeconomic status plays a decisive protective role..."*  
> *[Action: Click Next Slide]*

---

### Slide 8: Socioeconomic Gradients (Education)
**Time:** `4:20 – 5:00` (40s) | **Cumulative:** `5:00`

> "This heatmap clearly demonstrates **education as a social determinant of health**.
>
> We observe a strong inverse relationship: respondents with no formal education carry the highest burden of tobacco use, particularly cheap smokeless tobacco.
>
> As educational attainment increases, total tobacco use drops significantly. Furthermore, educated consumers shift almost exclusively to manufactured cigarettes, completely abandoning traditional smokeless varieties and bidis."
>
> *[Transition:] "Next, we analyzed daily consumption intensity among active smokers..."*  
> *[Action: Click Next Slide]*

---

### Slide 9: Daily Consumption Intensity
**Time:** `5:00 – 5:35` (35s) | **Cumulative:** `5:35`

> "Turning to daily smoking volume among active daily smokers, the median consumption is **15 to 20 sticks per day**—essentially a pack-a-day habit.
>
> The 45 to 54 age bracket exhibits the heaviest consumption density. 
>
> When comparing urban and rural smokers, urban daily smokers exhibit slightly higher stick volumes, which our economic analysis links to widespread single-stick retail availability at urban tea stalls."
>
> *[Transition:] "Geographic stratification further clarifies these consumption divides..."*  
> *[Action: Click Next Slide]*

---

### Slide 10: Geographic & Residential Disparities
**Time:** `5:35 – 6:10` (35s) | **Cumulative:** `6:10`

> "Geographically, rural Bangladesh carries a significantly higher overall tobacco burden, fueled by widespread informal markets for inexpensive bidis and unpackaged smokeless products.
>
> Urban centers reflect higher proportional cigarette consumption. 
>
> Division-level variances highlight that coastal and northern divisions face the highest prevalence, indicating that national tobacco control enforcement must be regionally decentralized."
>
> *[Transition:] "We now move to a severe public health hazard: Secondhand Smoke exposure..."*  
> *[Action: Click Next Slide]*

---

### Slide 11: Secondhand Smoke (SHS) Exposure ⭐
**Time:** `6:10 – 6:55` (45s) | **Cumulative:** `6:55`

> "Secondhand smoke exposure represents an urgent non-smoker hazard in Bangladesh.
>
> Despite existing legal prohibitions, exposure rates remain alarming in **public transport terminals and restaurants**. Indoor workplaces also expose nearly 17% of wage earners.
>
> Most critically, **the private home is the largest unregulated source of exposure**. Over 84% of men report indoor domestic exposure, which directly subjects non-smoking women and children to involuntary passive smoking and severe respiratory risk."
>
> *[Transition:] "To validate these interrelationships statistically, we generated a multivariate correlation matrix..."*  
> *[Action: Click Next Slide]*

---

### Slide 12: Multivariate Correlation Matrix
**Time:** `6:55 – 7:30` (35s) | **Cumulative:** `7:30`

> "Our Pearson correlation matrix confirms three key statistical relationships:
>
> First, a strong positive correlation ($r = 0.50$) between male gender and smoking.
>
> Second, a distinct negative correlation ($r = -0.28$) between formal education and smokeless tobacco.
>
> Third, a near-zero correlation ($r = -0.08$) between smoking and smokeless tobacco use. This proves that smoked and smokeless tobacco represent two **independent, parallel user bases** rather than interchangeable substitutes."
>
> *[Transition:] "This brings us to public health awareness: what does the population actually know?..."*  
> *[Action: Click Next Slide]*

---

### Slide 13: Public Awareness & Pathology Knowledge
**Time:** `7:30 – 8:05` (35s) | **Cumulative:** `8:05`

> "Our analysis reveals a critical **risk perception deficit**.
>
> While generic awareness that 'smoking causes serious illness' is nearly universal at **96.7%**, detailed knowledge of specific pathologies like strokes and cardiovascular disease drops substantially.
>
> Even more alarming, only **54.1%** of respondents know that secondhand smoke causes serious illness in non-smokers—revealing a massive **42.6 percentage point awareness gap** that public campaigns must bridge."
>
> *[Transition:] "When users attempt to quit, does the healthcare system support them?..."*  
> *[Action: Click Next Slide]*

---

### Slide 14: Cessation Attempts & Healthcare Advice
**Time:** `8:05 – 8:40` (35s) | **Cumulative:** `8:40`

> "We identified a major **missed clinical opportunity** in tobacco cessation.
>
> Nearly 50% of current smokers reported making an active quit attempt in the preceding 12 months, indicating high intrinsic readiness to quit.
>
> However, less than half of tobacco users who visited a healthcare provider received structured cessation advice from their doctor. Furthermore, institutional access to Nicotine Replacement Therapy (NRT) or cessation counseling remains virtually absent."
>
> *[Transition:] "Translating these empirical insights into policy, we propose three actionable levers..."*  
> *[Action: Click Next Slide]*

---

### Slide 15: Actionable Policy Levers (SDG 3.a)
**Time:** `8:40 – 9:25` (45s) | **Cumulative:** `9:25`

> "To achieve UN SDG Target 3.a, we recommend three evidence-based policy levers:
>
> 1. **Fiscal Tax Harmonization:** Eliminate Bangladesh's complex multi-tiered cigarette tax slabs. Significantly raise specific excise taxes on bidis and smokeless products to prevent smokers from down-trading to cheaper alternatives.
> 2. **Gender-Tailored Grassroots Campaigns:** Move away from generic cigarette-centric warnings. Deploy community health workers to target Zarda and Sadapata use specifically among rural and female demographics.
> 3. **Strict 100% Smoke-Free Enforcement:** Eliminate designated smoking areas in restaurants and public transit hubs, backed by strict municipal enforcement penalties."
>
> *[Transition:] "To conclude our presentation, let us review the research limitations..."*  
> *[Action: Click Next Slide]*

---

### Slide 16: Conclusion & Research Limitations
**Time:** `9:25 – 10:00` (35s) | **Cumulative:** `10:00`

> "In terms of methodology, we acknowledge that GATS 2017 is a **cross-sectional survey**, meaning we identify strong empirical associations rather than longitudinal causality, and female combustible smoking may reflect slight social desirability underreporting.
>
> **In conclusion:** Bangladesh faces a **bifurcated tobacco epidemic**—combustible smoking among men, and smokeless tobacco among women and vulnerable socioeconomic groups.
>
> Advancing SDG 3.a requires dual regulatory tracks that address both modalities with equal fiscal and educational urgency.
>
> Thank you for your time and attention. I am now open to your questions."
>
> *[End of Presentation — Timer: 10:00]*

---

## 🛡️ Quick-Fire Defense Cheatsheet for Evaluators

| If Faculty Asks... | Deliver This Exact 15-Second Answer |
| :--- | :--- |
| **"Why didn't you impute missing data?"** | *"The 67% missing rate is structural skip logic. Imputing values for non-smokers on stick-counts would introduce artificial smoking habits and invalidate our results."* |
| **"Why are survey weights (`gatsweight`) necessary?"** | *"GATS uses multi-stage stratified cluster sampling. Weights normalize unequal sampling probabilities across divisions and urban/rural strata, ensuring true national representativeness."* |
| **"Why is female SLT high while smoking is <2%?"** | *"Smoking carries a heavy social stigma for women in Bangladesh, whereas smokeless tobacco with betel leaf (paan) is culturally normalized and perceived as benign."* |
| **"What is the single highest-impact policy lever?"** | *"Tax harmonization. Eliminating tiered slabs prevents users from substituting expensive cigarettes with cheap bidis and untaxed zarda."* |
