#!/usr/bin/env python3
"""学习打卡小工具。

用法：
    python3 hello.py 今天复习了链表反转

每执行一次，就往 study-log.md 追加一条记录。
改完文件后 git commit + git push，你就能在 GitHub 上看到修改历史了
—— 这就是「版本管理」最直观的样子。
"""

import datetime
import pathlib
import sys

LOG = pathlib.Path(__file__).parent / "study-log.md"


def main():
    text = " ".join(sys.argv[1:]).strip()

    if not text:
        print("还没输入内容。用法示例：")
        print("    python3 hello.py 复习了链表反转")
        return

    today = datetime.date.today().isoformat()
    line = "- {}：{}\n".format(today, text)

    if not LOG.exists():
        LOG.write_text("# 学习打卡记录\n\n", encoding="utf-8")

    with LOG.open("a", encoding="utf-8") as f:
        f.write(line)

    print("已记录 ->", line.strip())


if __name__ == "__main__":
    main()
