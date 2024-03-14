import pandas as pd

def race_count(df):
    race_count = df['race'].value_counts().sum()
    return race_count

def average_age_of_men(df):
    average_age = df.groupby('sex')['age'].mean()['Male']
    return average_age

def percentage_bachelors(df):
    bachelor_degree = df['education'].isin(['Bachelors']).sum() * 100 / len(df)
    return bachelor_degree

def percentage_advanced_education(df):
    adv_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & (df['income'] == '>50K')
    percentage = (adv_education.sum() / len(df)) * 100
    return percentage

def percentage_high_income_no_advanced_education(df):
    adv_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & (df['income'] == '>50K')
    percentage = (adv_education.sum() / len(df)) * 100
    return percentage

def minimum_hours_worked_per_week(df):
    minimum_hours = df['hours.per.week'].min()
    return minimum_hours

def percentage_min_workers_high_income(df):
    minimum_hours_50 = df.loc[(df['hours.per.week'] == df['hours.per.week'].min()) & (df['income'] == '>50K')]
    percentage = (len(minimum_hours_50) / len(df[df['hours.per.week'] == df['hours.per.week'].min()])) * 100
    return percentage

def highest_earning_country(df):
    df_filtered = df[(df['income'] == '>50K') & (df['native.country'] != 'NA')]
    country_percentages = (df_filtered['native.country'].value_counts() / df['native.country'].value_counts()).fillna(0)
    max_country = country_percentages.idxmax()
    max_percentage = country_percentages.max() * 100
    return max_country, max_percentage

def top_IN_occupation(df):
    india_high_income = df[(df['native.country'] == 'India') & (df['income'] == '>50K')]
    top_occupation = india_high_income['occupation'].value_counts().idxmax()
    return top_occupation


    