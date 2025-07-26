import random
from datetime import datetime

def generate_commit_message():
    verbs = ["Fix", "Add", "Improve", "Update", "Refactor", "Remove", "Optimize"]
    objects = ["RPC handler", "CLI argument", "ENS lookup", "token logic", "auth check"]
    contexts = ["flow", "code", "support", "handler", "logic"]

    return f"{random.choice(verbs)} {random.choice(objects)} in {random.choice(contexts)}"

def generate_fake_log_entry(index):
    timestamp = datetime.now().isoformat()
    rand_value = random.randint(10000, 99999)
    return f"[AUTO LOG {index}] {timestamp} random={rand_value}"

if __name__ == "__main__":
    print("Пример генерации 5 сообщений:")
    for i in range(1, 6):
        print(generate_fake_log_entry(i))
        print("→", generate_commit_message())
