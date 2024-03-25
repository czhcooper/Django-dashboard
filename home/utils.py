# This file is for analysising user's data.

def analyze_data(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # 假设我们只打印前5行作为测试
            for line in lines[:5]:
                print(line.strip())
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
