
# coding: utf-8

# # Using PostgreSQL in Python (with Psycopg2)
# 
# ### Psycopg2
# 
# A library that allows Python to connect to an existing PostgreSQL database to utilize SQL functionality.
# 
# #### Documentation
#  * http://initd.org/psycopg/docs/install.html
# 

# In[ ]:

# After installing with pip install psycopg2
import psycopg2 as pg2


# In[ ]:

# Create a connection with PostgreSQL
# 'password' is whatever password you set, we set password in the install video
user_pw='password'
conn = pg2.connect(database='dvdrental', user='postgres',password=user_pw)


# In[ ]:

# Establish connection and start cursor to be ready to query
cur = conn.cursor()


# In[ ]:

# Pass in a PostgreSQL query as a string
cur.execute("SELECT * FROM payment")


# In[ ]:

# Return a tuple of the first row as Python objects
cur.fetchone()


# In[ ]:

# Return N number of rows
cur.fetchmany(10)


# In[ ]:

# Return All rows at once
cur.fetchall()


# In[ ]:

# To save and index results, assign it to a variable
data = cur.fetchmany(10)


# **Inserting Information**

# In[2]:

query1 = '''
        CREATE TABLE new_tables (
            userid integer
            , tmstmp timestamp
            , type varchar(10)
        );
        '''


# In[ ]:

cur.execute(query1)


# In[ ]:

# commit the changes to the database
conn.commit()


query2 = '''
DROP TABLE new_table;
DROP TABLE new_tables;
'''
cur.execute(query2)
conn.commit()
# In[ ]:

# Don't forget to close the connection!
# killing the kernel or shutting down juptyer will also close it
conn.close()

