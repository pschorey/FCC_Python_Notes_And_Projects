import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df =  pd.read_csv('adult.data.csv', index_col=None, sep=',')
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.

    race_count = df['race'].value_counts()
    #print('race count',df.count(axis='race'))

    # What is the average age of men?
    male_df = df[df['sex'] == 'Male'] #creates a data frame where all the results are only male
    average_age_men = round(male_df['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors = df[df['education'] == 'Bachelors']
    percentage_bachelors = round((len(bachelors) / len(df.education == 'Bachelors'))*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    educated = len(df[
        ((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))])
    educated_and_rich = df[
        ((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))
        & (df['salary'] == '>50K')]

    uneducated = len(df[
        ((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate'))])
    union_workers = len(df[
        ((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')) 
        & (df['salary'] == '>50K')])

    # percentage with salary >50K
    higher_education_rich = round((len(educated_and_rich) / educated)*100,1)
    lower_education_rich = round((union_workers / uneducated)*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df['hours-per-week'] == 1])
    num_min_over_50k = len(df[
    ((df['hours-per-week'] == 1) & (df['salary'] == '>50K'))])
    rich_percentage = round((num_min_over_50k / num_min_workers)*100,1)

    # What country has the highest percentage of people that earn >50K?
    topCountry = ''
    topPercentage = 0
    earn_over_50k = df[df['salary'] == '>50K']
    country_count_over_50k = earn_over_50k['native-country'].value_counts()
    country_counts = df['native-country'].value_counts()

    for k,v in country_count_over_50k.items():
        #print('>50k',k,v)
        percentage = v/country_counts[k]
        if (percentage >= topPercentage):
            topPercentage = percentage
            topCountry = k
    topPercentage = round(topPercentage * 100,1)

    highest_earning_country = topCountry
    highest_earning_country_percentage = topPercentage

    # Identify the most popular occupation for those who earn >50K in India.
    india_jobs_over_50k =df[
        ((df['native-country'] == 'India') & (df['salary'] == '>50K'))]
    jobArr = india_jobs_over_50k['occupation'].value_counts()
    jobIndex = 0
    topJob = ''
    for k,v in jobArr.items():
        if (jobIndex == 0):
            topJob = k
            jobIndex += 1

    top_IN_occupation = topJob

    # DO NOT MODIFY BELOW THIS LINE
    '''
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)
    '''
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
