import redis
import time

# redis = redis.from_url("redis://localhost:6379")
redis = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)


def test_function():
    redis.set("username", "Mcfresh")
    redis.hset("users", "name", "Obinna")
    redis.hset("users", "email", "obi@gmail.com")
    redis.expire("username", 2)
    return None


def main():
    test_function()
    print(redis.keys())
    mydict_values = redis.hgetall("users")
    print(type(mydict_values))
    var = redis.get("username")
    print(var)
    time.sleep(5)
    var = redis.get("username")
    print(var)
    time.sleep(5)
    var = redis.get("username")
    print(var)
    # print(f"The stored value is {str(var)} and I think he did well")
    # print(type(var))


if __name__ == "__main__":
    main()