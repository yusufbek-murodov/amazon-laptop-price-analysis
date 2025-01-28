# Laptop Price and Feature Analysis

This project analyzes a dataset of laptop specifications and prices to uncover trends in the laptop market. It uses data visualization techniques to provide clear insights into price distributions, feature relationships, brand market share, and other key factors influencing laptop pricing.

## Overview

The goal of this analysis is to understand:

*   The range and distribution of laptop prices.
*   The correlation between price and key features (RAM, Storage, CPU).
*   The market share of different brands.
*   The relationship between ratings, reviews and laptop features.
*   The distribution of different operating systems.
*   How key factors correlate with price.

These insights can be useful for a variety of purposes, from informing consumer purchase decisions to understanding competitive pricing strategies.

## Data Source

The data used for this project was compiled from publicly available laptop listings. The dataset is provided in the `cleaned_data.csv` file, and contains the following attributes:
* `brand_name`: The brand of the laptop.
* `model_name`: The model name of the laptop.
* `screen_size`: The screen size of the laptop.
* `ram`: The RAM of the laptop.
* `storage`: The storage capacity of the laptop.
* `cpu`: The CPU of the laptop.
* `operating_system`: The operating system installed on the laptop.
* `price`: The price of the laptop.
* `rating`: The rating of the laptop.
* `reviews`: The number of reviews of the laptop.
* `graphics`: The type of graphics card.
* `card_description`: If it is an integrated or dedicated card.

## Analysis and Visualizations

The analysis was performed using Python with libraries including pandas, matplotlib, and seaborn. Here are the key visualizations produced:

### 1. Distribution of Laptop Prices

#### Histogram of Prices
![Distribution of Laptop Prices](/images/image_1_1.png)

*   **Purpose:** This histogram visualizes the distribution of laptop prices within the dataset. It allows us to observe the concentration of prices across different ranges.
*   **Insight:**  The distribution of laptop prices is right-skewed, with the majority falling between 300 $ to 600 $. There are also some higher-end laptops priced at 1,000 $ and above, indicating some outliers in the price.
*   **Skills Demonstrated:** Distribution analysis, histogram creation.

#### Box Plot of Prices by Brand
![Price Distribution by Brand](/images/image_1_2.png)

*   **Purpose:** This box plot allows us to see how price varies between different brands.
*   **Insight:**  This box plot shows us that Dell and HP have a similar range of prices. We can also see that HP has some higher outliers, showing they have higher prices.
*   **Skills Demonstrated:** Comparison of distributions, box plot creation.

### 2. Price vs. Features

#### Scatter Plot of Price vs. RAM
![Price vs. ram](/images/image_2_1.png)

*   **Purpose:**  This scatter plot shows the relationship between laptop prices and RAM, colored by the CPU
*   **Insight:** There is a general upward trend of price increasing as RAM increases. We can also see that intel core cpus tend to be in the higher range, and also more clustered.
*   **Skills Demonstrated:** Correlation analysis, scatter plot creation.

#### Scatter Plot of Price vs. Storage
![Price vs. storage](/images/image_2_2.png)

*   **Purpose:**  This scatter plot shows the relationship between laptop prices and Storage, colored by the CPU.
*   **Insight:** There is a general upward trend of price increasing as storage increases, but not as strongly as price and ram.  We can also see that intel core cpus tend to be in the higher range, and also more clustered.
*   **Skills Demonstrated:** Correlation analysis, scatter plot creation.

### 3. Brand Market Share

#### Bar Chart of Laptop Count by Brand
![Laptop Count by Brand](/images/image_3_1.png)

*   **Purpose:** This bar chart shows the number of laptop models listed for each brand in the dataset.
*   **Insight:** HP has the highest number of laptop listings compared to Dell, indicating a larger share of the market in this dataset.
*  **Skills Demonstrated:** Count analysis, bar plot creation

#### Pie Chart of Brand Shares
![Brand Share of Laptops](/images/image_3_2.png)

*   **Purpose:**  This pie chart represents the percentage share of laptop listings for each brand.
*   **Insight:**  HP has 75% of the listings and Dell has 25%.
*  **Skills Demonstrated:** Proportional analysis, pie chart creation.

### 4. Average Price by Brand and Feature

#### Bar Chart of Average Price by Brand and RAM
![Average Price by Brand and ram](/images/image_4_1.png)

*   **Purpose:**  This bar chart shows the average price of laptops grouped by brand and RAM.
*   **Insight:** Laptops with more ram have a higher price, we can see that HP 16GB laptops have a higher average price than Dell.
*   **Skills Demonstrated:** Grouped analysis, bar plot creation.

#### Bar Chart of Average Price by Brand and Storage
![Average Price by Brand and storage](/images/image_4_2.png)

*   **Purpose:**  This bar chart shows the average price of laptops grouped by brand and Storage.
*   **Insight:** Laptops with more storage have a higher price, we can see that HP 1TB laptops have a higher average price than Dell.
*   **Skills Demonstrated:** Grouped analysis, bar plot creation.

#### Heatmap of Average Price by RAM and Storage
![Average Price by RAM and Storage](average_price_by_ram_and_storage.png)

*   **Purpose:** This heatmap shows the average price of laptops grouped by ram and storage.
*   **Insight:** It is clearly seen that laptops with more ram and storage have a higher price, also a general trend is observed that price tends to rise more with increase in RAM compared to increase in storage.
*   **Skills Demonstrated:** Bivariate analysis, heatmap creation, feature engineering.

### 5. Operating System Analysis

#### Bar Chart of Laptop Count by Operating System
![Laptop Count by Operating System](laptop_count_by_operating_system.png)

*   **Purpose:** This bar chart displays the count of laptops for each operating system in our dataset.
*   **Insight:** We can see that Windows 11 Home is the most commonly used operating system.
*   **Skills Demonstrated:** Count analysis, bar plot creation

#### Pie Chart of Operating System Shares
![Operating System Share of Laptops](operating_system_share_of_laptops.png)

*   **Purpose:** This pie chart displays the percentage share of operating system for each laptop in our dataset.
*   **Insight:** We can see that Windows 11 Home has an 86% share in the dataset
*   **Skills Demonstrated:** Proportional analysis, pie chart creation.

### 6. Rating Analysis

#### Box Plot of Rating Distribution by Brand
![Rating Distribution by Brand](rating_distribution_by_brand.png)

*   **Purpose:** This box plot represents the distribution of ratings by brand.
*   **Insight:** We can see that rating is very similar between the brands, and the ratings have a very narrow range.
*   **Skills Demonstrated:** Distribution analysis, box plot creation

#### Bar Plot of Average Rating by Brand
![Average Rating by Brand](average_rating_by_brand.png)

*   **Purpose:** This bar plot shows the average ratings by each brand
*   **Insight:** We can see that HP has a slightly higher average rating.
*   **Skills Demonstrated:** Average analysis, bar plot creation

### 7. Review Analysis

#### Scatter Plot of Reviews vs Rating
![Number of Reviews vs Rating](number_of_reviews_vs_rating.png)

*   **Purpose:** This scatter plot shows us the correlation between reviews and ratings
*   **Insight:** Laptops with higher ratings tend to have a higher amount of reviews.
*   **Skills Demonstrated:** Correlation analysis, scatter plot creation.

#### Bar Plot of Average Reviews by Brand
![Average Number of Reviews by Brand](average_number_of_reviews_by_brand.png)

*   **Purpose:** This bar plot displays the average number of reviews for each brand
*   **Insight:** HP laptops tend to have a higher average amount of reviews.
*   **Skills Demonstrated:** Average analysis, bar plot creation.

### 8. CPU Analysis
#### Bar Chart of Laptop Count by CPU
![Laptop Count by CPU](laptop_count_by_cpu.png)

*   **Purpose:** This bar chart displays the count of each CPU in the dataset.
*   **Insight:** The Intel core i5 is the most used cpu.
*   **Skills Demonstrated:** Count analysis, bar plot creation

#### Bar Chart of Average Price by CPU
![Average Price by CPU](average_price_by_cpu.png)

*   **Purpose:** This bar chart shows the average price of laptops with each CPU type.
*   **Insight:** Core i5 and Core i7 cpus tend to have higher price compared to other CPUs.
*   **Skills Demonstrated:** Average analysis, bar plot creation

## Key Insights

*   **Price:** Most laptops are priced between 30,000 to 60,000, however, there are some outliers in higher and lower prices.
*   **Features:** Both RAM and storage are positively correlated with price, RAM slightly more than Storage, laptops with intel cpus tend to be costlier.
*   **Market:** HP has more listings and higher brand share than Dell.
*   **Operating System:** Windows 11 Home is the most used OS in the dataset.
*   **Ratings and Reviews:** Laptops with more ratings tend to have more reviews.
*   **CPU:** The core i5 cpu is the most used and costly cpu.

## Conclusion
This project demonstrates effective data analysis and visualization skills, using a practical dataset to gain meaningful insights. This analysis could be useful for potential customers of these laptops and also for laptop companies to see how their pricing compares to other companies.

## Next Steps

*   Further analysis to investigate the impact of dedicated graphics cards and different brands.
*   Building predictive models to estimate the price of a laptop based on its features.
*   Creating an interactive dashboard for a more user-friendly data exploration experience.

## Contact

[Your Name]
[Your Email]
[Link to your LinkedIn, GitHub, etc.]