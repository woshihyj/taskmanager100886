class task:#定义一个task类
    def __init__(self,title,description,time,priority,status):#init初始化函数
        self.title=title
        self.description=description#对任务的描述
        self.time=time#期望的时间
        self.priority=priority#优先级：1：Highest,2:High,3:Medium,4:Low,5:Lowest
        self.status=status#地位

    def update_task(self, title=None, description=None, time=None, priority=None, status=None):#添加任务到列表
        if title:
            self.title = title
        if description:
            self.description = description
        if time:
            self.time = time
        if priority:
            self.priority = priority
        if status:
            self.status = status

    def __str__(self):
        return f"{self.title} |{self.description}|Time:{self.time.strftime('%Y-%m-%d')}|Priority:{self.priority}|Status:{self.status}"