from tkinter import *

screen = Tk()
screen.title("Calculate BMI")
screen.minsize(width=300, height=150)
screen.config(background="light yellow")


def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()

    if weight == "" or height == "":
        result_label.config(text="Enter Both Weight And Height")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string=write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter A Valid Number")


# user
weight_input_label = Label(text="Enter Your Weight(Kg)")
weight_input_label.pack()

weight_input = Entry()
weight_input.pack()

height_input_label = Label(text="Enter Your Height (Cm)")
height_input_label.pack()

height_input = Entry(width=10)
height_input.pack()

calculate_button = Button(text="Calculate", command=calculate_bmi)
calculate_button.pack()

result_label = Label()
result_label.pack()


def write_result(bmi):
    result_string = f"Your Bmi İs {round(bmi,2)}. You Are "
    if bmi <= 16:
        result_string += "Severly Thin"
    elif 16 < bmi <= 17:
        result_string += "Moderately Thin"
    elif 17 < bmi <= 18.5:
        result_string += "Mild Thin"
    elif 18.5 < bmi <= 25:
        result_string += "Normal"
    elif 25 < bmi <= 30:
        result_string += "Overweight"
    elif 30 < bmi <= 35:
        result_string += "Obese Class 1"
    elif 35 < bmi <= 40:
        result_string += "Obese Class 2"
    elif bmi > 40:
        result_string += "Obese Class 3"
    return result_string


mainloop()
