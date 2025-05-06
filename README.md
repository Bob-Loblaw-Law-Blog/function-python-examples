# Python Functions API

This Flask application exposes the functions from Python Lesson 3 Examples as API endpoints. It is designed as a minimal introduction to Flask and server-side API management.

## Setup

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python app.py
   ```

The server will start on `http://localhost:5000`.

## Available Endpoints

### Home
- **URL:** `/`
- **Method:** `GET`
- **Description:** Returns a list of available endpoints

### Lesson 03_02 - Double a Number
- **URL:** `/lesson_03_02/double`
- **Method:** `GET`
- **Parameters:** `value` (integer)
- **Example:** `/lesson_03_02/double?value=5`

### Lesson 03_03 - Filter Even Numbers
- **URL:** `/lesson_03_03/filter_even`
- **Method:** `GET`
- **Parameters:** `numbers` (comma-separated list of integers)
- **Example:** `/lesson_03_03/filter_even?numbers=1,2,3,4,5,6`

### Lesson 03_04 - Add Two Numbers
- **URL:** `/lesson_03_04/add`
- **Method:** `GET`
- **Parameters:** `x` (integer), `y` (integer)
- **Example:** `/lesson_03_04/add?x=5&y=10`

### Lesson 03_04 - Create Multiplier
- **URL:** `/lesson_03_04/create_multiplier`
- **Method:** `GET`
- **Parameters:** `multiplier` (integer), `value` (integer)
- **Example:** `/lesson_03_04/create_multiplier?multiplier=3&value=4`

### Lesson 03_05 - List Comprehension
- **URL:** `/lesson_03_05/list_comprehension`
- **Method:** `GET`
- **Parameters:**
  - `numbers` (comma-separated list of integers)
  - `operation` (string, either 'double' or 'even')
- **Example:** `/lesson_03_05/list_comprehension?numbers=1,2,3,4,5&operation=double`

### Lesson 03_06 - Reduce Sum
- **URL:** `/lesson_03_06/reduce_sum`
- **Method:** `GET`
- **Parameters:** `numbers` (comma-separated list of integers)
- **Example:** `/lesson_03_06/reduce_sum?numbers=1,2,3,4,5`

### Lesson 03_07/08/09 - Analyze Salaries
- **URL:** `/lesson_03_07_08_09/analyze_salaries`
- **Method:** `POST`
- **Body:** JSON array of employee objects
- **Example Body:**
  ```json
  [
    {
      "name": "Jane",
      "salary": 90000,
      "job_title": "developer"
    },
    {
      "name": "Bill",
      "salary": 50000,
      "job_title": "writer"
    }
  ]
  ```

## Example Usage (Python)

Here's how to use the API with Python's requests library:

```python
import requests

# Double a number
response = requests.get('http://localhost:5000/lesson_03_02/double?value=10')
print(response.json())

# Filter even numbers
response = requests.get('http://localhost:5000/lesson_03_03/filter_even?numbers=1,2,3,4,5,6')
print(response.json())

# Add two numbers
response = requests.get('http://localhost:5000/lesson_03_04/add?x=5&y=10')
print(response.json())

# Analyze salaries
employees = [
    {
        "name": "Jane",
        "salary": 90000,
        "job_title": "developer"
    },
    {
        "name": "Bill",
        "salary": 50000,
        "job_title": "writer"
    }
]
response = requests.post('http://localhost:5000/lesson_03_07_08_09/analyze_salaries', json=employees)
print(response.json())
```

## Example Usage (cURL)

```bash
# Double a number
curl "http://localhost:5000/lesson_03_02/double?value=10"

# Filter even numbers
curl "http://localhost:5000/lesson_03_03/filter_even?numbers=1,2,3,4,5,6"

# Add two numbers
curl "http://localhost:5000/lesson_03_04/add?x=5&y=10"

# Analyze salaries
curl -X POST "http://localhost:5000/lesson_03_07_08_09/analyze_salaries" \
     -H "Content-Type: application/json" \
     -d '[{"name":"Jane","salary":90000,"job_title":"developer"},{"name":"Bill","salary":50000,"job_title":"writer"}]'
```
