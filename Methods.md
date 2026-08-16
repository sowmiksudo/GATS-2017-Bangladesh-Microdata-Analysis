**Pandas Plotting (`13_plotting-with-pandas.ipynb`)**

* **Line Plot (`df.plot.line()` / `kind='line'`):** Tracks numeric trends and time-series changes across indices.


* **Bar & Horizontal Bar Chart (`df.plot.bar()`, `df.plot.barh()`):** Compares discrete categories and frequency counts.


* **Histogram (`df.plot.hist()`):** Displays the frequency distribution and binning of continuous variables.


* **Box Plot (`df.plot.box()` / `df.boxplot()`):** Summarizes median, IQR, spread, and outlier detection.


* **Area Plot (`df.plot.area()`):** Visualizes cumulative and stacked magnitude over time/groups.


* **Scatter Plot (`df.plot.scatter()`):** Evaluates correlation and relationships between two continuous variables.


* **Hexbin Plot (`df.plot.hexbin()`):** Analyzes 2D point density to prevent overplotting in large datasets.


* **Pie Chart (`df.plot.pie()`):** Displays proportions and part-to-whole relationships.


* **Density / KDE Plot (`df.plot.kde()` / `df.plot.density()`):** Estimates smooth probability density curves.


* **Scatter Matrix (`scatter_matrix()`):** Generates a grid of pairwise scatter plots and univariate histograms.



---

**Seaborn Plotting (`14_plotting-with-seaborn.ipynb`)**

**1. Categorical Plots**

* **Count Plot (`sns.countplot`):** Counts observations across categorical bins.


* **Bar Plot (`sns.barplot`):** Estimates central tendency (mean) with confidence interval error bars.


* **Box Plot & Boxen Plot (`sns.boxplot`, `sns.boxenplot`):** Shows distribution percentiles and tail behavior across categories.


* **Violin Plot (`sns.violinplot`):** Merges box plots with kernel density estimates for distribution shape.


* **Strip & Swarm Plot (`sns.stripplot`, `sns.swarmplot`):** Plots individual categorical data points without overlapping.


* **Point Plot (`sns.pointplot`):** Compares point estimates and slope differences across groups.



**2. Distribution Plots**

* **Histogram (`sns.histplot`):** Plots binned continuous data with optional KDE overlays.


* **Kernel Density Estimate (`sns.kdeplot`):** Computes univariate or bivariate continuous density curves.


* **ECDF Plot (`sns.ecdfplot`):** Empirical cumulative distribution functions.


* **Rug Plot (`sns.rugplot`):** Draws marginal tick marks along axes to indicate raw value distribution.



**3. Relational & Regression Plots**

* **Scatter Plot (`sns.scatterplot`):** Evaluates multivariable relationships using `hue`, `size`, and `style`.


* **Line Plot (`sns.lineplot`):** Visualizes continuous trends with automatic aggregation and error bands.


* **Linear Regression Plot (`sns.regplot`, `sns.lmplot`):** Fits linear models with confidence intervals.


* **Residual Plot (`sns.residplot`):** Evaluates regression residuals for model diagnostics.



**4. Matrix & Multi-Plot Grids**

* **Heatmap (`sns.heatmap`):** Color-encoded matrix for correlation tables and 2D cross-tabulations.


* **Cluster Map (`sns.clustermap`):** Hierarchically clustered heatmap revealing matrix patterns.


* **Pair Plot / PairGrid (`sns.pairplot`, `sns.PairGrid`):** Pairwise scatter matrices across all numerical features.


* **Joint Plot (`sns.jointplot`):** Bivariate scatter/KDE with marginal distribution plots.


* **Facet Grid (`sns.FacetGrid` / `catplot` / `relplot`):** Subplot grids conditioned on dataset subsets.