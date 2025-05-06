from flask import Flask, request, jsonify
import lesson_03_02
import lesson_03_03
import lesson_03_04
import lesson_03_05
import lesson_03_06
import lesson_03_07_08_09

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Python Functions API",
        "available_endpoints": [
            "/lesson_03_02/double",
            "/lesson_03_03/filter_even",
            "/lesson_03_04/add",
            "/lesson_03_04/create_multiplier",
            "/lesson_03_05/list_comprehension",
            "/lesson_03_06/reduce_sum",
            "/lesson_03_07_08_09/analyze_salaries"
        ]
    })

# Routes for each lesson
@app.route('/lesson_03_02/double', methods=['GET'])
def double_route():
    try:
        # Get the value from the request parameters
        value = request.args.get('value')
        if value is None:
            return jsonify({"error": "Please provide a 'value' parameter"}), 400
        
        # Convert to integer
        value = int(value)
        
        # Call the function from the module
        result = lesson_03_02.double(value)
        
        # Return the result as JSON
        return jsonify({"original": value, "doubled": result})
    except ValueError:
        return jsonify({"error": "Value must be a valid integer"}), 400

@app.route('/lesson_03_03/filter_even', methods=['GET'])
def filter_even_route():
    try:
        # Get the list from query parameters
        numbers_str = request.args.get('numbers', '')
        if not numbers_str:
            return jsonify({"error": "Please provide 'numbers' parameter as comma-separated values"}), 400
        
        # Convert to list of integers
        numbers = [int(num.strip()) for num in numbers_str.split(',')]
        
        # Call the function
        result = lesson_03_03.filter_even(numbers)
        
        # Return the result
        return jsonify({"original": numbers, "even_numbers": result})
    except ValueError:
        return jsonify({"error": "All values must be valid integers"}), 400

@app.route('/lesson_03_04/add', methods=['GET'])
def add_route():
    try:
        # Get the parameters
        x = request.args.get('x')
        y = request.args.get('y')
        
        if x is None or y is None:
            return jsonify({"error": "Please provide both 'x' and 'y' parameters"}), 400
            
        # Convert to integers
        x = int(x)
        y = int(y)
        
        # Call the function
        result = lesson_03_04.add(x, y)
        
        # Return the result
        return jsonify({"x": x, "y": y, "sum": result})
    except ValueError:
        return jsonify({"error": "Values must be valid integers"}), 400

@app.route('/lesson_03_04/create_multiplier', methods=['GET'])
def create_multiplier_route():
    try:
        # Get multiplier and value
        multiplier = request.args.get('multiplier')
        value = request.args.get('value')
        
        if multiplier is None or value is None:
            return jsonify({"error": "Please provide both 'multiplier' and 'value' parameters"}), 400
        
        # Convert to integers
        multiplier = int(multiplier)
        value = int(value)
        
        # Create the multiplier function and use it
        multiply_func = lesson_03_04.create_multiplier(multiplier)
        result = multiply_func(value)
        
        # Return the result
        return jsonify({
            "multiplier": multiplier,
            "value": value,
            "result": result
        })
    except ValueError:
        return jsonify({"error": "Values must be valid integers"}), 400

@app.route('/lesson_03_05/list_comprehension', methods=['GET'])
def list_comprehension_route():
    try:
        # Get the list from query parameters
        numbers_str = request.args.get('numbers', '')
        operation = request.args.get('operation', 'double')  # default to double
        
        if not numbers_str:
            return jsonify({"error": "Please provide 'numbers' parameter as comma-separated values"}), 400
        
        # Convert to list of integers
        numbers = [int(num.strip()) for num in numbers_str.split(',')]
        
        # Call the appropriate function based on operation
        if operation == 'double':
            result = lesson_03_05.double_list_comp(numbers)
            op_name = "doubled"
        elif operation == 'even':
            result = lesson_03_05.filter_even_list_comp(numbers)
            op_name = "filtered_evens"
        else:
            return jsonify({"error": "Invalid operation. Use 'double' or 'even'"}), 400
        
        # Return the result
        return jsonify({"original": numbers, op_name: result})
    except ValueError:
        return jsonify({"error": "All values must be valid integers"}), 400

@app.route('/lesson_03_06/reduce_sum', methods=['GET'])
def reduce_sum_route():
    try:
        # Get the list from query parameters
        numbers_str = request.args.get('numbers', '')
        if not numbers_str:
            return jsonify({"error": "Please provide 'numbers' parameter as comma-separated values"}), 400
        
        # Convert to list of integers
        numbers = [int(num.strip()) for num in numbers_str.split(',')]
        
        # Call the function
        result = lesson_03_06.get_sum_reduce(numbers)
        
        # Return the result
        return jsonify({"numbers": numbers, "sum": result})
    except ValueError:
        return jsonify({"error": "All values must be valid integers"}), 400

@app.route('/lesson_03_07_08_09/analyze_salaries', methods=['POST'])
def analyze_salaries_route():
    try:
        # Get the employees data from the request body
        employees = request.json
        
        if not employees or not isinstance(employees, list):
            return jsonify({"error": "Please provide a list of employee objects"}), 400
        
        # Validate employee data
        for emp in employees:
            if not all(key in emp for key in ['name', 'salary', 'job_title']):
                return jsonify({"error": "Each employee must have name, salary, and job_title"}), 400
        
        # Call the function
        result = lesson_03_07_08_09.analyze_salaries(employees)
        
        # Return the result
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
