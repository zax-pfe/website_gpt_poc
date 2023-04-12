from translation_natural_language_sql_gpt4 import Convert_to_sql



sql_convertor = Convert_to_sql()

response = sql_convertor.generate_response("all the sci fi movies that were released in 2003")

print("response : ", response)
