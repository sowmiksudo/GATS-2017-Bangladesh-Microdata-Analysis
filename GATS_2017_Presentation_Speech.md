# GATS 2017 Bangladesh Analysis - 10 Minute Presentation Script

This script provides a straightforward, student-friendly narration for your Reveal.js presentation. 
It uses plain, simple English without confusing jargon.

---

### Slide 1: Title & Introduction
**Time:** `0:00 - 0:30` (30s) | **Cumulative:** `0:30`

> "Good morning everyone. My name is Shayer Mahmud Sowmik, and today I will present my data science project for CS295. 
>
> I analyzed the Global Adult Tobacco Survey for Bangladesh from 2017 to uncover patterns in how people use tobacco and their exposure to secondhand smoke. 
>
> This research ties directly into the UN's Sustainable Development Goal 3, which aims to improve global health."
>
> *[Transition:] "Let's first look at the dataset I used..."*  
> *[Action: Click Next Slide]*

---

### Slide 2: About the Dataset
**Time:** `0:30 - 1:10` (40s) | **Cumulative:** `1:10`

> "The GATS 2017 dataset is massive, with over 12,000 respondents. 
>
> You might notice a high missing data rate of 67%. I want to clarify that this is not broken data. It's just normal survey skip logic. 
>
> For example, if someone says they don't smoke, the survey skips questions about how many cigarettes they smoke a day. It's normal survey behavior, not lost data."
>
> *[Transition:] "To process all this information, I used Python..."*  
> *[Action: Click Next Slide]*

---

### Slide 3: Data Preprocessing (Pandas)
**Time:** `1:10 - 1:40` (30s) | **Cumulative:** `1:40`

> "I used the Pandas library in Python to clean and categorize the data. 
>
> Instead of keeping confusing number codes, I mapped them into clear labels—like turning a '1' into 'Male' and a '2' into 'Female'. 
>
> I also grouped people into age brackets and separated tobacco users into clear categories: Smokers, Smokeless Tobacco users, and Dual Users."
>
> *[Transition:] "So, what does the overall tobacco use look like nationally?..."*  
> *[Action: Click Next Slide]*

---

### Slide 4: Overall Tobacco Use
**Time:** `1:40 - 2:15` (35s) | **Cumulative:** `2:15`

> "This chart compares raw survey counts in grey against national survey-weighted estimates in red.
>
> Overall, about 35.3% of adults in Bangladesh use tobacco. Smokeless tobacco is the most common at 17.3%, followed by smokers at 14.7%, and dual users at 3.3%.
>
> Notice that raw unweighted data overestimates tobacco use at 40.1%, whereas applying survey weights gives the true national estimate of 35.3%."
> To get these accurate national numbers, we used survey weights. This makes sure our sample properly represents the whole population of Bangladesh, rather than just the people surveyed."
>
> *[Transition:] "When we break this down by gender, a huge divide appears..."*  
> *[Action: Click Next Slide]*

---

### Slide 5: Tobacco Habits by Gender
**Time:** `2:15 - 2:50` (35s) | **Cumulative:** `2:50`

> "There is a very clear divide between men and women. 
>
> About 40% of men smoke cigarettes or bidis. However, less than 2% of women smoke. But that doesn't mean women don't use tobacco—about 25% of women use smokeless tobacco products.
>
> This shows that standard anti-smoking campaigns, which usually only talk about cigarettes, completely miss the female population."
>
> *[Transition:] "Next, we looked at what age people start smoking..."*  
> *[Action: Click Next Slide]*

---

### Slide 6: When Do Smokers Start?
**Time:** `2:50 - 3:25` (35s) | **Cumulative:** `3:25`

> "Our data shows that most daily smokers start around age 18.
>
> While older adults started at a wide variety of ages, younger people almost exclusively start smoking in their late teens. 
>
> This tells us that secondary schools and colleges are the most critical places for prevention programs."
>
> *[Transition:] "And how does tobacco use change as people get older?..."*  
> *[Action: Click Next Slide]*

---

### Slide 7: Tobacco Use by Age
**Time:** `3:25 - 4:00` (35s) | **Cumulative:** `4:00`

> "This graph shows how age affects habits. 
>
> Smoking increases slowly with age, rising from about 15% in youth to around 40% in older age. 
>
> However, smokeless tobacco use increases steadily as people get older. Older adults have the highest smokeless tobacco usage, showing it's a deeply rooted cultural habit."
>
> *[Transition:] "Beyond age, education plays a massive role..."*  
> *[Action: Click Next Slide]*

---

### Slide 8: Tobacco Use by Education Level
**Time:** `4:00 - 4:35` (35s) | **Cumulative:** `4:35`

> "This heatmap shows that education strongly lowers tobacco use. 
>
> People with no formal education use the most tobacco, especially smokeless products. 
>
> As people get more education, their tobacco use drops quickly. Interestingly, university graduates who do use tobacco strongly prefer cigarettes over smokeless products."
>
> *[Transition:] "For those who do smoke, how much are they smoking?..."*  
> *[Action: Click Next Slide]*

---

### Slide 9: Daily Cigarette Consumption
**Time:** `4:35 - 5:05` (30s) | **Cumulative:** `5:05`

> "Looking at daily smokers, the average person smokes 15 to 20 cigarettes a day—basically a pack a day.
>
> People aged 45 to 54 smoke the most heavily. We also found that urban smokers consume slightly more cigarettes per day than rural smokers."
>
> *[Transition:] "Speaking of where people live, let's look at the geographic split..."*  
> *[Action: Click Next Slide]*

---

### Slide 10: Urban vs. Rural Tobacco Use
**Time:** `5:05 - 5:40` (35s) | **Cumulative:** `5:40`

> "Where people live matters. Rural areas have much higher smokeless tobacco use, mainly driven by cheap and easily available bidis and loose zarda. 
>
> Urban areas, on the other hand, have a slightly higher share of manufactured cigarette smoking."
>
> *[Transition:] "Now let's talk about the danger to non-smokers: secondhand smoke..."*  
> *[Action: Click Next Slide]*

---

### Slide 11: Secondhand Smoke Exposure
**Time:** `5:40 - 6:20` (40s) | **Cumulative:** `6:20`

> "Secondhand smoke is a major issue in Bangladesh. 
>
> Despite laws against it, public transport and restaurants still have very high exposure rates. Many adults also face smoke at their workplaces. 
>
> But the biggest problem is inside homes, where men smoking indoors puts non-smoking women and children at severe health risk."
>
> *[Transition:] "To see how all these factors link together, I built a correlation matrix..."*  
> *[Action: Click Next Slide]*

---

### Slide 12: Variables Correlation
**Time:** `6:20 - 6:55` (35s) | **Cumulative:** `6:55`

> "This matrix shows how variables connect. 
>
> First, male smoking strongly correlates with homes having secondhand smoke (r = 0.75), which means men smoking indoors is what exposes women and children to passive smoke. Second, higher education is strongly linked to lower smokeless tobacco use. 
>
> Finally, smoking and smokeless habits do not usually overlap—people tend to do one or the other, not both."
>
> *[Transition:] "So what do people actually know about these health risks?..."*  
> *[Action: Click Next Slide]*

---

### Slide 13: Public Awareness & Knowledge Gaps
**Time:** `6:55 - 7:30` (35s) | **Cumulative:** `7:30`

> "This chart compares public awareness about active smoking versus secondhand smoke.
>
> Awareness that active smoking causes serious illness is almost universal at 96.7%. 
>
> However, only 54.1% of people know that secondhand smoke harms non-smokers. That is a huge 42.6 percentage point gap, which directly explains why so many people still smoke inside homes and public transport."
>
> Even worse, awareness about the dangers of secondhand smoke is very low, which is probably why so many people still smoke indoors."
>
> *[Transition:] "When people try to quit, do they get help?..."*  
> *[Action: Click Next Slide]*

---

### Slide 14: Quitting Tobacco
**Time:** `7:30 - 8:05` (35s) | **Cumulative:** `8:05`

> "Nearly half of tobacco users want to quit and tried to quit in the last year. 
>
> But there is a huge lack of medical support. Doctors rarely advise their patients to quit during routine checkups. 
>
> Without proper medical advice or medicine to help, many people simply fail to quit."
>
> *[Transition:] "Based on all this data, here is what needs to change..."*  
> *[Action: Click Next Slide]*

---

### Slide 15: Policy Recommendations
**Time:** `8:05 - 8:50` (45s) | **Cumulative:** `8:50`

> "To fix these issues, we recommend three simple policies:
>
> 1. **Raise Taxes:** We need to raise taxes on smokeless tobacco and bidis to match cigarettes, so people don't just switch to cheaper options.
> 2. **Target Women:** We need anti-smokeless campaigns specifically designed for women and rural areas, rather than just targeting cigarette smokers.
> 3. **Enforce Fines:** We need to strictly fine people who smoke in public transport and restaurants to protect non-smokers."
>
> *[Transition:] "To wrap up our findings..."*  
> *[Action: Click Next Slide]*

---

### Slide 16: Conclusion & Limitations
**Time:** `8:50 - 9:30` (40s) | **Cumulative:** `9:30`

> "There are some data limitations: this survey is from 2017, and people might have underreported their habits due to social stigma.
>
> But the final conclusion is clear: Bangladesh has two separate tobacco problems. We have smoking for men, and smokeless tobacco for women. 
>
> We need targeted solutions for both groups if we want to improve public health.
>
> Thank you for your time. I am happy to answer any questions."
>
> *[End of Presentation]*

---

## 💡 Quick-Fire Defense Cheatsheet for Questions

| If the Teacher Asks... | Deliver This Exact Answer |
| :--- | :--- |
| **"Why didn't you fill in the missing data?"** | *"The 67% missing rate is just normal survey skip logic. Non-smokers skipped the cigarette questions. Filling those in with fake numbers would ruin our analysis."* |
| **"Why are survey weights necessary?"** | *"The survey only asked 12,000 people. Weights help adjust the math so those 12,000 people accurately represent the whole population of Bangladesh."* |
| **"Why do women use so much smokeless tobacco?"** | *"Smoking cigarettes has a heavy social stigma for women in Bangladesh, but chewing tobacco with betel leaf is seen as normal and culturally accepted."* |
| **"What is the best policy to fix this?"** | *"Raising taxes across the board. If we only tax cigarettes, people just buy cheap bidis and zarda. We have to tax everything equally."* |
