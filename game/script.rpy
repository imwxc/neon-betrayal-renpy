## 霓虹背叛 - 第一幕：背叛之夜
## 基于 episode1_act1 剧本

# 角色定义
init python:
    # 主角
    chen_ziming = Character("陈子明", color="#ffffff")
    # 7号 - 荻原苍介
    akihara = Character("7号", color="#00d4ff")
    # 克雷吉
    craig = Character("克雷吉", color="#ff6b35")
    # 珀西
    percy = Character("珀西", color="#9b59b6")
    # 联络人
    contact = Character("联络人", color="#888888")
    # 旁白
    narrator = Character(what_color="#cccccc")

# 游戏开始 - 第一幕
label start:
    # 初始化变量
    $ akihara_affection = 0
    $ craig_affection = 0
    $ percy_affection = 0
    $ current_route = None
    
    scene black with fade
    
    # ====== 场景0：开场旁白 ======
    "雨水沿着霓虹灯牌的边缘滴落，像一串失真的倒计时。"
    
    "我从「奇美拉生物」总部跑出来时，警报还没响彻整座城市。"
    
    "数据芯片贴在掌心，温度像一枚烧红的罪证。"
    
    "我应该很清楚自己为什么要叛逃。"
    
    "可当我试图回想，脑子里只有几帧断裂的画面——白光、玻璃、呼吸面罩，还有一个陌生的代号在耳边回响。"
    
    "[获得记忆：断裂的过去]"
    "记忆的缝隙中，那句'编号 Ω，开始记录'像个不散的回声。我忘记了什么？还是...我被植入了什么？"
    
    # ====== 场景1：雨夜出逃 ======
    scene bg rainy_hq_outside with fade
    
    chen_ziming "……还没追上来。"
    
    chen_ziming "先躲进巷口。"
    
    "我抬手按住左太阳穴的接口疤痕，那里像有细小的电流在爬。"
    
    "视野边缘浮起轻微噪点——植入体在提醒我：你状态不稳定。"
    
    "会议室的玻璃反光里，有人站在我身后。"
    
    "我想回头，却像被按住了脖子。"
    
    "有人说：'编号 Ω，开始记录。'"
    
    "我贴在潮湿的墙边，广告牌的光把我的影子切成几段。"
    
    chen_ziming "我到底……忘了什么？"
    
    "我握紧芯片，逼自己不要再想那句'编号 Ω'。"
    
    "[获得记忆：闪回的疑虑]"
    "那个编号……它属于谁？是我，还是另一个人的过去？"
    
    # ====== 场景2：桥下拦截 ======
    scene bg under_bridge_rain with fade
    
    "还是被追上了。"
    
    chen_ziming "居然……是他。"
    
    "雨幕里走出一个人，像从我的过去里剪出来的阴影。"
    
    show akihara at right with dissolve
    
    akihara "把芯片交出来。"
    
    akihara "跟我回去。"
    
    chen_ziming "你挡我一次可以。挡我一辈子不行。"
    
    akihara "……子明。别把自己逼到死路。"
    
    # 第一个重大选择
    menu:
        "[选择]"
        
        "'跟我一起走。'（尝试说服他）":
            $ akihara_affection += 10
            $ current_route = "akihara"
            jump scene2A
            
        "'让开。'（趁机逃跑，必要时伤他）":
            $ akihara_affection -= 5
            jump scene2B
            
        "'我在等一个人。'（拖时间等接应）":
            $ craig_affection += 5
            $ current_route = "craig"
            jump scene2C

# ====== 2A：荻原苍介分支-短暂同行 ======
label scene2A:
    scene bg under_bridge_rain with fade
    
    "我们并肩走在狭窄通道里，雨声被隔在外面，脚步声反而刺耳。"
    
    akihara "你以为这是叛逃？"
    
    akihara "你连自己在做什么都未必记得清。"
    
    chen_ziming "少来这一套。你只要回答我——你会不会开枪？"
    
    akihara "……我会把你带回去。活着。"
    
    "[获得记忆：收养]"
    "他说要带我回去……活着。我们之间曾经有过什么？那个'活着'，是承诺还是任务？"
    
    chen_ziming "我也不确定自己为什么非逃不可。"
    
    "正打算吐露心声，追兵已经到了身后。"
    
    "7号深深看了我一眼。"
    
    akihara "子明，往前走，别回头。我把他们处理掉再来找你。"
    
    jump scene3

# ====== 2B：桥下脱身 ======
label scene2B:
    scene bg under_bridge_rain with fade
    
    "我从他身侧擦过去，动作快得像反射。"
    
    "下一秒，我听见闷响——像某种关系被折断。"
    
    chen_ziming "……别追。"
    
    "植入体噪声突然变大，霓虹边缘出现重影，我差点摔倒。"
    
    "那一声闷响，不只是身体的碰撞。像是有什么东西，永远地断裂了。"
    
    jump scene3

# ====== 2C：克雷吉分支-前来接应 ======
label scene2C:
    scene bg under_bridge_rain with fade
    
    "一辆黑色轿车停在巷口，车窗滑下。"
    
    show craig at center with dissolve
    
    craig "上车。"
    
    craig "别让我白跑一趟。"
    
    chen_ziming "你想要什么？"
    
    craig "先活下来，再谈价。"
    
    "[获得记忆：宿敌]"
    "克雷吉·塞西尔——竞争对手「新视界」公司高管。他为什么会在那里等着我？救我，害我，还是想要我手里奇美拉的机密芯片？"
    
    "正打算质询，追兵已经到了身后。"
    
    craig "车辆目标太大。"
    
    craig "你在隐蔽处跳车，我把他们处理掉再来找你。"
    
    craig "别想跑掉，陈子明。我总能找到你。"
    
    jump scene3

# ====== 场景3：暗流联络 ======
label scene3:
    scene bg temporary_hideout with fade
    
    "逃到临时落脚点，门锁合上那一刻，我才意识到自己一直在抖。"
    
    chen_ziming "该看了。到底值不值得我把命押上。"
    
    "芯片接入接口，视野边缘的噪点像潮水涌上来，色彩被拉开、重叠。"
    
    "标题跳出来——《城市级记忆干预计划》。"
    
    chen_ziming "……他们在改写市民的记忆。"
    
    "[获得记忆：机密文件·记忆干预计划]"
    "奇美拉生物公司不仅在制造义体，还在制造'真相'。他们有能力重写整个城市的记忆……包括我的？"
    
    "突然，通讯器震动，一个陌生频道自动接入，像早就等在这里。"
    
    contact "我们知道你拿到了什么。"
    
    contact "想活下来，按我说的路线走。"
    
    chen_ziming "暗流？你们怎么知道我在这？"
    
    contact "别问。只管走。"
    
    "[获得记忆：暗流的邀请]"
    "'暗流'——反企业抵抗组织。他们一直在监视奇美拉的一举一动。为什么是我？因为芯片，还是因为……我是'Ω'？"
    
    "公司的敌人，姑且算是我的朋友。"
    
    "我按对方指示行动，很快找到了前行的方向。"
    
    # ====== 场景4：安全屋 ======
    scene bg safehouse_interior with fade
    
    "安全屋很干净，干净得不像逃亡者该有的落脚点。"
    
    "我刚把呼吸压稳，手机就响了。"
    
    contact "需要我帮你联络同伴吗？"
    
    # 第二个重大选择
    menu:
        "[选择]"
        
        "'联络7号。'" if akihara_affection > 0:
            $ akihara_affection += 10
            jump scene4A
            
        "'我谁也信不过。'":
            jump scene4B
            
        "'联络克雷吉。'" if craig_affection > 0:
            $ craig_affection += 10
            jump scene4C

# ====== 4A：荻原苍介分支-安全屋 ======
label scene4A:
    scene bg safehouse_interior with fade
    
    show akihara at right with dissolve
    
    akihara "你躲不久的。"
    
    akihara "如果你要死，也得死在我看得见的地方。"
    
    chen_ziming "……是你的话，我接受。"
    
    "今晚，就暂时信任荻原苍介。"
    
    jump scene5

# ====== 4B：珀西分支-安全屋 ======
label scene4B:
    scene bg safehouse_interior with fade
    
    "我无法相信任何人，不是没有原因的。"
    
    "我回想着，头开始剧烈疼痛，想要呕吐。"
    
    "[获得记忆：前任恋人]"
    "我的恋人，竟然是个仿生人，恋慕更无从谈起……我居然被欺骗了整整三年。"
    
    "令人意想不到的是，他居然出现在了安全屋。"
    
    show percy at center with dissolve
    
    chen_ziming "珀西？你怎么可能知道我在这？"
    
    percy "我不是来抓你的。"
    
    percy "我是来和你谈谈——像我们以前那样。"
    
    "他看上去太镇定了，镇定得不像'谈判专家'，更像提前写好的答案。"
    
    $ percy_affection += 10
    $ current_route = "percy"
    
    "今晚，就暂时信任珀西·杨。"
    
    jump scene5

# ====== 4C：克雷吉分支-安全屋 ======
label scene4C:
    scene bg safehouse_interior with fade
    
    show craig at left with dissolve
    
    craig "我不喜欢欠人情，也不喜欢别人欠我。"
    
    craig "既然你选择了我，那么代价想必你也明白，对吧？"
    
    chen_ziming "……是的。"
    
    "今晚，就暂时信任克雷吉·塞西尔。"
    
    jump scene5

# ====== 场景5：尾声 ======
label scene5:
    scene bg safehouse_interior_night with fade
    
    "雨还在下。"
    
    "我忽然意识到——今晚我选的不只是同伴。也是活法。"
    
    "第一夜结束了。"
    
    "明天，追捕会继续。选择会变得更难。"
    
    "但至少今晚，我活下来了。"
    
    "[获得记忆：第一夜]"
    "逃离奇美拉，在雨夜中躲避追捕。那个叫'7号'的男人追上了我，死对头克雷吉出现，前恋人兼谈判专家珀西也找上门来。我拿着关于'记忆干预计划'的芯片，在这个充满霓虹与背叛的城市里，做出了第一个选择。"
    
    scene black with fade
    
    "【第一幕·完】"
    "【即将进入第二幕：信任的代价】"
    
    return
