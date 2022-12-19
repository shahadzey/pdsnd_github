import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


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
        city = input('Which cities data would you like to explore? Enter chicago, new york city, or washington: ').lower()
        if city in CITY_DATA.keys():
            break
        else:
            print('\nInvalid input.  Please try again.\n')
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('''Which month would you like to explore?  Enter 'all',
'january', 'february', 'march', 'april', 'may', or 'june': ''').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month == 'all':
            print('\nLets get the data for all months.')
            break
        elif month in months:
            print('\nLets get the data for {}.'.format(month.title()))
            break
        else:
            print('\nInvalid input.  Please try again.\n')
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('''Which day of the week would you like to explore?
Enter 'all', 'monday', 'tuesday', etc: ''').lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
        'saturday', 'sunday']
        if day == 'all':
            print('\nLets get the data for everyday.')
            break
        elif day in days:
            print('\nLets get the data for all {}s.'.format(day.title()))
            break
        else:
            print('Invalid input.  Please try again.')
            continue

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

    # extract month, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
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

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0] 
    print("Most common month is: ", most_common_month)
# TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0] 
    print("Most common day of week is: ", most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0] 
    print("Most common Start Time is: ", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station is: ",most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station is: ",most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    """ We will use gruop by to combinde start and end station but we can't use mode() then we use sort values and shows the first number of the row using head(1) """
    combine_stations = df.groupby(['Start Station','End Station'])
    most_combine_stations =  combine_stations.size().sort_values(ascending = False).head(1)
    print('most frequent combination of start station and end station trip is: ',most_combine_stations)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('the total travel time is: ',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('the mean travel time is: ',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    print('the count of user types are: ' , df['User Type'].value_counts() ) 
    
    # TO DO: Display counts of gender
    
    """ we must check the city from user input that isn't have city name washington because doesn't have a coloumns of     genders and year of the birth """

    if city != 'washington':
        print('the count of genders are: ' , df['Gender'].value_counts() )

    # TO DO: Display earliest, most recent, and most common year of birth
    print('the earliest year is: ' , df['Birth Year'].min() )
    print('the recent year is: ' , df['Birth Year'].max() )
    print('the most common year is: ' , df['Birth Year'].mode()[0] )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
  

# view raw data
def show_row_data(df):
    row = 0
    while True:
        view_raw_data = input("would you like see the raw data? if yes Enter 'Y' if no Enter 'N'.\n").lower() 
        if view_raw_data == "y":
            print( df.iloc[ row : row + 6] )
            row += 6
        elif view_raw_data == "n":
            break
        else:
            print(" sorry you enter wrong Input , try again")
            
        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()