"""
带划线的九九乘法表
"""

print("┌───────────────┐")
for i in range(1, 10):
    row = ""
    for j in range(1, i + 1):
        row += f"{j}×{i}={i*j:2d}  "
    print(f"│ {row.ljust(25)} │")
print("└───────────────┘")