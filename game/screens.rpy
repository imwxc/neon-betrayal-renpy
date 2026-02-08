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
        
        has vbox:
            spacing 10
        
        if who is not None:
            text who id "who"
        
        text what id "what"

screen choice(items):
    style_prefix "choice"
    
    vbox:
        xalign 0.5
        yalign 0.75
        spacing 16
        
        for i in items:
            button:
                action i.action
                xsize 600
                ysize 50
                
                frame:
                    background Solid("#1a1a2e")
                    hover_background Solid("#2a2a4e")
                    padding (20, 10)
                    xfill True
                    yfill True
                    
                    text i.caption:
                        xalign 0.5
                        yalign 0.5
                        color '#cccccc'
                        hover_color '#00d4ff'
                        size 22

## 确认对话框 - 修复退出错误
screen yesno_prompt(message, yes_action, no_action):
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
