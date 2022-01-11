PI = 3.141592

def number_input():
    """사용자로부터 숫자를 입력받고 형변환(float)하여 리턴 """
    output = input("숫자 입력> ")
    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius