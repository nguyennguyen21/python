solve_system = lambda a, b, c, d, e, f: (
    (c * e - b * f) / (a * e - b * d), (a * f - c * d) / (a * e - b * d)
) if (a * e - b * d) != 0 else (
    "Vô nghiệm" if (c * e - b * f) != 0 or (a * f - c * d) != 0 else "Vô định"
)