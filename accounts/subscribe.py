
import redis
import datetime
'''
r=redis.StrictRedis(db=1)
print(r)
r.set("name","nitesh")
print(r.get("name").decode('utf-8'))
today=datetime.datetime.now().isoformat('/')
r.set("todaydate",today)
value=r.get("todaydate")
print(value.decode('utf-8'))
set={"nitesh","ritu","ashu","naman"}
r.flushall()
r.set("set",set)
value=r.get("set").decode('utf-8')
print(value,type(value))
value=value[1:len(value)-1]
list=value.split(',')
print(list)
for i in list:
    print(i)
'''
'''
channel="cook"
alice_r=redis.Redis(db=2)
alice_p=alice_r.pubsub()
alice_p.subscribe(channel)

bob_r=redis.Redis(db=2)
bob_p=bob_r.pubsub()
bob_p.subscribe(channel)

admin_r=redis.Redis(db=2)
#alice_p.unsubscribe()
admin_r.publish(channel,f"hello the subscribers of {channel}  channel.")

alice_p.unsubscribe(channel)

bob_p.get_message()

alice_p.get_message()

bob_messages=bob_p.get_message()
alice_messages=alice_p.get_message()

print(bob_messages)
print(alice_messages)

'''

