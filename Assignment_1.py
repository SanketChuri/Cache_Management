
cache = list()
requests = list()

user_input = input("Press 1 for FIFO, Press 2 for LFU, or Press Q to QUIT the program.: ")
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
      print("Miss")
      return 
    elif value not in cache and len(cache) == 8:
      cache.pop(0)
      cache.append(value)
      # print('Cache3',cache)
      print("Miss")
      return
    # break
  return

      
    

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

      # cache.append(val)

 
   
    
     
      


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


