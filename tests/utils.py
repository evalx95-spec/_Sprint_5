import time
import random

def generate_email():
    timestamp = int(time.time() * 1000)
    random_num = random.randint(1, 9999)
    return f"testuser_{timestamp}_{random_num}@example.com"