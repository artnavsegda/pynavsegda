def my_function(cip_join):
    packed_join = (cip_join // 256) + ((cip_join % 256) * 256)
    print(packed_join.to_bytes(2, "big"))

my_function(10)
my_function(100)
my_function(1000)
my_function(10000)