

import time
import calendar
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

months = { 'all', 'january', 'february', 'march', 'april', 'may', 'june'}

day_of_week = { 'all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

   #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city do you want to choose among chicago, new york city, washington?\n").lower()

        if city in CITY_DATA:
            break
        else:
            print("Sorry you did not choose among Chicago, New Work City or Washington. Try again\n")
            continue


    # get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in months:
        month_name = input("By which month would you like to filter the data? All, January, February, March, April, May, June\n")

        if month_name.lower() in months:
            month = month_name.lower()
        else:
            print("Sorry you did not choose among All, January,..,June.\n")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in day_of_week:
        day_name = input("By which day would you like to filter the data? All, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday\n")

        if day_name.lower() in day_of_week:
            day = day_name.lower()
        else:
            print("Sorry you did not choose among the seven days.\n")


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    common_month = df['month'].mode()[0]
    common_month = calendar.month_name[common_month]
    print('The most common month:', common_month)

    #display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('THe most common day of the week:', common_day)

    #display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', common_start_station)

    #display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', common_end_station)

    #display most frequent combination of start station and end station trip
    combination_trip = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print('Most frequest combination of start station and end station trip:', str(combination_trip.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    #display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:\n', user_types)

    #Display counts of gender
    if city == 'chicago' or city == 'new york city':
        gender = df['Gender'].value_counts()
        print('\nCounts of gender:', gender)

        #Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print('\nEarlist year of birth: {}\n Most recent year of birth: {}\n Most common year of birth: {}\n'.format(earliest_birth_year, recent_birth_year, common_birth_year))

    else:
        print('gender and birth year data are not available for Washinton')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    index=0
    user_input=input('\nWould you like to display 5 rows of raw data? Enter Yes or No\n').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('\nwould you like to display more 5 rows of raw data? Enter Yes or No\n').lower()
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
