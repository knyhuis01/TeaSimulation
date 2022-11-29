class teaMug:
    """Represents amount of tea in a mug."""

tea = teaMug()

tea.color = "purple"
tea.size = "10 oz"
tea.shape = "heart"
tea.amount = 10

import math
def tea_drinking_simulation(t, time):
    tea_left = t.amount - 3*time #considering it takes one minute to drink three ounces
    result = "My %s, %s, %s mug has"%(t.color,t.size,t.shape),tea_left,"oz left after", time,"minutes"
    print(result)


tea_drinking_simulation(tea,3)
