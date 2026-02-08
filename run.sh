#!/bin/bash
# 运行霓虹背叛 Demo 的脚本

cd "$(dirname "$0")"
RENPYSH="/home/imwxc/renpy-sdk/renpy-8.3.4-sdk/renpy.sh"

if [ ! -f "$RENPYSH" ]; then
    echo "错误：找不到 Ren'Py SDK。请确保已正确安装 SDK。"
    echo "SDK 路径：$RENPYSH"
    exit 1
fi

echo "启动 霓虹背叛 (Neon Betrayal)..."
"$RENPYSH" . "$@"
