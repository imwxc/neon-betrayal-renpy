## 游戏配置选项 - Demo 版本
## 使用默认字体，不依赖外部资源

init python:
    # 游戏元数据
    build.name = "neon-betrayal"
    build.version = "1.0.0"
    
    # 窗口配置 (使用英文标题避免方块)
    config.name = "Neon Betrayal"
    config.version = "1.0.0"
    
    # 屏幕尺寸 - 使用较小的窗口以便测试
    config.screen_width = 1280
    config.screen_height = 720
    
    # 禁用全屏（方便测试）
    config.default_fullscreen = False
    
    # 文本显示速度
    config.default_text_cps = 40
    
    # 禁用自动阅读
    config.default_afm_enable = False
    
    # 存档配置
    config.has_autosave = True
    config.autosave_slots = 6
    config.has_quicksave = True
    config.quicksave_slots = 6
    
    # 启用 rollback
    config.rollback_enabled = True

    # 跳过配置
    config.allow_skipping = True

    # 使用支持中文的字体 (思源黑体)
    style.default.font = "SourceHanSansLite.ttf"
    style.default.size = 24

## 游戏启动配置
define gui.show_name = True
define gui.about = _("""
霓虹背叛 (Neon Betrayal)

一款赛博朋克风格的视觉小说游戏。

玩家扮演陈子明，一位从巨型生物科技公司「奇美拉生物」
叛逃的前高管，在逃亡过程中遭遇三位关键角色。

开发团队：Neon Betrayal Team
""")

## 主菜单配置 - 使用纯色背景
define gui.main_menu_background = "#000000"
define gui.game_menu_background = "#1a1a2e"

## 对话框配置
define gui.textbox_height = 200
define gui.textbox_yalign = 1.0

## 选择菜单配置
define gui.choice_spacing = 16
define gui.choice_button_width = 600
define gui.choice_button_height = 50
