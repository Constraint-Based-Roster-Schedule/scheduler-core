from ortools.sat.python import cp_model 

class ParameterHolder :
    '''
        Class for holding the parameters of the model

        :param days: number of days of roster month
        :type days: int

        :param shifts: number of shifts in a day
        :type shifts: int 

        :param doctors: number of doctors in the roster
        :type doctors: int

        :param shift_capacity: number of doctors per shift
        :type shift_capacity: int

        :param shift_limit: number of shifts allowed per doctor
        :type shift_limit: int 
        
    '''
    def __init__(self, days, shifts, doctors, shift_capacity, shift_limit ) :
    
        self.days = days
        self.shifts = shifts
        self.doctors = doctors 
        self.shift_capacity = shift_capacity
        self.shift_limit = shift_limit
    
def create_model (self, parameters:ParameterHolder ) -> cp_model.CpModel: 
    '''
        Requires a parameterHolder object and a CpModel object and returns a CpModel object. 

        :param parameters: ParameterHolder object holding the parameters. 
        :return: CpModel object 
    
    '''
    
    doctor_ls = range (parameters.doctors)
    shifts_ls = range (parameters.shifts)
    days_ls = range (parameters.days)
    
    model = cp_model.CpModel()

    # Define the solution format

    shifts = {}
    for n in doctor_ls :
        for d in days_ls :
            for s in shifts_ls : 
                shifts[(n,d,s)] = model.NewBoolVar('shift_n%id%is%i' % (n, d, s))

    # Adding Constraints to the schdeuler

    ### Doctors per shift
    