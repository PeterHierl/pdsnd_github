# Import the required Python packages
import time
import pandas as pd
import numpy as np

#Load and prepare the data sets
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york city', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

# Function to filter the data
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please choose one city from: Chicago, New York City or Washington. \n')
        if city.lower() not in CITIES:
            print('Your city was not in the list: Chicago, New York City or Washington. \n')
        else:
            city = city.lower()
            break
    print('{} is the city of your choice.'.format(city.title()))

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which months do you want: January, February, March, April, May, June or \"All\" \n")
        if month.lower() not in MONTHS:
            print("Your month was not in the list: January, February, March, April, May, June or \"All\" \n")
        else:
            month = month.lower()
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day you want to see: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or \"All\"? \n")
        if day.lower() not in DAYS:
            print("Your day was not in the list: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or \"All\"? \n")
        else:
            day = day.lower()
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = MONTHS.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    pop_month = df['month'].value_counts().idxmax()
    print('The most common month is: {} \n'.format(pop_month))

    # TO DO: display the most common day of week
    pop_day = df['day_of_week'].value_counts().idxmax()
    print('The most common day is: {} \n'.format(pop_day))

    # TO DO: display the most common start hour
    pop_hour = df['hour'].value_counts().idxmax()
    print('The most common hour is: {} \n'.format(pop_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is {}\n'.format(pop_start_station))

    # TO DO: display most commonly used end station
    pop_end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is {}\n'.format(pop_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    pop_start_end = df[['Start Station', 'End Station']].mode().loc[0]
    print('The most frequent combination of start station and end station trip'
    ' is from \n {} to {} \n'.format(pop_start_end[0], pop_start_end[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_tt = df['Trip Duration'].sum()
    print('The total travel time is {} \n'.format(total_tt))

    # TO DO: display mean travel time
    mean_tt = df['Trip Duration'].mean()
    print('The mean travel time is {} \n'.format(mean_tt))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The count of the user types: \n')
    for i, user_type in enumerate(user_types):
        print(' {}: {} \n'.format(user_types.index[i], user_type))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        count_genders = df['Gender'].value_counts()
        print('The count of the genders is: \n ')
        for i, count_gender in enumerate(count_genders):
            print(' {}: {} \n'.format(count_genders.index[i], count_gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        print('The earliest year of birth is: {} \n'.format(earliest_year))
        most_recent = df['Birth Year'].max()
        print('The most recent year of birth is: {} \n'.format(most_recent))
        most_common = df['Birth Year'].value_counts().idxmax()
        print('The most common year of birth is: {} \n'.format(most_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw_data(df):
    """Displays 5 rows of the raw data."""
    rows = True
    start = 0
    end = 5
    while rows:
        rows = input('Would you like to see 5 rows of the raw data, yes or no \n')
        while rows.lower() not in ['yes', 'no']:
            rows = input('Please enter yes or no. \n')
        if rows.lower() != 'yes':
            break
        print(df[start:end])
        start += 5
        end += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
