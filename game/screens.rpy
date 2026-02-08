## 完整屏幕定义

screen main_menu():
    tag menu
    
    add Solid("#0a0a1a")
    
    frame:
        xalign 0.5
        yalign 0.5
        background None
        
        vbox:
            spacing 40
            xalign 0.5
            
            text "霓虹背叛":
                xalign 0.5
                font "SourceHanSansLite.ttf"
                size 72
                color '#00d4ff'
            
            vbox:
                spacing 15
                xalign 0.5
                
                button:
                    action Start()
                    xsize 250
                    ysize 50
                    text "开始游戏":
                        xalign 0.5
                        yalign 0.5
                        font "SourceHanSansLite.ttf"
                        size 24
                        color '#ffffff'
                    background Solid("#1a1a2e")
                    hover_background Solid("#00d4ff")
                
                button:
                    action ShowMenu("load")
                    xsize 250
                    ysize 50
                    text "读取存档":
                        xalign 0.5
                        yalign 0.5
                        font "SourceHanSansLite.ttf"
                        size 24
                        color '#ffffff'
                    background Solid("#1a1a2e")
                    hover_background Solid("#00d4ff")
                
                button:
                    action ShowMenu("preferences")
                    xsize 250
                    ysize 50
                    text "设置":
                        xalign 0.5
                        yalign 0.5
                        font "SourceHanSansLite.ttf"
                        size 24
                        color '#ffffff'
                    background Solid("#1a1a2e")
                    hover_background Solid("#00d4ff")
                
                button:
                    action Quit(confirm=False)
                    xsize 250
                    ysize 50
                    text "退出":
                        xalign 0.5
                        yalign 0.5
                        font "SourceHanSansLite.ttf"
                        size 24
                        color '#ffffff'
                    background Solid("#1a1a2e")
                    hover_background Solid("#ff0080")

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        xalign 0.5
        yalign 1.0
        xfill True
        ysize 200
        background Solid("#000000cc")
        padding (40, 20)

        has vbox:
            spacing 10

        if who is not None:
            text who id "who":
                font "SourceHanSansLite.ttf"
                size 28
                bold True
                color '#00d4ff'

        text what id "what":
            font "SourceHanSansLite.ttf"
            size 24
            color '#ffffff'

screen choice(items):
    style_prefix "choice"

    # 隐藏对话框，让选择菜单占据全屏
    window:
        background None

    vbox:
        xalign 0.5
        yalign 0.5  # 垂直居中
        spacing 20

        for i in items:
            button:
                action i.action
                xsize 700
                ysize 60

                frame:
                    background Solid("#1a1a2e")
                    hover_background Solid("#2a2a4e")
                    padding (20, 10)
                    xfill True
                    yfill True

                    text i.caption:
                        xalign 0.5
                        yalign 0.5
                        font "SourceHanSansLite.ttf"
                        color '#cccccc'
                        hover_color '#00d4ff'
                        size 24

## 游戏菜单（读取存档、设置等）
screen game_menu(title, scroll=None, yinitial=0.0):
    tag menu

    add Solid("#1a1a2e")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 600
        background Solid("#0a0a1a")
        padding (20, 20)

        vbox:
            spacing 20
            xfill True
            yfill True

            hbox:
                spacing 20
                xfill True

                text title:
                    font "SourceHanSansLite.ttf"
                    size 36
                    color '#00d4ff'

                null width 20

                button:
                    action Return()
                    xsize 100
                    ysize 40
                    text "返回":
                        xalign 0.5
                        yalign 0.5
                        font "SourceHanSansLite.ttf"
                        size 18
                        color '#ffffff'
                    background Solid("#2a2a4e")
                    hover_background Solid("#00d4ff")

            null height 20

            transclude

## 读取存档界面
screen load():
    tag menu
    use game_menu("读取存档"):
        grid 3 2:
            spacing 20
            xalign 0.5
            yalign 0.5

            for i in range(6):
                button:
                    action FileLoad(i)
                    xsize 280
                    ysize 180
                    background Solid("#2a2a4e")
                    hover_background Solid("#3a3a5e")

                    vbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 10

                        text "存档 [i]":
                            xalign 0.5
                            font "SourceHanSansLite.ttf"
                            size 20
                            color '#ffffff'

                        if FileLoadable(i):
                            text FileTime(i, format="%Y-%m-%d %H:%M"):
                                xalign 0.5
                                font "SourceHanSansLite.ttf"
                                size 14
                                color '#aaaaaa'

## 保存界面
screen save():
    tag menu
    use game_menu("保存游戏"):
        grid 3 2:
            spacing 20
            xalign 0.5
            yalign 0.5

            for i in range(6):
                button:
                    action FileSave(i)
                    xsize 280
                    ysize 180
                    background Solid("#2a2a4e")
                    hover_background Solid("#3a3a5e")

                    vbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 10

                        text "存档 [i]":
                            xalign 0.5
                            font "SourceHanSansLite.ttf"
                            size 20
                            color '#ffffff'

                        if FileLoadable(i):
                            text FileTime(i, format="%Y-%m-%d %H:%M"):
                                xalign 0.5
                                font "SourceHanSansLite.ttf"
                                size 14
                                color '#aaaaaa'

## 设置界面
screen preferences():
    tag menu
    use game_menu("设置"):
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5

            hbox:
                spacing 20
                text "显示模式：":
                    font "SourceHanSansLite.ttf"
                    size 24
                    color '#ffffff'

                button:
                    action Preference("display", "window")
                    xsize 150
                    ysize 40
                    text "窗口":
                        xalign 0.5
                        yalign 0.5
                        font "SourceHanSansLite.ttf"
                        size 18
                        color '#ffffff'
                    background Solid("#2a2a4e")
                    hover_background Solid("#00d4ff")

                button:
                    action Preference("display", "fullscreen")
                    xsize 150
                    ysize 40
                    text "全屏":
                        xalign 0.5
                        yalign 0.5
                        font "SourceHanSansLite.ttf"
                        size 18
                        color '#ffffff'
                    background Solid("#2a2a4e")
                    hover_background Solid("#00d4ff")

            hbox:
                spacing 20
                text "文本速度：":
                    font "SourceHanSansLite.ttf"
                    size 24
                    color '#ffffff'

                button:
                    action Preference("text speed", 0)
                    xsize 80
                    ysize 40
                    text "快":
                        xalign 0.5
                        yalign 0.5
                        font "SourceHanSansLite.ttf"
                        size 18
                        color '#ffffff'
                    background Solid("#2a2a4e")
                    hover_background Solid("#00d4ff")

                button:
                    action Preference("text speed", 40)
                    xsize 80
                    ysize 40
                    text "中":
                        xalign 0.5
                        yalign 0.5
                        font "SourceHanSansLite.ttf"
                        size 18
                        color '#ffffff'
                    background Solid("#2a2a4e")
                    hover_background Solid("#00d4ff")

                button:
                    action Preference("text speed", 80)
                    xsize 80
                    ysize 40
                    text "慢":
                        xalign 0.5
                        yalign 0.5
                        font "SourceHanSansLite.ttf"
                        size 18
                        color '#ffffff'
                    background Solid("#2a2a4e")
                    hover_background Solid("#00d4ff")

## 快速菜单（游戏内菜单按钮）
screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 0.98
            spacing 20

            button:
                action Rollback()
                text "回退":
                    font "SourceHanSansLite.ttf"
                    size 16
                    color '#ffffff'
                background Solid("#2a2a4e")
                hover_background Solid("#00d4ff")

            button:
                action ShowMenu('save')
                text "保存":
                    font "SourceHanSansLite.ttf"
                    size 16
                    color '#ffffff'
                background Solid("#2a2a4e")
                hover_background Solid("#00d4ff")

            button:
                action ShowMenu('load')
                text "读取":
                    font "SourceHanSansLite.ttf"
                    size 16
                    color '#ffffff'
                background Solid("#2a2a4e")
                hover_background Solid("#00d4ff")

            button:
                action ShowMenu('preferences')
                text "设置":
                    font "SourceHanSansLite.ttf"
                    size 16
                    color '#ffffff'
                background Solid("#2a2a4e")
                hover_background Solid("#00d4ff")

            button:
                action MainMenu()
                text "主菜单":
                    font "SourceHanSansLite.ttf"
                    size 16
                    color '#ffffff'
                background Solid("#2a2a4e")
                hover_background Solid("#ff0080")

## 确认对话框 - 修复退出错误
screen confirm(message, yes_action, no_action):
    modal True
    
    add Solid("#000000cc")
    
    frame:
        xalign 0.5
        yalign 0.5
        background Solid("#1a1a2e")
        padding (40, 40)
        
        vbox:
            spacing 30
            xalign 0.5
            
            text message:
                xalign 0.5
                font "SourceHanSansLite.ttf"
                size 24
                color '#ffffff'
            
            hbox:
                spacing 30
                xalign 0.5
                
                button:
                    action yes_action
                    xsize 100
                    ysize 40
                    text "是":
                        xalign 0.5
                        yalign 0.5
                        font "SourceHanSansLite.ttf"
                        size 20
                        color '#ffffff'
                    background Solid("#2a2a4e")
                    hover_background Solid("#00d4ff")
                
                button:
                    action no_action
                    xsize 100
                    ysize 40
                    text "否":
                        xalign 0.5
                        yalign 0.5
                        font "SourceHanSansLite.ttf"
                        size 20
                        color '#ffffff'
                    background Solid("#2a2a4e")
                    hover_background Solid("#ff0080")

## 记忆卡片通知系统
screen memory_card(memory_title, memory_desc):
    zorder 100
    style_prefix "memory_card"

    # 5秒后自动隐藏
    timer 5.0 action Hide('memory_card')

    frame at memory_card_slide:
        xsize 450
        ysize 200
        background Solid("#1a1a2ecc")
        padding (20, 20)

        hbox:
            spacing 15

            # 记忆图标
            frame:
                xsize 80
                ysize 80
                background Solid("#00d4ff40")
                xalign 0.5
                yalign 0.5

                text "🧠":
                    xalign 0.5
                    yalign 0.5
                    size 40

            # 记忆内容
            vbox:
                spacing 8
                yalign 0.5

                text "获得记忆":
                    size 16
                    color "#00d4ff"
                    font "SourceHanSansLite.ttf"

                text memory_title:
                    size 24
                    color "#ffffff"
                    bold True
                    font "SourceHanSansLite.ttf"

                text memory_desc:
                    size 14
                    color "#aaaaaa"
                    font "SourceHanSansLite.ttf"

# 记忆卡片动画
transform memory_card_slide:
    xalign 0.5
    yalign 0.0
    yoffset -250
    alpha 0

    on show:
        parallel:
            easeout_back 0.5 yoffset 80
        parallel:
            linear 0.3 alpha 1.0

    on hide:
        parallel:
            easein 0.3 yoffset -250
        parallel:
            linear 0.2 alpha 0

## 记忆收集画廊
screen memory_gallery():
    tag menu

    add Solid("#0a0a1a")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 600
        background Solid("#1a1a2e")
        padding (30, 30)

        vbox:
            spacing 20
            xfill True
            yfill True

            # 标题
            text "记忆收集":
                xalign 0.5
                font "SourceHanSansLite.ttf"
                size 36
                color '#00d4ff'

            null height 10

            # 记忆网格
            grid 3 3:
                spacing 15
                xalign 0.5
                yalign 0.5

                for memory_id, memory in memories.items():
                    button:
                        action NullAction()
                        xsize 300
                        ysize 120

                        if memory_id in persistent.collected_memories:
                            background Solid("#2a2a4e")
                            hover_background Solid("#3a3a5e")

                            hbox:
                                spacing 10
                                xfill True
                                yfill True

                                frame:
                                    xsize 60
                                    ysize 60
                                    background Solid("#00d4ff20")
                                    xalign 0.5
                                    yalign 0.5

                                    text "🧠":
                                        xalign 0.5
                                        yalign 0.5
                                        size 30

                                vbox:
                                    spacing 5
                                    yalign 0.5

                                    text memory["title"]:
                                        font "SourceHanSansLite.ttf"
                                        size 18
                                        color '#ffffff'
                                        bold True

                                    text memory["brief"]:
                                        font "SourceHanSansLite.ttf"
                                        size 12
                                        color '#aaaaaa'
                        else:
                            background Solid("#1a1a2e")

                            text "???":
                                xalign 0.5
                                yalign 0.5
                                font "SourceHanSansLite.ttf"
                                size 24
                                color '#555555'

            # 返回按钮
            button:
                action Return()
                xsize 120
                ysize 40
                xalign 0.95
                yalign 0.95

                text "返回":
                    xalign 0.5
                    yalign 0.5
                    font "SourceHanSansLite.ttf"
                    size 18
                    color '#ffffff'
                background Solid("#2a2a4e")
                hover_background Solid("#00d4ff")
