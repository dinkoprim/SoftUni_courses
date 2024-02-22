done = False
while not done:
    # accept user inputs
    starting_balance = float(input('Enter the starting investment amount: '))
    number_of_years = int(input('Enter the number of years: '))
    interest_rate = float(input('Enter the interest rate as a %: '))
    yearly_investing = float(input('Enter yearly contribution to savings: '))

    # convert rate into decimal number
    interest_rate /= 100

    # accumulator for total interest and balance
    total_interest = 0
    ending_balance = 0

    # header for the table
    print()
    print("%4s%17s%15s%34s" % ('Years', 'Investment', 'Interest rate', 'Yearly contribution to savings'))
    print("%4s%18s%10s%15s" % (number_of_years, starting_balance, interest_rate, yearly_investing))
    print()
    print("%4s%18s%10s%16s" % ('Year', 'Balance', 'Interest', 'Ending balance'))

    # compute and print results for each year
    for each_year in range(1, number_of_years + 1):
        interest = starting_balance * interest_rate
        ending_balance = starting_balance + interest
        print('%4d%18.2f%10.2f%16.2f' % (each_year, starting_balance, interest, ending_balance))
        starting_balance = ending_balance + yearly_investing
        total_interest += interest

    # display the totals for the period
    print()
    print(f'Ending balance: {ending_balance:.2f}')
    print(f'Total interest: {total_interest:.2f}')
    print(f'Final year interest divided by 12 for monthly expenses: {interest/12:.2f}')

    close_console = input("To exit type 'E', to continue press enter: ")
    if close_console.lower() == 'e':
        done = True
