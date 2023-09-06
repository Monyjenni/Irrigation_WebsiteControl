import json
readings = []
for x in range (5):
    readings.append({
        'time':x,
        'temperature': 30+x,
        'humidity':60})
print(readings)