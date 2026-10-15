A/B Test for Delivery App

This project was developed as part of the A/B Test for Delivery App project on JetBrains Academy (Hyperskill).

The goal was to understand whether changes to a food delivery application’s interface could influence the Average Order Value (AOV). Using Python, I analyzed data from control and experimental groups, explored their distributions, handled outliers, and applied statistical tests to evaluate the results.

About the Project

A/B testing is commonly used to compare different versions of a product, website, or application to understand how changes affect user behavior.

In this project, I worked with two groups of users: a control group using the original interface and an experimental group using a modified version.

The main objective was to determine whether the observed differences in order values were statistically significant.

Technologies Used

* Python
* Pandas
* NumPy
* SciPy
* Statsmodels
* Matplotlib

Project Development

The project was divided into five stages, covering different aspects of statistical analysis and A/B testing.

1. Sampling Strategy

I started by comparing two samples using Levene’s test and an independent samples t-test.

This stage helped me understand how sample characteristics, variance, and differences between means can influence statistical conclusions.

2. Sample Size Calculation

I calculated the sample size required for the experiment using statistical power analysis.

The parameters included:

* Effect size: 0.20
* Significance level: 0.05
* Statistical power: 80%
* Equal sample sizes for both groups

This stage demonstrated the importance of having enough observations to detect meaningful differences between groups.

3. Exploratory Data Analysis

I explored the dataset to understand user behavior and identify unusual observations.

The analysis included:

* Number of sessions by day.
* Order value distribution.
* Session duration distribution.
* Identification and removal of outliers above the 99th percentile.

Removing these outliers helped reduce the influence of unusually high order values and long sessions on the analysis.

4. Non-parametric A/B Testing

Since the original order values were not normally distributed, I applied the Mann-Whitney U test to compare the control and experimental groups.

The results indicated a statistically significant difference between their distributions.

5. Parametric A/B Testing

In the final stage, I applied a logarithmic transformation to the order values and performed additional statistical tests.

I used Levene’s test to evaluate whether the groups had equal variances, followed by an independent samples t-test.

When the variances were unequal, I used Welch’s t-test.

The results also indicated a statistically significant difference between the groups, consistent with the findings from the previous stage.

Results

Both the non-parametric and parametric tests provided evidence of statistically significant differences between the control and experimental groups at the 5% significance level.

These results suggest that the interface change may have influenced purchasing behavior. However, statistical significance alone does not establish whether the new design would provide a meaningful business improvement.

Further analysis would be needed to evaluate the practical impact of the change.

Repository Structure

ab-test-delivery-app/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE

This repository contains the Python implementation from the final stage of the project. The previous stages are described above to provide context for the overall analysis.

How to Run

Clone the repository:

git clone https://github.com/maiapedro/ab-test-delivery-app.git

Navigate to the project directory:

cd ab-test-delivery-app

Install the required libraries:

pip install -r requirements.txt

Place the ab_test.csv dataset in the same directory as main.py.

Note: The dataset was provided as part of the Hyperskill learning project and is not included in this repository.

Run the program:

python main.py

The program generates a histogram of the log-transformed order values and displays the results of Levene’s test and the independent samples t-test.

What I Learned

This project helped me develop a better understanding of how statistical methods can be applied to business problems.

I gained practical experience with data exploration, data cleaning, statistical hypothesis testing, and Python libraries used in data analysis.

It also helped me understand how A/B testing can support data-driven decision-making when evaluating changes to digital products.

Acknowledgments

This project was developed through JetBrains Academy (Hyperskill) as part of my studies in Python and Data Analytics.
