import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.students
grades = db.grades


def find():

    print "find, reporting for duty"

    query = {"type":"homework"}

    try:
        cursor = grades.find(query)
        cursor = cursor.sort([("student_id",pymongo.ASCENDING),("score",pymongo.ASCENDING)])
    except:
        print "Unexpected error:", sys.exc_info()[0]

    old_id = -1

    #Deleting the lowest score in type: homework for each student.
    for doc in cursor:
    	new_id=doc["student_id"]
    	if old_id!=new_id:
    		grades.remove(doc)
    		old_id=new_id


find()