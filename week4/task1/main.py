from math_operations import basic_operations, power_operation, apply_operations

# Test basic_operations
result_basic = basic_operations(10, 5)
print("Basic Operations Result:", result_basic)

# Test power_operation
result_power = power_operation(2, 3)
print("Power Operation Result:", result_power)

# Test power_operation with modulo
result_power_modulo = power_operation(2, 3, modulo=5)
print("Power Operation with Modulo Result:", result_power_modulo)

# Test apply_operations
operations = [
    (lambda x, y: x + y, (3, 4)),
    (lambda x, y: x * y, (2, 5)),
]

result_apply = apply_operations(operations)
print("Apply Operations Result:", result_apply)
