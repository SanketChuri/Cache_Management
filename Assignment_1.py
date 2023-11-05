
cache = list()
requests = list()
frequency = dict()

while True:
  user_input = input("Press 1 for FIFO, Press 2 for LFU, or Press Q to QUIT the program.: ").capitalize()
  # print('user_input_user_input',user_input, type(user_input))


  def fifo(value):
    print('Value',value)
    while value != 0 :
      if value in cache: 
          print('Hit')
          # print('Cache1',cache)
          return 
      elif value not in cache and len(cache) < 8:
        cache.append(value)
        # print('Cache2',cache)
        print('Miss')
        return 
      elif value not in cache and len(cache) > 7:
        cache.pop(0)
        cache.append(value)
        # print('Cache3',cache)
        print('Miss')
        return
      # break
    return

  def lfu(value):
    # print('len(cache)len(cache)',len(cache))
    print('Value',value)
    while value != 0 :
      if value in cache:
        frequency[value] += 1
        print('Hit')
        # print('frequency1',frequency,)
        # print('cache1',cache)
        return
      
      elif value not in cache and len(cache) < 8:
        cache.append(value)
        frequency[value] = 1
        print('Miss')
        # print('frequency2',frequency,)
        # print('cache2',cache)
        return

      elif value not in cache and len(cache) > 7:

        # print('frequency3',frequency)
        # print('cache3',cache)
        lowestFrequencyValue = min(frequency.values())
        # print('lowestFrequencyValue',lowestFrequencyValue)

        lowestFrequencyKeyList = [key for key in frequency 
                                  if frequency[key] == lowestFrequencyValue]
        # print("lowestFrequencyKeyList",lowestFrequencyKeyList)

        lowestFrequencyKey = min(lowestFrequencyKeyList)
        # print('lowestFrequencyKey',lowestFrequencyKey)

        cacheIndex = cache.index(lowestFrequencyKey)
        # print('cacheIndex',cacheIndex)
        cache.pop(cacheIndex)
        frequency.pop(lowestFrequencyKey)









        # # f = ((cache)[:8])
        # # print('fffffffffff',f, frequency)

        # print('frequency3',frequency,)
        # print('cache3',cache)

        # f = dict(frequency.items())
        # print('ffffffffffff',f,)
        # # # now to find the lowest frequency(value)
        # lowestRequestValue = (min(f.values()))
        # print('lowestRequestValue',lowestRequestValue)

        # # # now to find the lowest frequency(key)
        # lowestRequestKeyList = [key for key in f 
        #                     if f[key] == lowestRequestValue]
        # print('lowestRequestKeyList',lowestRequestKeyList)

        # lowestRequestKey = min(lowestRequestKeyList)
        # print('lowestRequestKey',lowestRequestKey)

        # print('cachecache',cache)
        # index = cache.index(lowestRequestKey)
        # print('indexindex',index)

        
        # evictPageNumberKey = (lowestRequestKeyList.pop(lowestRequestKey))
        # print('evictPageNumber',evictPageNumberKey)

        # evictPageNumberKey = (lowestRequestKey.pop(0))
        # print('evictPageNumber',evictPageNumberKey)
        # print('before index cachecachecache',(cache))
        # print("frequencyfrequency",frequency)
        # index = cache.index(evictPageNumberKey)
        

        # cache.pop(index)
        cache.append(value)
        # # print('afyer indexcachecachecache',(cache))
        frequency[value] = 1
        print('Miss')
        # print('cachecache',cache)

        # print('cache',cache)
        # print("frequencyfrequency",frequency)
        # lowestRequestKeyList.clear()
        # f.clear()
        
        return
    return
  
  
  while True:
    val = int(input("Enter Number: "))
    requests.append(val)
    if val != 0:
      if user_input == "1":
        fifo(val)
        
      elif user_input == "2":
        lfu(val)
        
      elif print("Process has been terminate"):
        exit()
    else :
      print("Cache List",cache)
      print("Request List",requests)
      print("frequencyfrequency",frequency)
      cache.clear()
      requests.clear()
      frequency.clear()
      break

    # if user_input == "1":
    #   while True:
    #     val = int(input("Enter Number: "))
    #     requests.append(val)
    #     if val != 0: 
    #       fifo(val)
    #     else :
    #       print("Cache List",cache)
    #       print("Request List",requests)
    #       print("frequencyfrequency",frequency)
    #       cache.clear()
    #       requests.clear()
    #       break

    # elif user_input == "2":
    #   while True:
    #     val = int(input("Enter Number: "))
    #     requests.append(val)
    #     if val != 0: 
    #       lfu(val)
    #     else :
    #       print("Cache List",cache)
    #       print("Request List",requests)
    #       print("frequencyfrequency",frequency)
    #       cache.clear()
    #       requests.clear()
    #       break

    # elif user_input == "Q":
    #   print("Process has been terminate")
    #   exit()

    #---------------------------EXTRA--------------------------  
      # option = input("Do you want to terminate the process Y/N ").capitalize() 
      # if option is "Y" or "N":
      #   if option is "Y":
      #     exit()
      #   else:
      #     input("Do you want to terminate the process Y/N ").capitalize()
      # else:
      #   print('Please select proper option')
      #   input("Do you want to terminate the process Y/N ").capitalize()



