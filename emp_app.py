from flask import Flask, jsonify, abort, request
app = Flask(__name__)


emp_details = [
    {
        'emp_id': 1,
        'emp_name': 'Rajveer',
        'salary': 7000,
    },
    {
        'emp_id': 2,
        'emp_name': 'Ayush',
        'salary': 7500,
    },
    {
        'emp_id': 3,
        'emp_name': 'Ravi',
        'salary': 6000,
    }
]


@app.route('/emp/v1.0/emp_details', methods=['GET'])
def get_emp_details():
    return jsonify({'emp_details': emp_details})


@app.route('/emp/v1.0/emp_details/<int:Id>', methods=['GET'])
def get_emp_detail(Id):
    emp_detail = [id for id in emp_details if id['emp_id'] == Id]
    if len(emp_detail) == 0:
        abort(404)
    return jsonify({'emp_details': emp_detail[0]})


@app.route('/emp/v1.0/emp_details', methods=['POST'])
def add_emp():
    if not request.json:
        abort(400)
    new_emp = {
        'emp_id': request.json['emp_id'],
        'emp_name': request.json['emp_name'],
        'salary': request.json['salary'],
    }
    emp_details.append(new_emp)
    return jsonify({'emp_detail': new_emp}), 201


@app.route('/emp/v1.0/emp_details/<int:Id>', methods=['PUT'])
def update_emp_details(Id):
    emp_detail = [id for id in emp_details if id['emp_id'] == Id]
    if len(emp_detail) == 0:
        abort(404)
    elif not request.json:
        abort(400)
    elif 'emp_id' in request.json and type(request.json['emp_id']) != int:
        abort(400)
    elif 'emp_name' in request.json and type(request.json['emp_name']) != str:
        abort(400)
    elif 'emp_salary' in request.json and type(request.json['emp_salary']) != int:
        abort(400)
    emp_detail[0]['emp_id'] = request.json.get('emp_id', emp_detail[0]['emp_id'])
    emp_detail[0]['emp_name'] = request.json.get('emp_name', emp_detail[0]['emp_name'])
    emp_detail[0]['salary'] = request.json.get('salary', emp_detail[0]['salary'])
    return jsonify({'emp_detail': emp_detail[0]})


@app.route('/emp/v1.0/emp_details/<int:Id>', methods=['DELETE'])
def delete_emp_detail(Id):
    emp_detail = [id for id in emp_details if id['emp_id'] == Id]
    if len(emp_detail) == 0:
        abort(404)
    emp_details.remove(emp_detail[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
