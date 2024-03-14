import pandas as pd
import demographic_data_analyzer as dda


df = pd.read_csv('adult.csv')
print("1- RACE COUNT IS:", dda.race_count(df))
print("2 - Average age of men:", dda.average_age_of_men(df))
print("3- Percentage of people with Bachelor's degree:", dda.percentage_bachelors(df), "%")
print("4- Percentage of people with advanced education making more than 50K:", dda.percentage_advanced_education(df), "%")
print("5- Percentage of people without advanced education make more than 50K:", dda.percentage_high_income_no_advanced_education(df), "%")
print("6- Minimum number of hours a person works per week:", dda.minimum_hours_worked_per_week(df))
print("7- Percentage of the people who work the minimum number of hours per week and have a salary of more than 50K:", dda.percentage_min_workers_high_income(df), "%")
print("8- Country with the highest percentage of people that earn >50K:", dda.highest_earning_country(df))
print("9- Most popular occupation for those who earn >50K in India:", dda.top_IN_occupation(df))
  