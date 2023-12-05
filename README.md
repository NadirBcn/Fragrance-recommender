# Fragrance-recommmender
![app](https://github.com/NadirBcn/Fragrance-recommender/assets/94077842/e17a1544-0823-469e-8cf6-3a166129c0e9)

**Final Streamlit web app on :** -(APP currently being moved from heroku to another hosting platform)- 

## Fragrance Recommendation : Project Overview
* Created a fragrance recommendation system using the Content-based method to assist customers in finding products they may like based on products they already appreciate. 
* Scraped over 1000 unique fragrances from sephora API using python scarpy and selenium.
* Engineered multiple features from the text of each perfume description to quantify the most popular scents, families, and notes. In addition to a Score feature to measure the most well-liked brands and perfumes.  
* Used Content-based method based on cosine similarity to generate our recommendation.
* Deployed the built model in a Streamlit web app then hosted it using Heroku.

## Code and Ressource used :
* **Python version:** 3.9.7.
* **Packages:** requests, pandas, selenium, scrapy,matplotlib, json, re, pickle,streamlit.
* **URL Selenium Scrapper GitHub:** https://github.com/LenaNevel/CAPSTONE/blob/master/00_getting_slugs.ipynb



## Web Scrapping
Tweaked the URL Scrapper github repo (above) to get the URL of each fragrance product from https://www.sephora.com/shop/fragrance. Then from each URL, I extracted the product ID and store it in a csv file. 
Finally I used the csv file to go through each of the products, and Sephora API to scrappe the relevent features. With each perfume, I got the following : 
* product_id
* Brand
* Name
* Description
* recommended
* not_recommended
* overall_rating
* max_review
* produit
* User1
* ..
* User100

## Data Cleaning
After the Web Scrapping and in order to go any further in the project, I had to make sure the data was cleaned and usable. I made the following changes :
* Created new feature 'Family' from the Description text.
* New feature 'Scent' from the Description text.
* New feature 'Notes' from the Description text.
* Removed 'produit' column.
* Merged the brand and product name in a new column 'brand_name'
* Added a new dataframe with the top 10% most reviewed product.
* Calculated a 'Score' feature in the previously created df.
* Rearranged column order from the original and new dataframes.

## EDA
I created insightful plots and graphs to look at the distribution of my data and the value counts for numerous categorical variables. Some of the highlights of this part: 

![app2](https://user-images.githubusercontent.com/94077842/182175144-c822bc11-72d7-40f8-b2c4-3ece122734f3.png)![app3](https://user-images.githubusercontent.com/94077842/182175373-9e0de192-0a3f-4f2e-b106-26e42ab0f377.png)![app4](https://user-images.githubusercontent.com/94077842/182175598-22e2737a-e319-4eb1-9c45-3a4b26b6b1bf.png)

## Content-Based Recommender
To build a content-based recommandation system, the only thing we care about is the perfume features, which are contained in this case in the 'Description' column. So I started by cleaning this column and putting the result in a new column named 'Cleaned_Description'. 

Afterwards, I applied TF-IDF (Term Frequency - Inverse Document Frequency) to obtain a matrix where each column represent a word in 'Cleaned_Description' vocabulary (all the words that appear at least in one description) and each row represent a fragrance. This is done to reduce the importance of words that occur frequently and therefore, their significance in computing the final similarity score.

Finally, I built my content-based similarity model based on Cosine similarity.

## train-test split and cross validation
This project is built on Content-based type recommendation. Since it is unsupervised and based entirely on fragrance features, I had to try it myself to see the relevance of the results. The recommendations were in general excellent, the biggest problem were the missing 'price' data, which means that even if the components are comparable, a client who enjoys Chanel scents is unlikely to switch to a mass-market brand.


## Deployment
In this final step, I built a basic streamlit web-app that given a product brand and name, return the six most similar perfumes. 
I finallized my project by hosting the app on Heroku.  

