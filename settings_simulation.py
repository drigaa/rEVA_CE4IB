controller = True
Kp_value = 1e3 ## perfect would be inf

imposed_time_step = False
Δt = 240

temp_init = 21
temp_indor_setpoint = 21
Qa = 20

start_date = '01-01 12:00:00'
end_date = '12-30 18:00:00'
start_date = '2000-' + start_date
end_date = '2000-' + end_date

air_with_capacity = False

## Overwrite for steady state analysis
To_ss = 10
Ti_sp_ss = 21
Qa_ss = 25

## Wall settings
slope = 90
azimuth_east = -90
azimuth_north = 180
latitude = 46
wall_area = 9
albedo = 0.2
alpha = 0.25
beta_window = 0.8
view_factor = 0.2

if __name__ == '__main__':
    print(f'{start_date} \tstart date')
    print(f'{end_date} \tend date')