from flask import Flask, render_template, request, redirect, flash
import math

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flash messages

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None
    error = None
    health_risk = None
    healthy_weight_range = None
    bmi_prime = None
    ponderal_index = None

    if request.method == 'POST':
        height_unit = request.form.get('height_unit')
        weight_unit = request.form.get('weight_unit')

        # Height calculation based on the selected unit
        if height_unit == 'cm':
            height = request.form.get('height')
            if not height:
                error = "Please enter your height in centimeters."
            else:
                try:
                    height = float(height) / 100  # Convert to meters
                    if height <= 0 or height > 3:  # Validate reasonable height range
                        error = "Please enter a valid height between 1cm and 300cm."
                except ValueError:
                    error = "Invalid height value."
        elif height_unit == 'ft_in':
            feet = request.form.get('feet')
            inches = request.form.get('inches')

            if not feet or not inches:
                error = "Please enter both feet and inches for height."
            else:
                try:
                    feet = float(feet)
                    inches = float(inches)
                    if feet < 0 or inches < 0 or inches >= 12:
                        error = "Please enter valid feet and inches values."
                    else:
                        height = (feet * 30.48 + inches * 2.54) / 100  # Convert to meters
                except ValueError:
                    error = "Invalid feet or inches value."
        else:
            error = "Please select a valid unit for height."

        # Weight calculation with unit conversion
        weight = request.form.get('weight')
        if not weight:
            error = "Please enter your weight."
        else:
            try:
                weight = float(weight)
                if weight_unit == 'lbs':
                    weight = weight * 0.453592  # Convert lbs to kg
                if weight <= 0 or weight > 500:  # Validate reasonable weight range
                    error = "Please enter a valid weight between 1 and 500 kg."
            except ValueError:
                error = "Invalid weight value."

        # Calculate BMI if no errors
        if not error:
            if height > 0:
                bmi = round(weight / (height ** 2), 1)  # Round to 1 decimal place
                
                # Calculate additional metrics
                bmi_prime = round(bmi / 25, 2)  # BMI Prime (ratio to upper limit of normal BMI)
                ponderal_index = round(weight / (height ** 3), 1)  # Ponderal Index
                
                # Calculate healthy weight range
                lower_weight = round(18.5 * (height ** 2), 1)
                upper_weight = round(24.9 * (height ** 2), 1)
                healthy_weight_range = f"{lower_weight} - {upper_weight} kg"

                # Determine BMI category and health risk
                if bmi < 18.5:
                    category = 'Underweight'
                    health_risk = 'Risk of nutritional deficiency'
                elif 18.5 <= bmi < 24.9:
                    category = 'Normal weight'
                    health_risk = 'Low risk'
                elif 25 <= bmi < 29.9:
                    category = 'Overweight'
                    health_risk = 'Moderate risk of developing heart disease and diabetes'
                elif 30 <= bmi < 34.9:
                    category = 'Obese Class I'
                    health_risk = 'High risk of developing heart disease and diabetes'
                elif 35 <= bmi < 39.9:
                    category = 'Obese Class II'
                    health_risk = 'Very high risk of developing heart disease and diabetes'
                else:
                    category = 'Obese Class III'
                    health_risk = 'Extremely high risk of developing heart disease and diabetes'

                flash('BMI calculated successfully!', 'success')
            else:
                error = "Height must be greater than zero."

    return render_template('index.html', 
                         bmi=bmi, 
                         category=category, 
                         error=error, 
                         health_risk=health_risk,
                         healthy_weight_range=healthy_weight_range,
                         bmi_prime=bmi_prime,
                         ponderal_index=ponderal_index)

if __name__ == "__main__":
    app.run(debug=True)