import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df['education'].value_counts()['Bachelors'] / len(df['education']) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    a = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') |(df['education'] == 'Doctorate')]
    b = df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]
    higher_education = len(a)
    lower_education = len(b)

    # percentage with salary >50K
    higher_education_rich = len(a[a['salary'] == '>50K']) / len(a) *100
    lower_education_rich = len(b[b['salary'] == '>50K']) / len(b) *100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_df = df[df['hours-per-week'] == df['hours-per-week'].min()]
    num_min_workers = len(min_df[min_df['salary']=='>50K']) / len(min_df) *100

    rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
    group1 = df.groupby(['native-country', 'salary']).agg({'salary': 'count'})
    pct = group1.groupby(level=0).apply(lambda x: 100 * x / float(x.sum()))
    pct.columns = ['perc']
    df2 = pd.DataFrame(pct)
    df2 = df2.reset_index()
    c = df2[(df2['salary']=='>50K')]
    highest_earning_country = c[c['perc'] == c['perc'].max()]['native-country'].values[0]
    highest_earning_country_percentage = c[c['perc'] == c['perc'].max()]['perc'].values[0]

    # Identify the most popular occupation for those who earn >50K in India.
    df_india_above_50 = df[ (df['native-country']=='India') & (df['salary'] == '>50K') ]
    top_IN_occupation = df_india_above_50['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:",
              highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

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
