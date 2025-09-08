import signal_ICT_TakshAmrutiya_92400133191 as at
# task_1 : Generate and plot a unit step signal and a unit impulse signal of length 20.
at.unit_step(20)
at.unit_impulse(20)

# task_2 : Generate a sine wave of amplitude 2, frequency 5 Hz, phase 0, over t = 0 to 1 sec.
at.sine_wave(2,5,0,0)

# taks_3 : Perform time shifting on the sine wave by +5 units and plot both original and shifted signals.
_org_wave = at.sine_wave(1,3,0,5)
at.time_shift(_org_wave,5)

# taks_4 : Perform addition of the unit step and ramp signal and plot the result.
unit_step = at.unit_step(5)
ramp_ = at.ramp_signal(5)
at.signal_addition(unit_step,ramp_)

# task_5 : Multiply a sine and cosine wave of same frequency and plot the result.
sine = at.sine_wave(1,6,0,2)
cosine = at.cosine_wave(1,6,0,2)
at.signal_multiplication(sine,cosine)
