
# Set up Spark Session here

##########################################################
# Structured streaming basics
##########################################################

"""
    Exercise:
    - read the stocks data as a stream
    - write the stocks streaming DF to the console
"""

# trigger demonstration

# streaming aggregations

"""
    Exercise:
    1.  Read a stream of numbers from the socket (Netcat or socket application), and
        compute an up-to-date average of all the numbers received.
    2.  Read a stream of names from the socket and count the number of occurrences of each unique name.
"""

# streaming joins

##########################################################
# DStreams
##########################################################

# reading DStreams from socket
# reading DStreams from files
# DStreams transformations

"""
    Exercise: read people-data from the socket (lines randomly fed from people-1m dataset) and
    1. Show a DStream containing people's full names and their salary
    2. Show a DStream containing people's first,middle and last names on separate rows
    3. Show a DStream containing just high-income people (salary > 80000)
    4. Count the number of people in every batch
    5. Count the number of occurrences of each unique first name, with
        a) countByValue
        b) reduceByKey
"""

# DStreams window transformations

"""
     Exercise: read words from the socket. Assume:
         Word longer than 10 chars => $2
         Every other word => $0
    
     Input text into the socket => show the money made over the past 30 seconds, updated every 10 seconds.
     - use window
     - use countByWindow
     - use reduceByWindow
     - use reduceByKeyAndWindow
"""


##########################################################
# Integrations
##########################################################

# JDBC
# Kafka

##########################################################
# Advanced Streams
##########################################################

# window functions
# event time

"""
    Exercises: read the purchases DF as a stream (ideally from socket)
    1. Show the best selling product of every day, +quantity sold.
    2. Show the best selling product of every 24 hours, updated every hour.
"""

# processing time
# watermarks

if __name__ == '__main__':
    pass
