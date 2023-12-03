# Problem Statement:
•	The main problem statement here is predicting the student’s final grades and identifying the factors that are affecting the grade.

## EDA:
The data used was totally clean and contained no null values. So, In EDA we gained few insights about the student performance they are,
1.	It appears that there is no apparent correlation between the number of absences and academic grades. This observation may be attributed to the possibility that students who take leaves might compensate by obtaining study materials from their peers or making up for missed content, thereby influencing their grades independently of their attendance record.
2.	As student get older, their grades generally go down. But interestingly, in this dataset, individuals in their twenties stand out for their excellent academic performance.
3.	There is a positive correlation of approximately 0.16 between “studytime” and G3. This suggests that, on average, students who spend more time studying tend to achieve higher grades.
4.	There is a negative correlation of approximately -0.10 between traveltime and G3. This implies that, on average, students with longer travel times tend to achieve slightly lower grades.
5.	Teachers and healthcare professionals generally had higher education levels, while parents who stay at home tended to have lower education levels. However, an interesting discovery is that fathers who stay at home have a higher education level than mothers who stay at home.
6.	Parents with a strong educational background have supported their children by providing instruction and guidance. Also, when the parents are working in either health or teacher, their kids tends to have a more marks compared to other jobs.
7.	Students who spent more time with friends generally got lower grades. However, those who was rated activities as 2 tended to have the highest average scores. So we can say that we need to have limit for these kind of activities
8.	There is a slight increase in grades when students are taking part in social activities
9.	G1, G2, G3: The final grades (G1, G2, and G3) are highly positively correlated with each other. This is expected since later grades are likely to be influenced by earlier grades.
10.	Medu and Fedu: Mother's education (Medu) and father's education (Fedu) have a positive correlation, which is reasonable as education levels within a family often correlate.
11.	failures: The number of past class failures is negatively correlated with G1, G2, and G3. This indicates that as the number of failures increases, the final grades tend to decrease.
12.	traveltime: Travel time to school is negatively correlated with study time, suggesting that longer travel times may result in less time available for studying.
13.	freetime and goout: Free time and going out are negatively correlated, meaning that as free time increases, the frequency of going out with friends tends to decrease.

## Feature Engineering & Data Preprocessing:

In feature engineering, as we need to convert the categorical values into numerical ones, we tried both the methods of one hot encoding and label encoder. Both the encoders almost worked the same and almost got the same accuracies. So, we went with a label encoder because some of the columns were already label encoded.
