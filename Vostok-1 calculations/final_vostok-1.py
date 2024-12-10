import math
import time
import krpc


turn_start_altitude = 600
turn_end_altitude = 38_000
target_altitude_to_sep = 120_000

conn = krpc.connect(name='Выход на орбиту')
vessel = conn.space_center.active_vessel
flight = vessel.flight()

ref_frame = vessel.orbit.body.reference_frame
# Set up streams for telemetry
ut = conn.add_stream(getattr, conn.space_center, 'ut')
altitude = conn.add_stream(getattr, vessel.flight(), 'mean_altitude')
apoapsis = conn.add_stream(getattr, vessel.orbit, 'apoapsis_altitude')
stage_3_resources = vessel.resources_in_decouple_stage(stage=3, cumulative=False)
srb_fuel3 = conn.add_stream(stage_3_resources.amount, 'LiquidFuel')


stage_2_resources = vessel.resources_in_decouple_stage(stage=2, cumulative=False)
srb_fuel2 = conn.add_stream(stage_2_resources.amount, 'LiquidFuel')


stage_1_resources = vessel.resources_in_decouple_stage(stage=1, cumulative=False)
srb_fuel1 = conn.add_stream(stage_1_resources.amount, 'LiquidFuel')

# Pre-launch setup
vessel.control.sas = False
vessel.control.rcs = True
vessel.control.throttle = 0.8

# Countdown...
print('3...')
time.sleep(1)
print('2...')
time.sleep(1)
print('1...')
time.sleep(1)
print('Запуск!')

print(f'Начальное кол-во жидкого топлива: {srb_fuel3()}')
# Activate the first stage
vessel.control.activate_next_stage()
vessel.auto_pilot.engage()
vessel.auto_pilot.target_pitch_and_heading(90, 90)

# Main ascent loop
srbs_separated = False
turn_angle = 0

h = []
v = []
t = []
secs = 0

while True:
    velocity = vessel.flight(ref_frame).speed

    h.append(int(altitude()))
    v.append(int(velocity))
    secs += 1
    time.sleep(1)
    t.append(secs)

    # Gravity turn
    if altitude() > turn_start_altitude and altitude() < turn_end_altitude:
        frac = ((altitude() * 0.8 - turn_start_altitude) / (turn_end_altitude - turn_start_altitude))
        new_turn_angle = frac * 90
        time.sleep(0.25)
        if abs(new_turn_angle - turn_angle) > 0.4:
            turn_angle = new_turn_angle
            vessel.auto_pilot.target_pitch_and_heading(90 - turn_angle, 90)

    if not srbs_separated:
        if srb_fuel3() < 0.1:
            vessel.control.throttle = 0
            time.sleep(1)
            vessel.control.activate_next_stage()
            time.sleep(2)
            vessel.control.throttle = 0.5
            srbs_separated = True
            break


print(h)
print(v)
print(t)


