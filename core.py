import datetime

S_apic = ['Antharas', 'Valakas']
apic = ['Orfen', 'Beleth', 'Baium', 'Core', 'Queen Ant']


def validate_data(unvalid_data):
    valid_str = str(unvalid_data).replace(' Boss', '')
    valid_str = valid_str.replace(' was killed', '')
    valid_data = str(valid_str).split(': ')
    valid_data[0] = datetime.datetime.strptime(
        valid_data[0],
        "%Y-%m-%d %H:%M:%S",
        )

    return valid_data


def calc_time_for_boss(boss_name, time):
    boss_name_vl = boss_name.upper()
    offset = datetime.timezone(datetime.timedelta(hours=3))
    current_time = datetime.datetime.now(offset)
    vl_current_time = datetime.datetime.strftime(
        current_time,
        "%Y-%m-%d %H:%M:%S"
        )
    vl_current_time = datetime.datetime.strptime(
        vl_current_time,
        "%Y-%m-%d %H:%M:%S"
        )
    if boss_name in S_apic:
        t_d = datetime.timedelta(days=10)
        if time.date() + t_d > vl_current_time.date():
            start_resp = time.date() + t_d
            ag_start_resp = start_resp - vl_current_time.date()
            message = f'''BOS DONT LIVE!
resp {boss_name_vl} start {ag_start_resp.days} day later at  18:00
resp end at {start_resp} 00: 00'''
        else:
            message = f'''BOSS {boss_name_vl} RESP TODAY AT 18:00 - 00:00'''

    elif boss_name in apic:
        t_d = datetime.timedelta(days=5)
        if time.date() + t_d > vl_current_time.date():
            start_resp = time.date() + t_d
            ag_start_resp = start_resp - vl_current_time.date()
            message = f'''BOS DONT LIVE!
resp {boss_name_vl} start  {ag_start_resp.days} day later at 18:00
resp end at {start_resp} 00: 00'''
        else:
            message = f'''BOSS {boss_name_vl} RESP TODAY AT 18:00 - 00:00'''
    else:
        t_d = datetime.timedelta(hours=12)
        if time + t_d > vl_current_time:
            start_resp = time + t_d
            end_resp = time + 2 * t_d
            ag_start_resp = start_resp - vl_current_time
            message = (f'''BOS DONT LIVE!
resp {boss_name_vl} start at {ag_start_resp} hours leater
resp end {end_resp} hours later''')
        elif time + 2*t_d < vl_current_time:
            print(f'kill ({time})')
            print(f'kill+ T_d ({time+t_d})')
            print(f'kill+ 2*t_d({time+2*t_d})')
            message = ('''BOS LIVE!''')
        else:
            print(f'kill ({time})')
            print(f'kill+ T_d ({time+t_d})')
            print(f'kill+ 2*t_d({time+2*t_d})')
            start_resp = time + t_d
            end_resp = start_resp + t_d
            ag_end_resp = end_resp - vl_current_time
            message = (f'''BOSS MAYBE LIVE?)
resp {boss_name_vl} start  at {start_resp}
resp end {ag_end_resp} hours later''')
    return message

# dney 10 resp 18: 00 do 00 00
# dney 5 d 18: 00 do 00
# 24 +-12
