# Name:- Sanket Manoj Churi
# Student Number:- 201700900

requests = list()
cache = list()
cacheFrequency = dict()
evict = dict()

# FIFO function
def fifo(page):
    if page in cache:
        print('hit')
        return
    elif page not in cache and len(cache) < 8:
        cache.append(page)
        print('miss')
        return
    elif page not in cache and len(cache) > 7:
        cache.pop(0)
        cache.append(page)
        print('miss')
        return
    return

# LFU Function
def lfu(page):
    if page in cache:                              # When page is in cache list
        cacheFrequency[page] += 1                 # Incrementing the request frequency if request is in cache list
        print('hit')
        return

    elif page not in cache and len(cache) < 8:                    # When page is not in cache list and length of cache list is less then 8 
        cache.append(page)                                        # Putting the request in the cache if list if length of cacheless then 8 memory
        cacheFrequency[page] = 1                                  # Incrementing the request frequency if request is in cache list
        print('miss')
        return

    elif page not in cache and len(cache) > 7:                     # When request is not in cache list and length of cache list is greater then 8

        lowestCacheFrequencyValue = min(cacheFrequency.values())                             # Lowest value of Cache frequency request
        lowestCacheFrequencyKeyList = [key for key in cacheFrequency                            # List of lowest value of Cache Frequency request
                                    if cacheFrequency[key] == lowestCacheFrequencyValue]
        lowestCacheFrequencyKey = min(lowestCacheFrequencyKeyList)                                  # Smallest key of the Cache frequency list
        cache.remove(lowestCacheFrequencyKey)                                                   

        if lowestCacheFrequencyKey not in evict:                                           # To check if  lowest frequency is in evict dictionary
            evict[lowestCacheFrequencyKey] = 1                                              # set its value to 1
        else:
            evict[lowestCacheFrequencyKey] = cacheFrequency[lowestCacheFrequencyKey]          
        cacheFrequency.pop(lowestCacheFrequencyKey)
        cache.append(page)

        if page in evict:       
            evict[page] += 1
            cacheFrequency[page] = evict[page]
        else:
            cacheFrequency[page] = 1
        print('miss')
        return
    return


while True:
    val = int(input("Enter Number: "))
    if val == " ":
        continue
    elif val != 0:
        requests.append(val)
        continue
    else:
        while True:
            user_input = input("press 1 for fifo, or press 2 for lfu, or press Q to quit the program.: ").capitalize()
            if user_input == ("Q"):
                print("Process has been terminate")
                exit()
            elif user_input not in ("1", "2", "Q"):
                print('Please select the given input.')
                continue

            for i in range(len(requests)):
                number = (requests[i])
                if user_input == "1":
                    fifo(number)
                elif user_input == "2":
                    lfu(number)
            print(cache)
            cache.clear()                       # Clearing Cache
            cacheFrequency.clear()              # Clearing cacheFrequency
            evict.clear()                       # Clearing evict page dictionary
            requests.clear()                    # Clearing request
            continue
