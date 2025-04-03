def chèn_tag_html(S, T):
    # Tạo chuỗi HTML chứa S trong tag T
    return f"<{T}>{S}</{T}>"

# Nhập chuỗi S và tên tag T từ người dùng
S = input("Nhập chuỗi S: ")
T = input("Nhập tên tag HTML T (ví dụ: 'i', 'b', 'h1', v.v.): ")

# Tạo và in ra chuỗi HTML
result = chèn_tag_html(S, T)
print(result)
