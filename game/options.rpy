## 游戏配置选项 - Demo 版本
## 使用默认字体，不依赖外部资源

## 初始化 GUI（必须在其他配置之前）
init offset = -2
init python:
    gui.init(1280, 720)

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

    # 启动时显示主菜单（而不是直接进入游戏）
    config.main_menu_music = None

    # 禁用自动加载最后存档
    config.autoreload = False

    # 使用 FontGroup 配置字体
    # 顺序很重要：先添加的字体优先级更高
    # 0x0020-0x007f: 基本拉丁字母 (英文/数字)
    # 0x0370-0x03ff: 希腊字母
    # 0x4e00-0x9fff: 中日韩统一表意文字 (中文)
    style.default.font = FontGroup()\
        .add("DejaVuSans.ttf", 0x0020, 0x007f)\
        .add("DejaVuSans.ttf", 0x0370, 0x03ff)\
        .add("SourceHanSansLite.ttf", 0x4e00, 0x9fff)\
        .add("SourceHanSansLite.ttf", 0x3000, 0x303f)\
        .add("SourceHanSansLite.ttf", 0xff00, 0xffef)
    style.default.size = 24

    # 注册字体别名，方便在文本中使用
    config.font_name_map["chinese"] = "SourceHanSansLite.ttf"
    config.font_name_map["english"] = "DejaVuSans.ttf"

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
