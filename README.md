# Exploratory Data Analysis (EDA) - US Ultra Marathon Races (2020)

## Project Overview
This project performs an end-to-end Exploratory Data Analysis (EDA) on a massive global dataset of Ultra Marathon races. The primary objective is to clean raw data, perform feature engineering, and uncover key behavioral and performance insights regarding athletes competing in the United States (`USA`) during the year `2020` for two major race distances: **50km** and **50 miles (50mi)**.

## Tech Stack
- **Language:** Python (3.x)
- **Data Wrangling:** Pandas (Optimized memory management using `low_memory=False`, advanced `Method Chaining`, `Query`, and `Vectorized String Manipulation`)
- **Data Visualization:** Seaborn, Matplotlib

## Data Cleaning & Preprocessing Workflow
Real-world data is often noisy and inconsistent. The data preparation pipeline consists of the following steps:
1. **Target Data Filtering:** Extracted records exclusively for races held in the `USA`, occurring in `2020`, and covering distances of either `50km` or `50mi`.
2. **String Manipulation:** Parsed text columns to isolate clean event names and stripped unit characters (e.g., removing the trailing `' h'` from the `Athlete performance` time column).
3. **Feature Engineering:** - Calculated the exact `Athlete age` by subtracting the birth year from the event year.
   - Categorized race months into their respective weather seasons (`winter`, `spring`, `summer`, `fall`) using an optimized dictionary mapping approach.
4. **Memory Optimization & Missing Values:** Dropped redundant features (`Athlete club`, `Athlete country`, etc.) to minimize RAM consumption and audited the dataset for missing data (`NaN/Null`).

## 📊 Key Insights & Advanced Aggregations
Using advanced Pandas method chaining (`groupby`, `agg`, `sort_values`, `query`), this project answers critical analytical questions:
- **Age vs. Performance:** Identified which age groups achieved the highest average speed (`avg_speed`) in 50-mile races. To ensure statistical significance and eliminate outliers, groups with a sample size of fewer than 20 athletes were filtered out.
- **Seasonal Distribution:** Analyzed runner turnouts and average speeds across different seasons to determine peak performance periods.
- **Demographic Distribution:** Utilized Seaborn's `histplot` to visualize the overall age distribution among ultra-marathon participants.

## How to Run
1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/chucuudangiu-sys/Exploratory-Data-Analysis-With-Python-Pandas.git](https://github.com/chucuudangiu-sys/Exploratory-Data-Analysis-With-Python-Pandas.git)
