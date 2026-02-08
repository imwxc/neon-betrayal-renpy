## 资源文件说明

### 图像资源

#### 角色立绘 (game/images/characters/)

将立绘图片转换为 WebP 或 PNG 格式，命名如下：

**陈子明 (主角)**

- chen_ziming.webp - 默认表情
- chen_ziming_tired.webp - 疲惫
- chen_ziming_wary.webp - 警惕

**荻原苍介**

- akihara.webp - 默认
- akihara_cold.webp - 冷淡
- akihara_conflicted.webp - 矛盾
- akihara_gentle.webp - 温柔

**克雷吉**

- craig.webp - 默认
- craig_smile.webp - 微笑
- craig_serious.webp - 严肃

**珀西**

- percy.webp - 默认
- percy_smile.webp - 微笑
- percy_calm.webp - 平静
- percy_confused.webp - 困惑

#### 背景图 (game/images/backgrounds/)

- company_hq_outside_rain.webp - 公司总部外（雨）
- rainy_hq_outside.webp - 雨夜总部外
- under_bridge_rain.webp - 雨夜桥下
- temporary_hideout.webp - 临时落脚点
- safehouse_interior.webp - 安全屋内
- safehouse_interior_night.webp - 安全屋内（夜晚）

#### GUI 资源 (game/gui/)

需要创建以下图片资源：

- main_menu.png - 主菜单背景 (1920x1080)
- game_menu.png - 游戏菜单背景
- textbox.png - 文本框背景
- textbox_white.png - 陈子明专用文本框
- textbox_cyan.png - 荻原苍介专用文本框
- textbox_orange.png - 克雷吉专用文本框
- textbox_purple.png - 珀西专用文本框
- button.png - 按钮背景
- button_hover.png - 按钮悬停背景
- button_choice.png - 选择按钮
- button_choice_hover.png - 选择按钮悬停
- slot.png - 存档位
- slot_hover.png - 存档位悬停
- frame.png - 通用框架
- window_icon.png - 窗口图标

### 音频资源

#### 背景音乐 (game/audio/bgm/)

转换为 OGG 格式：

- cyberpunk_ambient.ogg
- tension.ogg
- tension_low.ogg
- glitch_ambient.ogg
- safehouse_hum.ogg
- theme_music.ogg

#### 音效 (game/audio/sfx/)

转换为 OGG 格式：

- rain_ambient.ogg
- alarm_distant.ogg
- rain_close.ogg
- breathing_heavy.ogg
- rain_heavy.ogg
- footsteps_boots.ogg
- vehicle_brake.ogg
- door_unlock.ogg
- door_lock.ogg
- electric_hum.ogg
- communicator_vibrate.ogg
- channel_static.ogg
- rain_window.ogg
- city_rumble_distant.ogg
- breathing_rapid.ogg
- impact_soft.ogg

### 字体资源 (game/fonts/)

- NotoSansSC-Regular.otf - 常规字体
- NotoSansSC-Bold.otf - 粗体

### 从原项目迁移资源

原项目位于 `/home/imwxc/Documents/neon-betrayal/`，资源路径：

- 角色立绘: `assets/characters/**/*.svg`
- 背景图: `assets/backgrounds/*.svg`
- CG: `assets/cg/*.svg`
- 音效: `assets/sfx/*.mp3`

**注意**: SVG 需要转换为 PNG/WebP 格式才能被 Ren'Py 使用。
