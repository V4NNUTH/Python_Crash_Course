aliens = []

for alien_num in range(30):
    new_alien = {'colur':'red','point':5,'speed':'slow'}
    aliens.append(new_alien)
   

for alien in aliens[:5]:
    print(alien)

print("...")

print(f"Total number of aliens: {len(aliens)}")