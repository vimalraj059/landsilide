from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    # Simulated sensor readings
    moisture = random.randint(0, 100)  # percentage
    vibration = random.randint(0, 10)  # arbitrary units

    # Danger condition
    if moisture > 80 and vibration > 7:
        status = "⚠️ Danger: Landslide Risk Detected!"
        color = "red"
    elif moisture > 60:
        status = "⚠️ Warning: High Soil Moisture"
        color = "orange"
    else:
        status = "✅ Safe"
        color = "green"

    return render_template('index.html',
                           moisture=moisture,
                           vibration=vibration,
                           status=status,
                           color=color)

if __name__ == '__main__':
    app.run(debug=True)
