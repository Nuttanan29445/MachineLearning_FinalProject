import PySimpleGUI as sg

# Add a touch of color
sg.theme('DarkAmber')

# Prepare Lst
optionsLst = [f'Option {i}' for i in range(1, 11)]
columns = ['Price', 'Levy', 'Manufacturer', 'Model', 'Prod_year', 'Category',
           'Leather_interior', 'Fuel', 'Engine_volume', 'Mileage', 'Gear_box', 'Drive_wheels', 'Doors', 'Wheel', 'Color',
           'Airbags']
translate = ['ราคา', 'ค่าธรรมเนียม', 'ผู้ผลิตรถยนต์', 'รุ่นรถยนต์',
             'ปีที่ผลิต', 'หมวดหมู่รถยนต์', 'เบาะนั่งเป็นหนัง', 'ชนิดเชื้อเพลง', 'ความแรงเครื่องยนต์', 'ระยะทางสะสม', 'ชนิดของเกียร์', 'ขับเคลื่อนกี่ล้อ', 'จำนวนประตูรถ', 'ล้อ', 'สีรถยนต์', 'ถุงลมนิรภัย']
Price = [941.0, 45.0, 31248.0, 4234.0,
         37000.0, 11917.0, 39750.0, 8000.0, 10036.0]
Levy = [584.0, 779.0, 751.0, 779.0, 891.0, 779.0, 730.0, 779.0, 779.0]
Manufacturer = ['HYUNDAI', 'HONDA', 'JEEP', 'TOYOTA',
                'HYUNDAI', 'TOYOTA', 'SSANGYONG', 'MITSUBISHI', 'BMW']
Model = ['Elantra', 'FIT', 'Compass', 'Camry',
         'Tucson', 'Prius', 'Actyon', 'Colt', '320 DIESEL']
Prod_year = [2014.0, 2007.0, 2013.0, 2013.0,
             2016.0, 2007.0, 2016.0, 2006.0, 2002.0]
Category = ['Sedan', 'Hatchback', 'Jeep', 'Sedan',
            'Jeep', 'Sedan', 'Jeep', 'Hatchback', 'Sedan']
Leather_interior = ['Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No']
Fuel = ['Petrol', 'Petrol', 'Petrol', 'Hybrid',
        'Diesel', 'Hybrid', 'Diesel', 'Petrol', 'Diesel']
Engine_volume = [1.8, 1.3, 2.4, 2.5, 2.0, 1.5, 1.6, 1.5, 2.0]
Mileage = [101526.0, 87000.0, 59897.0, 26918.0,
           80000.0, 318400.0, 72000.0, 169969.0, 280000.0]
Gear_box = ['Automatic', 'Automatic', 'Automatic', 'Automatic',
            'Automatic', 'Automatic', 'Automatic', 'Automatic', 'Manual']
Drive_wheels = ['Front', 'Front', 'Front', 'Front',
                'Front', 'Front', 'Front', 'Front', 'Rear']
Doors = ['4-5', '4-5', '4-5', '4-5', '4-5', '4-5', '4-5', '4-5', '4-5']
Wheel = ['Left wheel', 'Right-hand drive', 'Left wheel', 'Left wheel',
         'Left wheel', 'Left wheel', 'Left wheel', 'Right-hand drive', 'Left wheel']
Color = ['Silver', 'Black', 'White', 'White',
         'Silver', 'Sky blue', 'Red', 'Silver', 'Black']
Airbags = [12, 5, 4, 12, 4, 5, 4, 2, 8]
options = [Price, Levy, Manufacturer, Model, Prod_year, Category,
           Leather_interior, Fuel, Engine_volume, Mileage,
           Gear_box, Drive_wheels, Doors, Wheel, Color,
           Airbags]

# Prepare Layout
inputs = [[sg.Text(c + f" ({translate[i]})"), sg.Input(f"Input_{i + 1}", s=(30, 1), disabled=True,
                                                       use_readonly_for_disable=False, k=f'_{c.upper()}_')] for i, c in enumerate(columns)]

inputs_textfield = [sg.Text(c + f" ({translate[i]})")
                    for i, c in enumerate(columns)]

inputs_label = [sg.Input(f"Input_{i + 1}", s=(30, 1), disabled=True,
                         use_readonly_for_disable=False, k=f'_{c.upper()}_') for i, c in enumerate(columns)]

# All the stuff inside window.
layout = [[sg.Text('Car Price Prediction')],
          [sg.Combo(optionsLst, size=(30, 20), enable_events=True)],
          inputs,
          [sg.Button('Predict', pad=(200, 20))],
          [sg.Button('Ok'), sg.Button('Cancel')]
          ]

# Create the Window
window = sg.Window('Window Title', layout, size=(500, 600), font=24)


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    option_selected = int(values[0].split(" ")[1]) - 1

    # Options Selected
    if event == 0:
        for i, c in enumerate(columns):
            window.Element(f'_{c.upper()}_').Update(
                options[i][option_selected])

    if event == 'Predict':
        for i in range(len(options)):
            print(options[i][option_selected])


window.close()
