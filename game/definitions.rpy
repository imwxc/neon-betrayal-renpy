## 角色定义 - Demo 版本
## 使用默认文本框，不依赖外部图片资源

# 主角 - 陈子明（玩家视角，旁白）
define narrator = Character(what_color="#cccccc", what_size=24)

# 陈子明（内心独白显示为白色）
define chen_ziming = Character("陈子明", color="#ffffff")

# 荻原苍介 - 曾经的导师，现追捕者（青色霓虹）
define akihara = Character("荻原苍介", color="#00d4ff")

# 克雷吉·塞西尔 - 竞争对手（橙红色）
define craig = Character("克雷吉", color="#ff6b35")

# 珀西·杨 - 谈判专家（紫色）
define percy = Character("珀西", color="#9b59b6")

# 联络人 - 暗流组织（灰色，神秘感）
define contact = Character("联络人", color="#888888")

## 立绘定义 - 使用纯色占位
# 陈子明
image chen_ziming = Solid("#ffffff20")
image chen_ziming tired = Solid("#cccccc20")
image chen_ziming wary = Solid("#aaaaaa20")

# 荻原苍介
image akihara = Solid("#00d4ff20")
image akihara cold = Solid("#0088aa20")
image akihara conflicted = Solid("#00668820")
image akihara gentle = Solid("#44ddff20")

# 克雷吉
image craig = Solid("#ff6b3520")
image craig smile = Solid("#ff884420")
image craig serious = Solid("#cc552220")

# 珀西
image percy = Solid("#9b59b620")
image percy smile = Solid("#bb79d620")
image percy calm = Solid("#7b399620")
image percy confused = Solid("#5b298620")

## 背景定义 - 使用纯色
image bg company_hq_outside_rain = Solid("#1a1a2e")
image bg rainy_hq_outside = Solid("#16213e")
image bg under_bridge_rain = Solid("#0f3460")
image bg temporary_hideout = Solid("#2c3e50")
image bg safehouse_interior = Solid("#34495e")
image bg safehouse_interior_night = Solid("#2c3e50")

# 简化背景别名
image black = Solid("#000000")
image gray = Solid("#333333")
image white = Solid("#ffffff")

## 音频定义 - Demo 版本不加载实际音频
## 注释掉音频定义以避免错误
