def count_prime_divisors(n):
    count = 0
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:

            # بررسی اول بودن divisor
            is_prime = True

            for i in range(2, divisor):
                if divisor % i == 0:
                    is_prime = False
                    break

            if is_prime:
                count += 1

                # حذف تمام توان‌های divisor
                while n % divisor == 0:
                    n //= divisor

        divisor += 1

    return count


max_count = -1
max_number = -1

for _ in range(10):
    num = int(input())

    prime_div_count = count_prime_divisors(num)

    if (prime_div_count > max_count) or (
        prime_div_count == max_count and num > max_number
    ):
        max_count = prime_div_count
        max_number = num

print(max_number, max_count)