# import time
# import multiprocessing


# start = time.perf_counter()

# def do_something():
#     print('Sleeping 1 second')
#     time.sleep(1)
#     print('Done Sleeping')


# if __name__ == '__main__':  
#     p1 = multiprocessing.Process(target= do_something)
#     p2 = multiprocessing.Process(target= do_something)

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     finish = time.perf_counter()

#     print(f'finished in {round(finish-start)} second(s)')








# -------What if we wanted to run our code 10 times?
# import time
# import multiprocessing


# start = time.perf_counter()

# def do_something():
#     print('Sleeping 1 second')
#     time.sleep(1)
#     print('Done Sleeping')


# if __name__ == '__main__':  
    
#     processes = []

#     for _ in range(10):
#         p = multiprocessing.Process(target= do_something)
#         p.start()
#         processes.append(p)
    
#     for process in processes:
#         p.join()

#     finish = time.perf_counter()

#     print(f'finished in {round(finish-start)} second(s)')









# -------Passing an argument...
# import time
# import multiprocessing


# start = time.perf_counter()

# def do_something(seconds):
#     print(f'Sleeping {seconds} second')
#     time.sleep(seconds)
#     print('Done Sleeping')


# if __name__ == '__main__':  
    
#     processes = []

#     for _ in range(10):
#         p = multiprocessing.Process(target= do_something, args = [1.5])
#         p.start()
#         processes.append(p)
    
#     for process in processes:
#         p.join()

#     finish = time.perf_counter()

#     print(f'finished in {round(finish-start)} second(s)')













# -------Using Concurrent.futures and context manager...
# import time
# import concurrent.futures


# start = time.perf_counter()

# def do_something(seconds):
#     print(f'Sleeping {seconds} second')
#     time.sleep(seconds)
#     return 'Done Sleeping'


# if __name__ == '__main__':  
    
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         f1 = executor.submit(do_something, 1)
#         f2 = executor.submit(do_something, 1)
#         print(f1.result())
#         print(f2.result())

#     finish = time.perf_counter()

#     print(f'finished in {round(finish-start)} second(s)')









# -------Looping 10 times...
# import time
# import concurrent.futures


# start = time.perf_counter()

# def do_something(seconds):
#     print(f'Sleeping {seconds} second')
#     time.sleep(seconds)
#     return 'Done Sleeping'


# if __name__ == '__main__':  
    
#     with concurrent.futures.ProcessPoolExecutor() as executor:
        
#         results = [executor.submit(do_something, 1) for _ in range(10)]

#         for f in concurrent.futures.as_completed(results):
#             print(f.result())

#     finish = time.perf_counter()

#     print(f'finished in {round(finish-start)} second(s)')










# -------Passing a list of seconds...
# import time
# import concurrent.futures


# start = time.perf_counter()

# def do_something(seconds):
#     print(f'Sleeping {seconds} second')
#     time.sleep(seconds)
#     return f'{seconds} Done Sleeping'


# if __name__ == '__main__':  
    
#     with concurrent.futures.ProcessPoolExecutor() as executor:
        
#         seconds = [5,4,3,2,1]

#         results = [executor.submit(do_something, sec) for sec in seconds]

#         for f in concurrent.futures.as_completed(results):
#             print(f.result())

#     finish = time.perf_counter()

#     print(f'finished in {round(finish-start)} second(s)')










# -------Using map method...
# import time
# import concurrent.futures


# start = time.perf_counter()

# def do_something(seconds):
#     print(f'Sleeping {seconds} second')
#     time.sleep(seconds)
#     return f'{seconds} Done Sleeping'


# if __name__ == '__main__':  
    
#     with concurrent.futures.ProcessPoolExecutor() as executor:
        
#         seconds = [5,4,3,2,1]
#         # When we used submit, it returned future objects, 
#         # but when we use map, it just returns the results...
#         # map is going to return the results in the order that
#         # they were started...
#         results = executor.map(do_something, seconds)

#         # It actually did not finish in that order...
#         for result in results:
#             print(result)
#             # --Output
#             # 5 Done Sleeping
#             # 4 Done Sleeping
#             # 3 Done Sleeping
#             # 2 Done Sleeping
#             # 1 Done Sleeping

#     finish = time.perf_counter()

#     print(f'finished in {round(finish-start)} second(s)')











# # -------Real-world example...Synchronous
# import time
# from PIL import Image, ImageFilter
# import concurrent.futures



# img_names = [
#     'photo-1516117172878-fd2c41f4a759.jpg',
#     'photo-1532009324734-20a7a5813719.jpg',
#     'photo-1516972810927-80185027ca84.jpg',
#     'photo-1541698444083-023c97d3f4b6.jpg',
#     'photo-1493976040374-85c8e12f0c0e.jpg',
#     'photo-1522364723953-452d3431c267.jpg',
#     'photo-1549692520-acc6669e2f0c.jpg',
#     'photo-1504198453319-5ce911bafcde.jpg',
#     'photo-1524429656589-6633a470097c.jpg',
#     'photo-1550439062-609e1531270e.jpg',
#     'photo-1507143550189-fed454f93097.jpg',
#     'photo-1530122037265-a5f1f91d3b99.jpg',
#     'photo-1564135624576-c5c88640f235.jpg',
#     'photo-1513938709626-033611b8cc03.jpg',
#     'photo-1530224264768-7ff8c1789d79.jpg'
# ]

# start = time.perf_counter()


# size = (1200, 1200)


# for img_name in img_names:
#     img = Image.open(img_name)

#     img = img.filter(ImageFilter.GaussianBlur(15))

#     img.thumbnail(size)

#     img.save(f'processed/{img_name}')

#     print(f'{img_name} was processed...')


# finish = time.perf_counter()

# print(f'finished in {round(finish-start)} second(s)') # finished in 15 second(s)










# ----------Parallel
import time
from PIL import Image, ImageFilter
import concurrent.futures



img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1549692520-acc6669e2f0c.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg'
]

start = time.perf_counter()


size = (1200, 1200)


def process_image(img_name):
    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)

    img.save(f'processed/{img_name}')

    print(f'{img_name} was processed...')


if __name__ == '__main__':  

    with concurrent.futures.ProcessPoolExecutor() as executor:

        executor.map(process_image, img_names)



    finish = time.perf_counter()

    print(f'finished in {round(finish-start)} second(s)') # finished in 5 second(s)