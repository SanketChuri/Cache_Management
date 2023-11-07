# Name:- Sanket Manoj Churi
# Student Number:- 201700900

cache = list()
requests = list()
frequency = dict()

while True:
  user_input = input("Press 1 for FIFO, Press 2 for LFU, or Press Q to QUIT the program.: ").capitalize()

  if user_input == "Q":
    print("Process has been terminate")
    exit()
  elif user_input not in ("1","2","Q"):
    print('Please select the given input.')
    continue

  def fifo(value):
    while value != 0 :
      if value in cache: 
          print('Hit')
          return 
      elif value not in cache and len(cache) < 8:
        cache.append(value)
        print('Miss')
        return 
      elif value not in cache and len(cache) > 7:
        cache.pop(0)
        cache.append(value)
        print('Miss')
        return
      break
    return

  def lfu(value):
    while value != 0 :
      if value in cache:
        frequency[value] += 1
        print('Hit')
        return
      
      elif value not in cache and len(cache) < 8:
        cache.append(value)
        frequency[value] = 1
        print('Miss')
        return

      elif value not in cache and len(cache) > 7:

        lowestFrequencyValue = min(frequency.values())

        lowestFrequencyKeyList = [key for key in frequency 
                                  if frequency[key] == lowestFrequencyValue]

        lowestFrequencyKey = min(lowestFrequencyKeyList)

        lowestFrequencyKeyIndex = cache.index(lowestFrequencyKey)
        cache.pop(lowestFrequencyKeyIndex)
        frequency.pop(lowestFrequencyKey)
        cache.append(value)
        frequency[value] = 1
        print('Miss')
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

    else :
      print("Cache List",cache)
      print("Request List",requests)
      # print("frequencyfrequency",frequency)
      cache.clear()
      requests.clear()
      frequency.clear()
      break

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



