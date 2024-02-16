from flask import Flask, render_template, request, jsonify
import ctypes

app = Flask(__name__)

lib = ctypes.CDLL('./libbinary_operations.so')  # Nombre del archivo compartido generado al compilar el código C

lib.binary_add.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
lib.binary_add.restype = ctypes.c_uint64

lib.binary_subtract.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
lib.binary_subtract.restype = ctypes.c_uint64

lib.binary_multiply.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
lib.binary_multiply.restype = ctypes.c_uint64

lib.binary_divide.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
lib.binary_divide.restype = ctypes.c_uint64

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/binmath', methods=['POST'])
def binary_math():
    data = request.get_json()
    operation = data.get('operation')
    num1 = int(data.get('num1'), 2)
    num2 = int(data.get('num2'), 2)
    result = 0

    if operation == 'add':
        result = lib.binary_add(num1, num2)
    elif operation == 'subtract':
        result = lib.binary_subtract(num1, num2)
    elif operation == 'multiply':
        result = lib.binary_multiply(num1, num2)
    elif operation == 'divide':
        result = lib.binary_divide(num1, num2)

    result_binary = bin(result)[2:]
    return jsonify({'result': result_binary})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)