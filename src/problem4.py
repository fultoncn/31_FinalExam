"""
Final exam, problem 4.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Colleen.  May 2018.

"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# DONE: 2.
#   In this problem, you will go through the methods of the  Pig  class
#   that is defined below, one by one, in the order that they appear.
#   For each method:
#      (a) Read the method's doc-string (i.e., specification in double-quotes).
#            If you do not understand WHAT the method is to do,
#            ask your instructor to clarify it.
#      (b) Implement the method.
#      (c) Write at least SOME code  in  main  that tests your code.
#
###############################################################################

def main():
    """ Tests the  Pig  class. """
    # -------------------------------------------------------------------------
    # WRITE CODE HERE AS NEEDED to TEST the code that you write
    #   in the  Pig  class.  At the least, you must:
    #     -- Construct two Pig objects
    #     -- Call each method that you implement below.
    # -------------------------------------------------------------------------

    # To get weight
    p1 = Pig(5)
    print('Starting Weight:', p1.get_weight(), 'lbs')
    # Add in the weight of food
    weight_of_food = 1
    print('Weight after Eating:', p1.eat(weight_of_food), 'lbs')
    print('Weight after year:', p1.eat_for_a_year(), 'lbs')
    other_pig = 66500
    print('The heavier pig weighs:', p1.heavier_pig(other_pig), 'lbs')
    print('The new pig weighs:', p1.new_pig(other_pig), 'lbs')


class Pig(object):
    def __init__(self, weight):
        """
        What comes in:  The Pig's weight (in pounds).
        Side effects: Sets instance variables as needed by the other methods.
        """
        # DONE: Implement and test this method.
        self.weight = weight

    def get_weight(self):
        """ Returns this Pig's weight. """
        # DONE: Implement and test this method.
        return self.weight

    def eat(self, pounds_of_slop):
        """
        Increments this Pig's weight by the given pounds_of_slop.
        """
        # DONE: Implement and test this method.
        return self.weight + pounds_of_slop

    def eat_for_a_year(self):
        """
        Calls the   eat   method as many times as needed to make this Pig:
          -- eat 1 pound of slop, then
          -- eat 2 pounds of slop, then
          -- eat 3 pounds of slop, the
          -- eat ... [4 pounds, then 5, then 6, then ... ]
          -- eat 364 pounds of slop, then
          -- eat 365 pounds of slop.
        """
        # DONE: Implement and test this method.
        total_slop = 0
        for k in range(365):
            slop_day = (k+1)
            # print(slop_day)
            total_slop = total_slop + slop_day
            # print(total_slop)
        return self.eat(total_slop)

    def heavier_pig(self, other_pig):
        """
        Returns either this Pig object or the other given Pig object,
        whichever is heavier.
        """
        # DONE: Implement and test this method.
        if self.eat_for_a_year() > other_pig:
            return self.eat_for_a_year()
        else:
            return other_pig

    def new_pig(self, other_pig):
        """
        Returns a new Pig whose weight is the weight of the heavier
          of this Pig and the other_Pig.
        """
        # DONE: Implement and test this method.
        max_weight = self.heavier_pig(other_pig)
        return max_weight


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
