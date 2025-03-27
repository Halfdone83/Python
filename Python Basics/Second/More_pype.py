v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())


pool_level = (p1 + p2) * h
pipe_1 = p1 * h
pipe_2 = p2 * h

pool_level_percentage = (pool_level / v) * 100

if pool_level < v:
    print(f"The pool is {pool_level_percentage:.2f}% full. Pipe 1: {(pipe_1 / pool_level) * 100:.2f}%. Pipe 2: {(pipe_2 / pool_level) * 100:.2f}%.")
else:
    print(f"For {h:.2f} hours the pool overflows with {pool_level - v:.2f} liters.")



