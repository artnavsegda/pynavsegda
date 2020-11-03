def my_function(cip_join):
    packed_join = (cip_join // 256) + ((cip_join % 256) * 256)
    print(packed_join)

my_function(25)
my_function(1000)
my_function(15000)