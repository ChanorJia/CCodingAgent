import sys

def fibonacci_sum(n):
    """计算斐波那契数列前 n 项的和（从第1项 F(1)=1 开始）"""
    if n <= 0:
        return 0
    if n == 1:
        return 1

    a, b = 1, 1  # F(1), F(2)
    total = a + b  # 前两项的和

    for _ in range(3, n + 1):
        c = a + b
        total += c
        a, b = b, c

    return total

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("用法: python fib.py <n>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 1:
            print("n 必须为正整数")
            sys.exit(1)
    except ValueError:
        print("请输入一个整数")
        sys.exit(1)

    result = fibonacci_sum(n)
    print(f"斐波那契数列前 {n} 项的和为: {result}")
