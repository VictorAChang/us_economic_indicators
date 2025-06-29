

<h1 style="font-size: 400%; text-align:center;"> Analyzing U.S. Economic Indicators </h1>


<div style="font-size: 125%; text-align:center;"> Written by Victor Chang | MBA 615 - Descriptive Analytics </div>

</br><br>

<h1 style="text-align:center;"> Executive Summary </h1>

Employee retention is a critical component of workforce management, directly impacting operational efficiency, company culture, and long-term performance. High turnover not only drives up recruitment and training costs, estimated at over $1 trillion annually in the U.S., but also erodes institutional knowledge, morale, and strategic continuity. This analysis uses descriptive and diagnostic analytics to explore patterns in employee behavior, focusing on satisfaction, tenure, salary, and other workplace factors. Findings indicate that low satisfaction, shorter tenure, and lower compensation are strong predictors of employee turnover. Based on these insights, this report recommends actionable strategies including mentorship programs and transparent career development to help organizations proactively address attrition and build a more engaged, resilient workforce.

<h1 style="text-align:center;"> Data Extraction </h1>

<b style="font-size: 125%;"> St. Louis Federal Reserve Website </b>

Data was gathered from the [St. Louis Federal Reserve Website](https://fred.stlouisfed.org/)

The following six U.S. Economic Indicators were analyzed in this study:
- [Gross Domestic Product](https://fred.stlouisfed.org/series/GDP)
- [Federal Debt: Total Public Debt](https://fred.stlouisfed.org/series/GFDEBTN)
- [Share of Net Worth Held by the Top 1% (99th to 100th Wealth Percentiles)](https://fred.stlouisfed.org/series/WFRBST01134#)
- [30-Year Fixed Rate Mortgage Average in the United States](https://fred.stlouisfed.org/series/MORTGAGE30US)
- [Chinese Yuan Renminbi to U.S. Dollar Spot Exchange Rate](https://fred.stlouisfed.org/series/EXCHUS)
- [U.S. Dollars to Euro Spot Exchange Rate](https://fred.stlouisfed.org/series/EXUSEU)

The data extracted was filtered to include only 10 years, starting on December 2006 and ending on December 2016. Additionally the name was gathered quarterly. 
 

<b style="font-size: 125%;"> CSV downloaded were merged into a single table </b>



<h1 style="text-align:center;"> Data Exploration </h1>

<b style="font-size: 125%;"> Data Source </b>

Data is produced by Portobello Tech, an app innovator that has devised an intelligent way of predicting employee turnover within the company. The data source is from Kaggle at https://www.kaggle.com/datasets/akshayhedau/employee-turnover-analytics-dataset?resource=download. Data from prior evaluations show the employee’s satisfaction at the workplace. The data could be used to identify patterns in work style and their interest to continue to work in the company. The HR Department owns the data and uses it to predict employee turnover. Employee turnover refers to the total number of workers who leave a company over a certain time period. 

<b style="font-size: 125%;"> Data Description </b>

<i> First Five rows of the dataset </i>

![alt text](images/head.png)

The image above shows the first five rows of the dataset, using python's pandas library to display the data as a dataframe for ease of view. 

<i> Data Columns </i>

* satisfaction_level: From 0-1, how satisfied employees are since 
* last_evaluation: Unsure, but most likely from 0-1, measuring employee performance
* number_project = From 2-7, how many project the employee has work on
* average_monthly_hours = Average number of hours worked each month
* time_spend_company = How long they have been at the company in years
* Work_accident = If the employee has had an accident at work
* left = If the employee has left the company
* promotion_last_5years = If the employee has had a promotion in the last 5 years
* sales = Unsure, but most likely the role within sales that each employee works in
* salary = employee salary

The columns above describe in more detail what each row means or represents. Some of the values are not exactly known as the dataset in kaggle did not describe exactly what they are and we do not want to assume incorrectly and make wrong predictions based on those columns. 

<div align="center">

<b style="font-size: 110%;"> Data Information </b>

| #  | Column                 | Non-Null Count | Dtype   |
|----|------------------------|----------------|---------|
| 0  | `satisfaction_level`   | 14,999         | float64 |
| 1  | `last_evaluation`      | 14,999         | float64 |
| 2  | `number_project`       | 14,999         | int64   |
| 3  | `average_montly_hours` | 14,999         | int64   |
| 4  | `time_spend_company`   | 14,999         | int64   |
| 5  | `Work_accident`        | 14,999         | int64   |
| 6  | `left`                 | 14,999         | int64   |
| 7  | `promotion_last_5years`| 14,999         | int64   |
| 8  | `sales`                | 14,999         | object  |
| 9  | `salary`               | 14,999         | object  |

</div>

Data information above shows that the dataset does not contain any null or missing values and also displays the data types of each column. It is important to know the data types as they affect the way the data is manipulated to extract insights and predictions about employee retention. 

<i> Data Statistics </i>

![alt text](images/describe.png)

The table above shows important statistic information about our dataset. It is important especially important to pay attention to the difference between mean and median values. Huge differences among these two values is an indicator that the data might have too many outliers and may be skewed, needing further cleaning to derive accurate insights. Looking at the max and min values can also show if there are values that simply do not make sense. Most of the values from this dataset are within normal ranges, and do not need further cleaning to derive important conclusions. 

<h1 style="text-align:center;"> Analytical Techniques </h1>

<b style="font-size: 125%;"> Diagnostic Analytics </b>

Diagnostic analytics is a method in data analysis that digs into historical data to determine why certain events occurred, addressing the question, “Why did this happen?”. It employs techniques such as drill down, data mining, correlations, and regression to reveal underlying causes behind observed trends or anomalies (Drury, 2025; Holliday, 2021). The value of diagnostic analytics lies in its capacity to uncover root causes and contributing factors, such as changes in customer behavior, operational inefficiencies, or external influences, which empowers businesses to make targeted improvements, prevent issues from reoccurring, and refine strategies for better outcomes (Drury, 2025; Holliday, 2021).


<div align="center">

<b style="font-size: 110%;"> Heatmap </b>

<img src="images/image.png">

</div>

The correlation matrix above, which was created using python's library seaborn, displays the different correlation values among all columns in the table. Focusing on employee turnover, which is the "left" column, we see that the columns with the highest correlation to this column are satisfaction level, work accidents, time spent at the company, and salary. Columns with high correlation help derive stronger and more confident insights that demonstrate more value to stakeholders. 

</br>


<b style="font-size: 125%;"> Descriptive Analytics </b>

Descriptive analytics refers to the process of examining historical data to answer the fundamental question: “What happened?” By aggregating, organizing, and visualizing past information, such as sales figures, customer transactions, or operational metrics (Kelly, 2024; Morris, 2021). This approach helps stakeholders track trends, identify areas of inefficiency, and benchmark results against goals or industry standards. The importance of descriptive analytics lies in its ability to transform raw, complex datasets into digestible insights, enabling decision makers to establish a factual basis for deeper analysis or strategy development (Morris, 2021).

<div align="center">

<b style="font-size: 110%;"> Histogram </b> </br>

<img src="images/image-1.png">

</div>

Focusing on just the columns that have high correlation values to employee turnover, the histograms above show the distribution of the respective columns. 

<i> Satisfaction Levels </i>

We can see that employee turover is extremely high among employees whose satisfaction level is almost zero. Satisfaction levels aroud 0.4 also sem to show a relatively high employee turnover, higher than satisfaction levels aroud 0.2.  

<i> Time Spent at the Company </i>

The higher numbers of employee turnover seem to be for employees who spent between 3-5 years at the company. It seems that employees who are past 7 years at the company have zero to almost zero employee turnover. 

<i> Work Accidents </i>

Employee turnover for work accidents does seem to show a slightly higher employee turnover for employees who have no work accidents.

<i> Salary </i>

Salary seems to have a direct inverse correlation with employee turnover. Employees with higher salaries have a smaller chance leaving the company. In fact, employees with high salaries show an extremely low chance of leaving the company.  


</br>

<h1 style="text-align:center;"> Insights and Recommendations </h1>

<b style="font-size: 125%;"> Actionable Insights </b>

Based on the trends observed through descriptive and diagnostic analytics, employees with shorter tenure, lower salaries, and reduced job satisfaction are most likely to leave the organization. These findings are supported by the data, which show that turnover rates are especially high among employees with low satisfaction scores and minimal time at the company. Additionally, salary plays a significant role: those earning lower wages are far more likely to depart, while higher earning employees rarely leave. Beyond compensation, diagnostic insights suggest that non-financial factors such as work life balance and opportunities for career development are key drivers of retention. When employees perceive limited growth potential or experience burnout due to poor work life integration, they are more inclined to seek opportunities elsewhere. These factors emphasize the importance of not only improving pay structures but also fostering a supportive and growth oriented work environment to reduce attrition.

<b style="font-size: 125%;"> Solutions and Strategies </b>

To enhance employee retention, organizations should implement mentorship programs and increase transparency around career progression through continuous learning. Mentorship helps new hires feel supported and integrated, significantly reducing early stage turnover. Companies that offer structured mentoring report stronger engagement and retention outcomes, as these programs build trust, foster a sense of belonging, and accelerate employee development (Herbert, 2025; Ward, 2024). 

In parallel, increasing transparency around learning and advancement opportunities, such as through onboarding support, skill building resources, or clearly defined development tracks, empower employees to take ownership of their growth. When workers feel invested in and understand how they can progress, they are more likely to stay committed to the organization. These strategies directly address common causes of turnover such as low satisfaction, limited support, and unclear growth paths.

<h1 style="text-align:center;"> Communication </h1>


<b style="font-size: 125%;"> Findings </b>

<i style="font-size: 100%;"> Live Employee Attrition Dashboard: </i>

Explore key features influencing attrition and run interactive “what-if” simulations:

👉 [Launch the App]()

<h1 style="text-align:center;"> Conclusion </h1>

Employee retention is both a strategic priority and a reflection of organizational health. Through targeted analysis, we can better understand the underlying factors that lead to turnover and apply data driven solutions to prevent it. By investing in mentorship, clarifying career progression, and focusing on workplace satisfaction, companies can help reduce costly attrition while also fostering a supportive culture that promotes growth and loyalty. With the right analytics and action, retention becomes a competitive advantage.

<h1 style="text-align:center;"> References </h1>

* Anvari, R., JianFu, Z., & Chermahini, S. H. (2014). Effective Strategy for Solving Voluntary Turnover Problem among Employees. Procedia, Social and Behavioral Sciences, 129, 186–190. https://doi.org/10.1016/j.sbspro.2014.03.665
* Drury, A. (2025, May 8). Data Analytics: What It Is, How It's Used, and 4 Basic Techniques. Investopedia. https://www.investopedia.com/terms/d/data-analytics.asp
* Gallup. (2023). The True Cost of Employee Turnover. https://www.gallup.com/workplace
* Herbert, N. (2025, January 14). Mentoring New Employees During the Onboarding Process. Chronus. https://chronus.com/blog/mentoring-new-employees
* Holliday, M. (2021, December 8).What Is Diagnostic Analytics? How It Works and Examples. NetSuite. https://www.netsuite.com/portal/resource/articles/data-warehouse/diagnostic-analytics.shtml
* Kaggle. (n.d.). Employee Turnover Analystics Dataset. https://www.kaggle.com/datasets/akshayhedau/employee-turnover-analytics-dataset?resource=download
* Kelly, R. (2024, August 9). Descriptive Analytics: What It Is and Related Terms. Investopedia. https://www.investopedia.com/terms/d/descriptive-analytics.asp
* Lancaster, L. (2024, August 16). Effects of High Turnover Among Employees. https://stratus.hr/resources/effects-of-high-employee-turnover
* Morris, A. (2021, July 7). Descriptive Analytics Defined: Benefits & Examples. NetSuite. https://www.netsuite.com/portal/resource/articles/erp/descriptive-analytics.shtml
* Ramos, P. R. (2019). The effectiveness of compensation in maintaining employee retention. Social Sciences & Humanities Open, 1, Article 100001. https://doi.org/10.1016/j.ssaho.2019.100001
* Ward, N. (2024, May 1). Here’s How Mentoring Increases Employee Retention. MentorcliQ. https://www.mentorcliq.com/blog/mentoring-increases-employee-retention

 

