# Project Description

Given a customer dataset collected by a strategy team of a mall. (CustomerID, Gender, Age, Annual Income, Spending Score (1-100)

The goal is to understand and identify the customers with some patterns based on this data. 

Two clustering methods were used to categorized the customers.

## K-Means Clustering
Before jumped into applying kmeans clustering to this dataset. We need to utlize elbow method to find the optimal number of clusters. 

Number of clusters tested were from 1 to 10. The within-cluster sum of squares were calculated for 10 different number of clusters.

Viewing the wcss value generated, we can identify the optimal number of cluster is 5.
![](images/wcss.PNG)

Applying the k-means clustering to the dataset we can categorize the customers to 5 groups. The customers from the target group are target customers the marketing team should focus on.

![](images/k-means.png)
