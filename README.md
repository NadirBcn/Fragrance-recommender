# Fragrance-recommmender
![app](https://user-images.githubusercontent.com/94077842/182139214-476f1d19-c4b5-4eb3-bf71-624ffb16525c.PNG)

**Final Streamlit web app on :** https://frag-recom.herokuapp.com/

## Fragrance Recommendation : Project Overview
* Created a fragrance recommendation system using the Content-based method to assist customers in finding products they may like based on products they already appreciate. 
* Scraped over 1000 unique fragrances from sephora website using python scarpy and selenium.
* Engineered multiple features from the text of each perfume description to quantify the most popular scents, families, and notes. In addition to a Score feature to measure the most well-liked brands and perfumes.  
* Used Content-based method based on cosine similarity to generate our recommendation.
* Deployed the built model in a Streamlit web app hosted using Heroku.

## Code and Ressource used :
**Python version:** 3.9.7.
**Packages:** requests, pandas, selenium, scrapy,matplotlib, json, re, pickle.
**URL Selenium Scrapper GitHub:** https://github.com/LenaNevel/CAPSTONE/blob/master/00_getting_slugs.ipynb



## Web Scrapping
Tweaked the URL Scrapper github repo (above) to get the URL of each fragrance product from https://www.sephora.com/shop/fragrance. Then from each URL, I extracted the product ID and store it in a csv file. Finally I used the csv file to go through each of the products and scrappe the relevent features. With each perfume, we got the following : 
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
I created insightful plots and graph and looked at the distribution of my data and the value counts for numeorus categorical varialbles. Some of the highlights of this part: 





