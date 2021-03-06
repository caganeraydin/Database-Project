procedure_dict = {
    'Teeth Cleaning': ['D1110', 'non-surgical',
                      'Procedure for the removal of tartar (mineralized plaque) that may develop ',
                      150, '01:30'],
    'Teeth Filling': ['D2140', 'non-surgical',
                      'To treat a cavity your dentist will remove the decayed portion of the tooth and then '
                      '"fill" the area on the tooth where the decayed material was removed',
                      175, '02:30'],
    'Teeth Crown': ['02740', 'non-surgical',
                    'Dental crowns are tooth-shaped “caps” that can be placed over your tooth.',
                    325, '03:00'],
    'Root Canal': ['D3331', 'endodonctic',
                   'Root canal is a treatment to repair and save a badly damaged or infected tooth instead of removing it.',
                   250, '03:30'],
    'Braces': ['D8010', 'orthodontic',
               'Braces are dental tools that help correct problems with your teeth, like crowding, crooked teeth, '
               'or teeth that are out of alignment',
               4000, '04:00'],
    'Teeth Bonding': ['21112', 'cosmetic',
                      'Teeth bonding is a procedure in which a tooth-colored resin material (a durable plastic material) is '
                      'applied and hardened with a special light, which ultimately "bonds" the material to the tooth to restore '
                      'or improve a persons smile.',
                      300, '02:00']
}

# 0-> procedure_code
# 1-> procedure_type
# 2-> description
# 3-> amount_of_procedure