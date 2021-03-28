# author: github.com/teo113
# desc: This script loops through a range, and then loops through a list

# 01. range looper
num_range = list(range(1, 10+1))

for x in range(0, len(num_range)):
    try:
        print(f"no.{num_range[x]}")
    except:
        raise Exception(f"Hmmm, something went wrong on {num_range[x]}")

print(f"looped through a range of " + str(len(num_range)) + " integers")

# 02. list looper
my_list = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel']

for x in range(0, len(my_list)):
    try:
        print(f"rv point:{my_list[x]}")
    except:
        raise Exception(f"Warning at rv:{my_list[x]}")
    #else:
    #    print(f"rv checked successfully, continue with caution...")
    continue

print(str(len(my_list)), f"rv locations checked")
