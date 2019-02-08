# class Employee:
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@brunel.ac.uk'
#
#     def fullname(self):
#         return'{} {}'.format(self.first, self.last)
#
#
#
# emp_1 = Employee('Bob', 'Jones', 3500)
# emp_2 = Employee('Jane', 'Jackson', 5500)
#
#
# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())
#
#
# print('{} {}'.format(emp_1.first, emp_1.last))


#: Exercise 1 --------------------------------------------------------------------------------------

# class Enemy:
#
#     weaponsList = {"Katana": 12, "Pistol": 4, "Smg": 6, "Rifle": 8}
#
#     def __init__(self, first_name, last_name, clan, special, description):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.clan = clan
#         self.special = special
#         self.description = description
#
#     def Set_Description(self):
#         self.description = str(self.first_name), "is a high-ranking gangster working for a weapon smuggling syndicate."
#
#     def Get_Description(self):
#         print('{} {}'.format('Known activities:', self.description))
#
#     def Get_Full_Name(self):
#         print('\n', '{} {} {}'.format('Name:', self.first_name, self.last_name))
#
#     def Get_Clan_Name(self):
#         print('{} {}'.format('Clan:', self.clan))
#
#     def Get_Weapons_List(self):
#         #print('{} {}'.format('Weapon proficiencies: ', str((self.weaponsList).replace("{", "").replace("}", ""))))
#         try:
#             for key, value in self.weaponsList.items():
#                 pass
#             print('Weapon proficiencies:')
#             for key, value in self.weaponsList.items():
#                 print('\t', '{}: {}'.format(key, value))
#         except:
#             print('Weapon proficiencies: -UNKNOWN-')
#
#     def Get_Special(self):
#         print('{} {}'.format('Special ability:', self.special))
#
#     def Get_Full_Report(self):
#         print('\n', '{} {} {}'.format('Name:', self.first_name, self.last_name))
#         print('{} {}'.format('Clan:', self.clan))
#         print('{} {}'.format('Known activities:', self.description))
#         try:
#             for key, value in self.weaponsList.items():
#                 pass
#             print('Weapon proficiencies:')
#             for key, value in self.weaponsList.items():
#                 print('\t', '{}: {}'.format(key, value))
#         except:
#             print('Weapon proficiencies: -UNKNOWN-')
#         print('{} {}'.format('Special ability:', self.special))
#
#     def Add_Weapon_Explosives(self):                                                   # This adds to all enemies - why?
#         self.weaponsList['Explosives'] = 10
#
# #: Spawn 5 enemies using a range loop
# for x in range(1,6):
#     if x < 6:                   # How to make this create new enemies by adding the iterated integer to each enemy name?
#         #spawn_enemy = 'enemy_'+str(x)
#         #print(spawn_enemy)
#         enemy_<(x)> = Enemy('Gangster', 'Thug', 'The Brawlers', 'Painkiller', 'Assault, theft and fraud.')
#         x += 1
#
# #: Spawn 2 enemies
# enemy_1 = Enemy('Scars', 'McSlasher', 'The Blades', 'Slashing spree', '')
# enemy_2 = Enemy('Black', 'Eyes', 'Iron Fist', 'Berserk rage', '-INVESTIGATION ONGOING-')
#
# #: Add description to 'enemy_1'
# enemy_1.Set_Description()
#
# #: Add 'Explosives' weapon to 'enemy_2' 'weaponList' dictionary
# enemy_2.Add_Weapon_Explosives()                # This adds 'Explosives' to all class instances - why? Linked to line 79?
#
# #: Print full details of 'enemy_1' and 'enemy_2'
# enemy_1.Get_Full_Report()
# enemy_2.Get_Full_Report()

# enemy_2.Get_Full_Name()
# enemy_2.Get_Description()
# enemy_2.Get_Weapons_List()


#: Questions:
#: 1) How to remove single-space indentation on printed 'Name' lines? (Need to keep new-line spacing.)
#: 2) Is there a cleaner way to remove a dictionary's curly brackets when printing it as a list?


#: Exercise 2 --------------------------------------------------------------------------------------

class Collectible:


