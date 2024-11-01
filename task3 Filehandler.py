import json

class FileHandler:
    @staticmethod#装饰器用于定义一个静态方法。静态方法不接受隐式的 self 参数，不依赖类实例
    def save_tasks(tasks, filename="tasks.json"):
        data = [
            {
                "title": task.title,
                "description": task.description,
                "time": task.time.strftime("%Y-%m-%d"),
                "priority": task.priority,
                "status": task.status,
            }
            for task in tasks#循环，task遍历tasks
        ]
        with open(filename, "w") as f:
            json.dump(data, f)

    @staticmethod
    def load_tasks(filename="tasks.json"):
        tasks = []
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for item in data:
                    time = time.strptime(item["time"], "%Y-%m-%d")
                    task = task(
                        title=item["title"],
                        description=item["description"],
                        time=time,
                        priority=item["priority"]
                    )
                    task.status = item["status"]
                    tasks.append(task)
        except FileNotFoundError:
            print("No saved tasks found.")
        return tasks