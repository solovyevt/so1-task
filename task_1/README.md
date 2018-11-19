Task:

`Create a nagios check that will trigger in case of 3 occurrences of a "Handbill not printed" string in Elasticsearch. 
(If you don't know nagios, you could consider creating script that will output meaningful status)`

This Python script uses _count API to get the number of documents containing string `"Handbill not printed"` in the field `"message"` with selected time period from now.

In need of various usage it can be easily converted to command-line script using dict of arguments.