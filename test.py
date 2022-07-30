it_point = 150
location = 151
dmg = 100
hp = 1000
missile = 3


def tank_dmg(hit_point, location, dmg, hp, missile):
    if hit_point == location:
        print(f'적중! {dmg * missile} 데미지 주었다!')
        hp -= dmg * missile
          
    elif hit_point == location+1  and missile == 1:
        print(f'적중! {dmg * missile} 데미지 주었다!')
        hp -= dmg * missile
        
    elif hit_point == location+1  or hit_point == location-1 and missile == 3:
        print(f'적중! {dmg * (missile-1)} 데미지 주었다!')
        hp -= dmg * (missile -1)
        
    elif hit_point == location+2 or hit_point == location-2:
        print(f'적중! {dmg } 데미지 주었다!')
        hp -= dmg
    return hp

tank_dmg(151, 151, 100, 1000, 3)
print(hp)

    


