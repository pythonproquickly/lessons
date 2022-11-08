my_list = [1.1, 0.3, 0.6]
for element in my_list:
    try:
        print("The element is:", element)
        reciprocal = 1 // int(element)
        print(reciprocal)
    except ZeroDivisionError as e:
        print("Oops!!!")

vaccinations = [
    {"iso": "ALB", "vacc": "Pfizer, Sinovac",
     "vacc months": ["Jan", "Feb", "Mar", "May"],
     "vacc counts": [549, 6728, 110015, 650001]},
    {"iso": "FRO", "vacc": "Moderna, Pfizer",
     "vacc months": ["Apr"], "vacc counts": [15531]},
    {"iso": "VEN", "vacc": "Sputnik V",
     "vacc months": ["Feb", "Apr", "May", "Jun"],
     "vacc counts": [157, 10770, 316015, 620437]},
    {"iso": "ZMB", "vacc": "Oxford",
     "vacc months": ["Jun"], "vacc counts": [148304]}
]
