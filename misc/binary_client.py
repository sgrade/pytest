import httpx

base_url = "http://127.0.0.1:8000"

response = httpx.post(url=base_url, json={"num": 5})
output_bytes = response.content

print(output_bytes)
