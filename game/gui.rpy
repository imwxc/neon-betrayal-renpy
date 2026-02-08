## GUI 自定义 - Demo 版本
## 使用默认样式，不依赖外部资源

init python:
    # 赛博朋克配色方案
    gui.accent_color = '#00d4ff'  # 青色霓虹
    gui.idle_color = '#1a1a2e'    # 深蓝黑
    gui.hover_color = '#00d4ff'   # 青色
    gui.selected_color = '#ff0080' # 霓虹粉
    gui.insensitive_color = '#444444' # 灰色
    
    # 文本颜色
    gui.text_color = '#ffffff'
    gui.idle_text_color = '#aaaaaa'
    gui.hover_text_color = '#00d4ff'
    gui.selected_text_color = '#ff0080'
    
    # 界面背景
    gui.muted_color = '#1a1a2e'
    gui.hover_muted_color = '#2a2a4e'
    
    # 文本框样式 - 使用纯色背景
    gui.textbox_background = Solid("#000000cc")
    
    # 按钮样式 - 使用默认
    gui.button_background = None
    gui.button_text_font = "SourceHanSansLite.ttf"
    gui.button_text_size = 24
    
    # 快速菜单
    gui.quick_button_text_font = "SourceHanSansLite.ttf"
    gui.quick_button_text_size = 18

## 样式定义 - 使用支持中文的字体
style default:
    font "SourceHanSansLite.ttf"
    size 24
    color gui.text_color

style say_label:
    font "SourceHanSansLite.ttf"
    size 28
    bold True
    color gui.accent_color

style say_dialogue:
    font "SourceHanSansLite.ttf"
    size 24
    color gui.text_color

style choice_button:
    background Solid("#1a1a2e")
    hover_background Solid("#2a2a4e")
    padding (20, 10)

style choice_button_text:
    font "SourceHanSansLite.ttf"
    size 22
    color gui.idle_text_color
    hover_color gui.hover_color

## 赛博朋克特效样式
style glitch_text:
    properties gui.text_properties("glitch")
    
style neon_text:
    color '#00d4ff'
    outlines [ (2, '#00d4ff40', 0, 0), (4, '#00d4ff20', 0, 0) ]

## 主菜单样式 - 使用纯色背景
style main_menu_frame:
    background Solid("#000000")

style main_menu_text:
    font "SourceHanSansLite.ttf"
    size 48
    color '#00d4ff'
    outlines [ (2, '#00d4ff60', 0, 0), (4, '#00d4ff30', 0, 0) ]

## 游戏菜单样式
style game_menu_outer_frame:
    background Solid("#1a1a2e")

style game_menu_navigation_frame:
    background None

style game_menu_content_frame:
    background None

style game_menu_viewport:
    xsize 800
    ysize 500

## 存档/读档界面
style slot:
    background Solid("#2a2a4e")
    hover_background Solid("#3a3a5e")
    padding (10, 10)

style slot_time_text:
    font "SourceHanSansLite.ttf"
    size 16
    color '#aaaaaa'

style slot_name_text:
    font "SourceHanSansLite.ttf"
    size 18
    color '#ffffff'
