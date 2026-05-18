import time

def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print(f"Execution Time: {end_time - start_time:.6f} seconds")

        return result

    return wrapper

@time_logger
def create_list(n):
    return list(range(1, n + 1))

n = int(input("Enter n: "))

result = create_list(n)

print("Result:", result)