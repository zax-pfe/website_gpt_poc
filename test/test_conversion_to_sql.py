import sys
import os 

current_dir = os.getcwd() 
sys.path.insert(0, current_dir)

from translation_natural_language_sql import Convert_to_sql



sql_convertor = Convert_to_sql()

response = sql_convertor.generate_response("all the sci fi movies that were released in 2002")

print("response : ", response)
