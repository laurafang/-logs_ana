import psycopg2
# the module that connects to the database

"""

The task is to create a reporting tool that prints out reports (in plain text) 
based on the data in the database.
1.What are the most popular three articles of all time? 
Which articles have been accessed the most? Present this information as a sorted list
with the most popular article at the top.
2.Who are the most popular article authors of all time? 
That is, when you sum up all of the articles each author has written, 
which authors get the most page views? Present this as a sorted list with the most 
popular author at the top.
3.On which days did more than 1% of requests lead to errors? 
The log table includes a column status that indicates the HTTP status code that 
the news site sent to the user's browser. (Refer back to this lesson 
if you want to review the idea of HTTP status codes.)

"""
DBNAME = "news"

# Open and connect to database; Run the query; Return database cursor objects
def query(user_query):
	DB = psycopg2.connect(database = DBNAME)
	cursor = DB.cursor()
	cursor.execute(user_query)
	result = cursor.fetchall()
	DB.close()
	return result

# 1. popular article
def pop_article():
	top_article = query(("select * from top three articles"))
	print('The most popular three articles are:')
	for item, views in top_article:
		print(" \"{}\" -- {} views".format(item, views))
# 2. popular author
def pop_author():
	top_authors = query(("select * from top authors"))
	print('The most popular authors are:')
	for names, views in top_authors:
		print(" {} -- {} views".format(name, views))

# 3. error
def error_day():
	errorday = process_query("select * from errorday")
    print("Days with more than 1%  of requests lead to errors")
    for day, percentage in errorday:
        print(" {0:%B %d, %Y} -- {1:.2f} %  errors".format(day, percentage))


if __name__ == '__main__':
	pop_article()
	pop_author()
	error_day()