import sys
sys.path.insert(0, 'C:\\Users\\33633\\Documents\\website_gpt_poc')
from translation_natural_language_sql_gpt4 import Convert_to_sql_gpt4



sql_convertor = Convert_to_sql_gpt4()

response = sql_convertor.generate_response("all the sci fi movies that were released in 2003")

print("response : ", response["choices"][0]["message"]["content"])
