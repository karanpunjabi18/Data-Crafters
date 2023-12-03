# Problem Statement:
•	The main problem statement here is predicting the students' final grades and identifying the factors affecting the grades.

## Methodology:
![Methodology_img](https://github.com/karanpunjabi18/Data-Crafters/assets/118504346/ef9a6cf3-9816-4bfe-b25b-ab1fb7b8bba0)


## EDA:
The data used was clean and contained no null values. So, In EDA, we gained a few insights into the student performance they are,
1.	there is no apparent correlation between the number of absences and academic grades. This observation may be attributed to the possibility that students who take leaves might compensate by obtaining study materials from their peers or making up for missed content, thereby influencing their grades independently of their attendance record.
2.	As a student gets older, their grades generally go down. But interestingly, in this dataset, individuals in their twenties stand out for their excellent academic performance.
3.	A positive correlation of approximately 0.16 exists between “studytime” and G3. This suggests that, on average, students who spend more time studying tend to achieve higher grades.
4.	There is a negative correlation of approximately -0.10 between traveltime and G3. This implies that, on average, students with longer travel times tend to achieve slightly lower grades.
5.	Teachers and healthcare professionals generally had higher education levels, while parents who stayed at home tended to have lower education levels. However, an exciting discovery is that fathers who stay at home have a higher education level than mothers who stay at home.
6.	Parents with a solid educational background have supported their children by providing instruction and guidance. Also, when the parents are working in either health or teaching, their kids tend to have more marks compared to other jobs.
7.	Students who spent more time with friends generally got lower grades. However, those activities rated as two tend to have the highest average scores. So we can say that we need to have limits for these kind of activities
8.	There is a slight increase in grades when students are taking part in social activities
9.	G1, G2, G3: The final grades (G1, G2, and G3) are highly positively correlated with each other. This is expected since later grades are likely influenced by earlier grades.
10.	Medu and Fedu: Mother's education (Medu) and father's education (Fedu) have a positive correlation, which is reasonable as education levels within a family often correlate.
11.	failures: The number of past class failures negatively correlates with G1, G2, and G3. This indicates that as the number of failures increases, the final grades tend to decrease.
12.	traveltime: Travel time to school is negatively correlated with study time, suggesting that longer travel times may result in less study time.
13.	freetime and goout: Free time and going out are negatively correlated, meaning that as free time increases, the frequency of going out with friends decreases.

## Feature Engineering & Data Preprocessing:

In feature engineering, as we need to convert the categorical values into numerical ones, we tried both the methods of one hot encoding and label encoder. Both the encoders almost worked the same and almost got the same accuracies. So, we went with a label encoder because some columns were already label encoded.

## Model Building:

We created a custom function that just needs to pass the model and the input & output variables. The function will return us the MSE, R2 Score, and CV Score. Then, we used the Lazy Predict library to get a quick overview of which model performed best on our data.
From the results, we got LightGBM as the best model. Then, after we hyper-tuned this model, we got an accuracy of 84%. Also, we saved the model as a pickle file, which can be used for future predictions while deploying.

## Results Obtained:
We compared three ML models (Linear Regression, Random Forest, and LightGBM) and got the R2 Score as 
```
i)	LightGBM – 0.84
ii)	Linear Regression – 0.80
iii)	RandomForestRegressor – 0.82
```
There are three base models in this code.
- The 1st model has been trained on all 32 features, the 2nd has been trained on only 15 features selected by the SelectKbest parameter function, and the last has been trained on all 32 features. 
- But the main difference between the 1st and 3rd models was the columns were encoded by a label encoder and one hot encoding, respectively.
- The initial model achieved a higher accuracy of 84% by utilizing all available features compared to the second model, which only used the top 15 performing features and achieved an accuracy of 81%. However, the second model demonstrated better usability by achieving a competitive accuracy with fewer features when compared to the first model.

