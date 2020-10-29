## Beating the Airbnb Market

---
### Project Proposal
Using historic Airbnb Data for the city of Berlin; is it possible to determine whether a home would make a good investment for rental income?  Additionally, if you are currently renting your home out, are there things you can do to make your listing more competitive.  
   * **Data** - Kaggle has a comprehensive dataset of every Airbnb listing in the city of Berlin (~22,000 homes).  In addition it contains rental history for every home in the above list which should give a good idea of the vacancy rate for each home. Dataset can be found here: [Berlin Airbnb](https://www.kaggle.com/brittabettendorf/berlin-airbnb-data)
   * *Why Berlin? I purposely wanted a city that I know nothing about.  I wanted the data to tell the story and not any any prior knowledge I had about the local housing market.* 

**Motivation:**
As much as I love working in an office, I have always been interested purchasing a home for rental income.  When looking for potential homes, I've never had a straightforward way to estimate what the monthly cashflow would be based on the information provided on a site like Zillow, nor have I been able to conclusively determine if a home is worth it.  My hope with this analysis is that I could plug in certain features from Zillow, and see whether a home is potentially worth looking into.  In addition, I hope this analysis will highlight the key factors that affect what makes a home a good investment.   

---
### Tools Used
1. SQL to create and extract the data. [Data Generation]
1. Pandas, Numpy, Regex and Linear Regression to engineer various features. [Data Cleaning] 
1. Seaborn, Folium and Choropleth to visualize the data. [EDA]
1. Random Forest, Logistic Regression, and Support Vector Classification algorithms to classify homes in a "Above Average"/"Below Average" bucket. [Classification]

---
### Features  
* **Target Variable:** Whether a listing's monthly cash flow is greater than the median cash flow within a given neighborhood.  
* **Given Numerical:** Number of (bedrooms, beds, bathrooms, and accommodations), review score, and cleaning fee.
* **Given Categorical:** Cancellation Policy, room type, neighborhood, host response time and existence of certain amenities
* **Engineered Features:** 
    * Apartment Size- Extracted from the description field
    * Distance from the city center
    * Number of amenities
    * Length of the description field

----
### Key Takeaways
**Obvious** Factors below by far played the largest role in determining cash flow for a given listing. 
    
   * Size, Distance from City Center, Number of people that can be accommodated, and Number of Bedrooms

**Honestly, this doesn't really reveal anything you already don't know. Here are a few things that did surprise me!!**

   * Bed Type had low impact.  This is important if you have a smaller place with an extra sofa.  You can claim that sofa as a bed and increase the number of people that your place can accommodate
   * Flexible Cancellation policy had a low impact.  This means that you could shift to a more strict policy and shield yourself from lost out on income due to last minute cancellations
   * Having more amenities matters, even if you don't think they are important(i.e. shampoo, toaster)
   * Simply having a more detailed description had a small effect on increasing your monthly cash flow. 
