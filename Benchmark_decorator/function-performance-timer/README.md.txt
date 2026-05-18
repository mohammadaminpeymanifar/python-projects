Python Performance Benchmark Decorator

A simple but powerful Python project that demonstrates how to measure function execution time using a custom decorator.
This project is designed for learning decorators, performance measurement, and clean Python code structure.

## Features
- Measure execution time of any function
- Support multiple runs (benchmarking)
- Calculate average execution time
- Uses functools.wraps for best practices
- Uses time.perf_counter() for high precision timing
- What You Learn

## This project helps you understand:

- Python decorators
- Higher-order functions
- Function wrapping
- Performance measurement techniques
- Writing reusable utilities in Python

## Example Usage

@benchmark(repeat=5)
def create_list(n):
    return list(range(1, n + 1))

result = create_list(100000)


### Sample Output
==============================
Function: create_list
Runs: 5
Average Execution Time: 0.003214 seconds
==============================