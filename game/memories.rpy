## 记忆系统定义
## 存储所有可收集的记忆

# 定义所有记忆数据
define memories = {
    "memory_01": {
        "title": "断裂的过去",
        "brief": "关于编号的疑问",
        "desc": "记忆的缝隙中，那句'编号 Omega，开始记录'像个不散的回声。我忘记了什么？还是...我被植入了什么？"
    },
    "memory_02": {
        "title": "闪回的疑虑",
        "brief": "那个编号属于谁？",
        "desc": "那个编号……它属于谁？是我，还是另一个人的过去？"
    },
    "memory_03": {
        "title": "收养",
        "brief": "荻原苍介的承诺",
        "desc": "他说要带我回去……活着。我们之间曾经有过什么？那个'活着'，是承诺还是任务？"
    },
    "memory_04": {
        "title": "宿敌",
        "brief": "克雷吉·塞西尔",
        "desc": "克雷吉·塞西尔——竞争对手「新视界」公司高管。他为什么会在那里等着我？救我，害我，还是想要我手里奇美拉的机密芯片？"
    },
    "memory_05": {
        "title": "机密文件·记忆干预计划",
        "brief": "奇美拉的阴谋",
        "desc": "奇美拉生物公司不仅在制造义体，还在制造'真相'。他们有能力重写整个城市的记忆……包括我的？"
    },
    "memory_06": {
        "title": "暗流的邀请",
        "brief": "反企业抵抗组织",
        "desc": "'暗流'——反企业抵抗组织。他们一直在监视奇美拉的一举一动。为什么是我？因为芯片，还是因为……我是'Omega'？"
    },
    "memory_07": {
        "title": "前任恋人",
        "brief": "珀西·杨的真相",
        "desc": "我的恋人，竟然是个仿生人，恋慕更无从谈起……我居然被欺骗了整整三年。"
    },
    "memory_08": {
        "title": "第一夜",
        "brief": "背叛之夜的总结",
        "desc": "逃离奇美拉，在雨夜中躲避追捕。那个叫'7号'的男人追上了我，死对头克雷吉出现，前恋人兼谈判专家珀西也找上门来。我拿着关于'记忆干预计划'的芯片，在这个充满霓虹与背叛的城市里，做出了第一个选择。"
    }
}

# 已收集的记忆列表（持久化存储）
default persistent.collected_memories = []

# 显示记忆卡片通知的函数
init python:
    def show_memory(memory_id):
        if memory_id not in persistent.collected_memories:
            persistent.collected_memories.append(memory_id)

        if memory_id in memories:
            memory = memories[memory_id]
            renpy.show_screen("memory_card", memory_title=memory["title"], memory_desc=memory["brief"])

    def has_memory(memory_id):
        return memory_id in persistent.collected_memories
