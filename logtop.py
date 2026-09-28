import argparse
from collections import Counter

def read_column(path, col):
    """读出日志里每行的第 col 列，返回一个列表"""
    items = []
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                fields = line.split()
                if len(fields) > col:
                    items.append(fields[col])
    except FileNotFoundError:
        print(f"错误: 文件 {path} 不存在")
    return items

def main():
    parser = argparse.ArgumentParser(description="统计日志 Top IP/路径")
    parser.add_argument("file", help="日志文件路径")
    parser.add_argument("--top", type=int, default=10, help="显示前几个 (默认 10)")
    parser.add_argument("--mode", choices=["ip", "path"], default="ip",
                        help="统计 IP 还是路径 (默认 ip)")
    args = parser.parse_args()

    col = 0 if args.mode == "ip" else 2
    items = read_column(args.file, col)
    for name, n in Counter(items).most_common(args.top):
        print(n, name)

if __name__ == "__main__":
    main()
