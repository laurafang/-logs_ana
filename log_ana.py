# -*- coding: utf-8 -*-
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
	top_article = query("select title, count(*) from articles "
              "join log on path like CONCAT('%',slug) group by title "
              "order by count(*) desc limit 3")
	print("The most popular three articles are:")
	for title, views in top_article:
		print(" \"{}\" -- {} views".format(title, views))
# 2. popular author
def pop_author():
	top_authors = query("select name, count(path) from authors "
            "join articles on authors.id = author join log "
            "on path like CONCAT('%', slug) group by name order by count(path) desc limit 4")
	print('The most popular authors are:')
	for name, views in top_authors:
		print(" {} -- {} views".format(name, views))

# 3. error
def error_day():
    errorday = query("select date, avg from ("
            "select date, (sum(error) / (select count(*) "
            "from log where (time::date) = date)) as avg "
            "from (select (time::date) as date, count(*) as error "
            "from log where status like '4%' group by date) "
            "as error_percentage group by date order by avg  desc) as final "
            "where avg >= .01")
    print('Days with more than 1%  of requests lead to errors')
    for res in errorday:
        print (str(res[0]) + " — " + str(round((res[1]*100), 2)) +
               '%')


if __name__ == '__main__':
	pop_article()
	pop_author()
	error_day()
