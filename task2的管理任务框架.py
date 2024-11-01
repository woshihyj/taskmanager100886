class TaskManager:
    def __init__(self):#初始化
        self.tasks=[]

    def add_task(self,task):#添加任务
        self.tasks.append(task)

    def remove_task(self,title):
        self.tasks=[task for task in self.tasks if task.title !=title]#删除与输入title一样的任务

    def update_tsak(self,**kwargs):#**kwargs表示关键参数（固定用法）
        for task in self.tasks:
            if task.title == title:#判断title是否一致
                task.update_task(**kwargs)#将字典更新

    def display_tasks(self, sort_by="priority"):
        if sort_by == "priority":
            tasks = sorted(self.tasks, key=lambda x: x.priority)#lambda表示匿名函数,key用于指定键值？
        elif sort_by == "time":
            tasks = sorted(self.tasks, key=lambda x: x.time)
        for task in tasks:
            print(task)
