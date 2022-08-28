import statistics
import random
integers = [random.randint(0, 100) for _ in range(0, 1000)]
uniforms = [random.uniform(0, 100) for _ in range(0, 1000)]
normals = [random.normalvariate(500, 0.5) for _ in range(0, 1000)]

integers_mean = statistics.mean(integers)
integers_std = statistics.stdev(integers)
uniforms_mean = statistics.mean(uniforms)
uniforms_std = statistics.stdev(uniforms)
normals_mean = statistics.mean(normals)
normals_std = statistics.stdev(normals)

print(f"{integers_mean=}")
print(f"{integers_std=}")
print(f"{uniforms_mean=}")
print(f"{uniforms_std=}")
print(f"{normals_mean=}")
print(f"{normals_std=}")
