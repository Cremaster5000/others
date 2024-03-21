"""This is a exercise where you can tell how many days are between two 
diferent dates ("dd/MM/YYYY"), it only takes the diference no matther wich one is older"""



def countDays(date_1,date_2):
	days_1 = int(date_1[0:2])
	months_1 = int(date_1[3:5])
	years_1 = int(date_1[6:10])

	days_2 = int(date_2[0:2])
	months_2 = int(date_2[3:5])
	years_2 = int(date_2[6:10])

	total_years = abs(years_1-years_2)
	total_months = abs(months_1-months_2)
	total_days = abs(days_1-days_2)

	print(f'Days: {total_days}, months: {total_months}, total years: {total_years}')
	print(f'or total days: {total_years*365+total_months*30+total_days}')


date_1 = input("Put the first date in format (dd/MM/YYYY): ")
date_2 = input("Put the second date in format (dd/MM/YYYY): ")
countDays(date_1,date_2)
