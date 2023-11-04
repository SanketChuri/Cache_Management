
cache = list()
requests = list()
frequency = dict()

user_input = input("Press 1 for FIFO, Press 2 for LFU, or Press Q to QUIT the program.: ").capitalize()
print('user_input_user_input',user_input, type(user_input))


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
    elif value not in cache and len(cache) == 8:
      cache.pop(0)
      cache.append(value)
      # print('Cache3',cache)
      print('Miss')
      return
    # break
  return

def lfu(value):
  print('len(cache)len(cache)',len(cache))
  while value != 0 :
    if value in cache:
      frequency[value] += 1
      print('Miss')
      return
    elif value not in cache and len(cache) < 8:
      cache.append(value)
      frequency[value] = 1
      print('Hit')
      return
    elif value not in cache and len(cache) > 7:
      # a = sorted(cache[:9])
      # print('aaaaaaaaaaaaaa',a)

      f = dict(sorted(frequency.items())[:8])
      print('ffffffffffff',f)

      # now to find the lowest frequency
      




      


      
      
      

      
      cache.append(value)
      frequency[value] = 1
      print('cache',cache)
      print("frequencyfrequency",frequency)
      print('habibibib')
      return
  return












    # if value in cache:
    #   print('Hit')
    #   for i in cache:
    #     if i in frequency:
    #       frequency[i] += 1
    #     else:
    #       frequency[i] = 1
    #     print(frequency)
    # return
    


if user_input == "1":
  while True:
    val = int(input("Enter Number: "))
    requests.append(val)
    if val != 0: 
      fifo(val)
    else :
      print("Cache List",cache)
      print("Request List",requests)
      cache.clear()
      break

elif user_input == "2":
  while True:
    val = int(input("Enter Number: "))
    requests.append(val)
    if val != 0: 
      lfu(val)
    else :
      print("Cache List",cache)
      print("Request List",requests)
      print("frequencyfrequency",frequency)
      cache.clear()
      break

elif user_input == "Q":
  option = input("Do you want to terminate the process Y/N ").capitalize() 
  if option is "Y" or "N":
    if option is "Y":
      exit()
    else:
      input("Do you want to terminate the process Y/N ").capitalize()
  else:
    print('Please select proper option')
    input("Do you want to terminate the process Y/N ").capitalize()

    




    
     
      


# def fifo(value):
#   # while True:
#   #   if value not in cache:
#   #     cache.append(value)
#   #     print('cacheeeeeeeee',cache)
#   #     print("Miss - add ",value, " to cache")
#   # else:
#   #     print("Hit - already got ",value," in cache")
#   # return value

#  while True:
#     # print('enter a number'),int(input())
#     # val = int(input())
#     if value not in cache:
#         cache.append(value)
#         print('sssssss',value)
#     # else:
#     #     a.sort()
#     #     for i in a:
#     #         print(i)

#     #     for i in a:
#     #         if i not in notRepeatedList:
#     #             notRepeatedList.append(i)
#     #             print('Repeated', a)
#     #             print('Not Repeated', notRepeatedList)
#         break



  


# print('dsdsddsd',fifo())


  
# elif user_input == 2:
#   lfu()
# elif user_input == Q:
#   quit


