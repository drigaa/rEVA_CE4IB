controller = True
Kp_value = 150 ## perfect would be inf

imposed_time_step = True
Δt = 240

temp_init = 0

start_date = '01-01 12:00:00'
end_date = '01-30 18:00:00'
start_date = '2000-' + start_date
end_date = '2000-' + end_date


## Overwrite for steady state analysis
To_ss = 10
Ti_sp_ss = 25
Qa_ss = 0



if __name__ == '__main__':
    print(f'{start_date} \tstart date')
    print(f'{end_date} \tend date')