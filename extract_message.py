import json

message = """{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "SELECT * FROM movies WHERE genre LIKE '%Sci-Fi%' AND year_of_production BETWEEN 2000 AND 2005",
        "role": "assistant"
  ],
  "created": 1681376310,
  "id": "chatcmpl-74n4gkSiKI8l9lYF03DS8FFc4isTH",
  "model": "gpt-4-0314",
    "completion_tokens": 23,
    "prompt_tokens": 264,
    "total_tokens": 287
  }
  """


print(message["choices"])