REDIS_ADDR = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PD = ''
result_db = 4
ansible_remote_user = 'root'
ansible_result_redis_db  = 10
BROKER = "redis://:%s@127.0.0.1:6379/3" % REDIS_PD
BACKEND = "redis://:%s@127.0.0.1:6379/4" % REDIS_PD
inventory = 'scripts/inventory'