# 霓虹背叛 (Neon Betrayal)

一款赛博朋克风格的视觉小说游戏，使用 Ren'Py 引擎开发。

## 游戏简介

玩家扮演陈子明，一位从巨型生物科技公司「奇美拉生物」叛逃的前高管，在逃亡过程中遭遇三位关键角色——曾经的导师荻原苍介、竞争对手克雷吉·塞西尔、前恋人珀西·杨。

## 技术栈

- **引擎**: Ren'Py 8.x
- **语言**: Python 3 + Ren'Py 脚本
- **资源**: PNG 图像、OGG 音频

## 项目结构

```
neon-betrayal-renpy/
├── game/
│   ├── scripts/          # 剧本文件
│   │   ├── episode1.rpy  # 第一章
│   │   └── choices.rpy   # 选择分支
│   ├── images/
│   │   ├── characters/   # 角色立绘
│   │   └── backgrounds/  # 背景图
│   ├── audio/
│   │   ├── bgm/          # 背景音乐
│   │   └── sfx/          # 音效
│   ├── gui/              # GUI 自定义
│   ├── options.rpy       # 游戏配置
│   ├── screens.rpy       # 界面定义
│   └── script.rpy        # 主入口
├── README.md
└── project.json          # Ren'Py 项目配置
```

## 开发说明

1. 安装 Ren'Py SDK
2. 将项目放入 Ren'Py 项目目录
3. 使用 Ren'Py Launcher 启动

## 角色

- **陈子明** (主角) - 叛逃的前高管
- **荻原苍介** - 曾经的导师，现追捕者
- **克雷吉·塞西尔** - 竞争对手「新视界」高管
- **珀西·杨** - 公司派来的「谈判专家」

## 许可

MIT License
