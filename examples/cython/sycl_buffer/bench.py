import dpctl
import syclbuffer as sb
import numpy as np

X = np.full((10 ** 4, 4098), 1e-4, dtype="d")

# warm-up
print("=" * 10 + " Executing warm-up " + "=" * 10)
print("NumPy result: ", X.sum(axis=0))

dpctl.set_default_queue("opencl", "cpu", 0)
print(
    "SYCL({}) result: {}".format(
        dpctl.get_current_queue().get_sycl_device().get_device_name(),
        sb.columnwise_total(X),
    )
)

dpctl.set_default_queue("opencl", "gpu", 0)
print(
    "SYCL({}) result: {}".format(
        dpctl.get_current_queue().get_sycl_device().get_device_name(),
        sb.columnwise_total(X),
    )
)

import timeit

print("Times for 'opencl:cpu:0'")
print(
    timeit.repeat(
        stmt="sb.columnwise_total(X)",
        setup='dpctl.set_default_queue("opencl", "cpu", 0); '
        "sb.columnwise_total(X)",  # ensure JIT compilation is not counted
        number=100,
        globals=globals(),
    )
)

print("Times for 'opencl:gpu:0'")
print(
    timeit.repeat(
        stmt="sb.columnwise_total(X)",
        setup='dpctl.set_default_queue("opencl", "gpu", 0); sb.columnwise_total(X)',
        number=100,
        globals=globals(),
    )
)

print("Times for NumPy")
print(timeit.repeat(stmt="X.sum(axis=0)", number=100, globals=globals()))
