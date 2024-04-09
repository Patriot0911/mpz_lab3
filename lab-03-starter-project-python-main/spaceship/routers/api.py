from fastapi import APIRouter
import numpy as np

router = APIRouter()

MATRIX_SIZE = 10

@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get('/matrix')
def hello_world() -> dict:
    matrix1 = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)
    matrix2 = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)
    result = np.dot(matrix1, matrix2)
    return {
        "matrix_a": matrix1.tolist(),
        "matrix_b": matrix1.tolist(),
        "product": result.tolist()
    }
