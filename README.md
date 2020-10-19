## Is This Home a good Investment for Rental Income?

**Project Proposal**
* Using historic Airbnb Data for the city of Berlin; is it possible to determine whether a home would make a good investment for rental income?  This analysis will aim to utilize SQL to extract the data, Pandas to prep the data and various classification algorithms to place homes in a "Buy"/"Pass" bucket based on a variety of features.  

**Why Berlin?**
* I purposely wanted a city that I know nothing about.  I wanted the data to tell the story and not any any prior knowledge I had about the local housing market.  

**Motivation**
* As much as I love working in an office, I have always been interested purchasing a home for rental income.  When looking for potential homes, I've never had a straightforward way to estimate what the monthly cashflow would be based on the information provided on a site like Zillow, nor have I been able to conclusively determine if a home is worth it.  My hope with this analysis is that I could plug in certain features from Zillow, and see whether a home is potentially worth looking into.  In addition, I hope this analysis will highlight the key factors that affect what makes a home a good investment.   

**Data Source**
* Kaggle has a comprehensive dataset of every Airbnb listing in the city of Berlin (~20,000).  In addition it contains rental history for every home in the above list which should give a good idea of the vacancy rate for each home.

**Data Intuition**
* Plots like: neighborhood, room_type, rooms, amenities, review rating, proximity to transit, Map View,

**List of potential features:**  

2. Host is superhost
3. Property Type
4. Room Type
5. Number of bedrooms
6. Number of bathrooms
7. Number of people accomodates
8. Bed Type
9. Vacancy Rate
10. Review Score
11. Cancellation Policy
12. Amenities

**Target Variable:**

* Monthly cash flow, based on the price/night and the approximate vacancy. If predicted price is greater than the Median cash flow (by neighborhood), than it is considered a "Potential Buy".
