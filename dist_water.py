import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

# --------------------------------
# Ultrasonic Sensor Pins
# --------------------------------
TRIG = 23
ECHO = 24

# --------------------------------
# Water Sensor Pin
# --------------------------------
WATER_SENSOR = 17

# --------------------------------
# GPIO Setup
# --------------------------------
GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.setup(WATER_SENSOR, GPIO.IN)

print(" Smart Paddy Crop Management System ")
print("========================================")

try:
    while True:

        # =====================================
        # ULTRASONIC SENSOR SECTION
        # =====================================

        GPIO.output(TRIG, False)
        time.sleep(0.2)

        # Send ultrasonic pulse
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        pulse_start = None
        pulse_end = None

        timeout = time.time()

        # Wait for echo start
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

            if pulse_start - timeout > 0.5:
                break

        timeout = time.time()

        # Wait for echo end
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

            if pulse_end - timeout > 0.5:
                break

        # Distance calculation
        if pulse_start and pulse_end:

            pulse_duration = pulse_end - pulse_start

            distance = pulse_duration * 17150
            distance = round(distance, 2)

            # Paddy crop stage classification
            if distance < 10:
                crop_stage = "GERMINATIVE"

            elif distance < 30:
                crop_stage = "VEGETATIVE"

            else:
                crop_stage = "TILLERING"

        else:
            distance = 0
            crop_stage = "SENSOR ERROR"

        # =====================================
        # WATER SENSOR SECTION
        # =====================================

        sensor_value = GPIO.input(WATER_SENSOR)

        # Water detected
        if sensor_value == 1:

            water_level = "HIGH"
            motor_status = "OFF"

        # No water detected
        else:

            water_level = "LOW"
            motor_status = "ON"

        # =====================================
        # FINAL OUTPUT
        # =====================================

        print("\n Paddy Field Status ")
        print("================================")

        print(f" Crop Distance : {distance} cm")
        print(f" Crop Stage    : {crop_stage}")

        print("--------------------------------")

        print(f" Water Level   : {water_level}")
        print(f" Motor Status  : {motor_status}")

        print("================================")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nProgram stopped")

finally:
    GPIO.cleanup()
