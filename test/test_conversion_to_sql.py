import sys
sys.path.insert(0, 'C:\\Users\\33633\\Documents\\website_gpt_poc')

from translation_natural_language_sql import Convert_to_sql



sql_convertor = Convert_to_sql()

response = sql_convertor.generate_response("all the sci fi movies that were released in 2002")

print("response : ", response)
