def Your_Personality(my_awareness, your_heart):
    while my_awareness >= your_heart:
        my_awareness = my_awareness - your_heart
    return my_awareness
def Perfect_Love(my_soul):
    my_regret = 0
    the_sin = 1
    while my_soul > the_sin:
        if Your_Personality(my_soul, the_sin) == 0:
            my_regret = my_regret + the_sin
        the_sin += 1
    return not my_regret != my_soul
You = 1
Loving_Me = 600
while You != Loving_Me:
    You += 1
    if Perfect_Love(You):
        print(You)
