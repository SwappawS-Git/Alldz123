
import threading 
import random
import time



files = ["photo.jpg", "document.pdf", "video.mp4", "archive.zip"]

def DownloadFile(FileName):
    print(f'Початок завантаження файла - {FileName}...')
    time.sleep(random.randint(1, 3))
    print(f'Файл {FileName} завантажився')
print('NO THreading______________________')
NoTHread_Start_time = time.perf_counter()
for i in files:
    DownloadFile(i)
NoTHread_END_time = time.perf_counter()
print('THreading_________________________')
THread_Start_time = time.perf_counter()

ThReads = [threading.Thread(target=DownloadFile, args=[i]) for i in files]
for i in ThReads:
    i.start()

for i in ThReads:
    i.join()

THread_END_time = time.perf_counter()

TimeNow = time.perf_counter()
Th = THread_END_time - THread_Start_time
NoTh = NoTHread_END_time - NoTHread_Start_time
print('_____________Times________________')
print()
print(f"No ThRead time {NoTh}")
print(f"ThRead    time {Th}")
print(f'Різниця у часі  {NoTh-Th}')