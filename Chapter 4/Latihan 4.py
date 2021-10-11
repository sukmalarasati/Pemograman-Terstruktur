#pukul berapa sampai di kota C

#kotaA ke kotaB
jarakkotaA_ke_B = 125
kecepatankotaA_ke_B = 62
#kotaB ke kotaC
jarakkotaB_ke_C = 256
kecepatankotaB_ke_C = 70

#waktu yang di tempuh kotaA ke B
waktuJamdarikotaA_ke_B   = jarakkotaA_ke_B // kecepatankotaA_ke_B
waktuMenitdarikotaA_ke_B = round((jarakkotaA_ke_B % kecepatankotaA_ke_B) / kecepatankotaA_ke_B * 60)

#waktu yang di tempuh kotaB ke C
waktuJamdarikotaB_ke_C   = jarakkotaB_ke_C // kecepatankotaB_ke_C
waktuMenitdarikotaB_ke_C = round((jarakkotaB_ke_C % kecepatankotaB_ke_C) / kecepatankotaB_ke_C * 60)

#waktu awal berangkat
waktuJamberangkat   = 6
waktuMenitberangkat = 0

#waktu break
waktuMenitbreak     = 45

#waktu sampai kota C
waktuJamSampai   = (waktuJamberangkat + waktuJamdarikotaA_ke_B + waktuJamdarikotaB_ke_C)
waktuMenitSampai = (waktuMenitberangkat + waktuMenitdarikotaA_ke_B + waktuMenitdarikotaB_ke_C + waktuMenitbreak)
if (waktuMenitSampai >= 60):
    waktuJamSampai   += 1
    waktuMenitSampai -= 60

	
print("Jadi, Pak Amir sampai di kota C pada pukul %d.%d" % (waktuJamSampai,waktuMenitSampai))
