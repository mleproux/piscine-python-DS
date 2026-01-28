from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

print("tqdm :")
for elem in tqdm(range(333), bar_format='{l_bar}{bar:80}{r_bar}{bar:-10b}'):
    sleep(0.005)
print()
print("ft_tqdm :")
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
