# Logs-Analysis Project

In this Udacity Full-stack nano degree project, I built an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.  
The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, the code will answer questions about the site's user activity.  
The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.


# How to run the program
1. Install VM using VirtualBox and install Vagrant for VM settings
2. Configure the VM by running in the folder [vargrant up]  
3. Run vargrant ssh for logging into the VM  
4. Put "news data" into working folder  
5. Run psql -d news -f newsdata.sql 
6. After generating the database, run reporting.py to get the report


# Description of the program's design

The project provided a SQL file to generate a PostgreSQL database  
and a Vagrantfile settings to run a VM server to run the database.

SQL--> database <-- VM <-- Vargrantfile setting