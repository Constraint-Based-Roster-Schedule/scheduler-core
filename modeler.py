from ortools.sat.python import cp_model 

class ParameterHolder :
    def __init__(self, days, shifts, doctors, shift_capacity, shift_limit ) :
        self.days = days
        self.shifts = shifts
        self.doctors = doctors 
        self.shift_capacity = shift_capacity    # doctors per shift
        self.shift_limit = shift_limit          # upper limit for shifts per doctors in a month
    
def create_model (self, parameters:ParameterHolder, model: cp_model.CpModel ) -> cp_model.CpModel: 

    doctor_ls = range (parameters.doctors)
    shifts_ls = range (parameters.shifts)
    days_ls = range (parameters.days)

    # Define the solution format

    shifts = {}
    for n in doctor_ls :
        for d in days_ls :
            for s in shifts_ls : 
                shifts[(n,d,s)] = model.NewBoolVar('shift_n%id%is%i' % (n, d, s))

    # Adding Constraints to the schdeuler

    ### Doctors per shift
    