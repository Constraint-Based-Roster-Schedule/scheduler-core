from ortools.sat.python import cp_model

'''
setting up the date for the problem. Different problem, different data. 
'''
nurse_num = 4
shift_num = 3
days_num = 3

# sort of an ID for each one. 
all_nurses = range(nurse_num) 
all_shifts = range(shift_num) 
all_days = range(days_num) 

#create model 
model = cp_model.CpModel() 

'''
    problem: representing a solution 
    solution: solution is a set of tuples where (n,d,s) = 1 if nth nurse is assigned to sth shift on dth day.
'''
shifts = {}
for n in all_nurses :
    for d in all_days :
        for s in all_shifts : 
            shifts[(n,d,s)] = model.NewBoolVar('shift_n%id%is%i' % (n, d, s))

'''
    now we add constraints
'''

#constraint: only one nurse per shift everyday

for d in all_days :
    for s in all_shifts : 
        model.AddExactlyOne(shifts[(n,d,s)] for n in all_nurses) 

#constraint: at most one shift per nurse per day 

for n in all_nurses :
    for d in all_days : 
        model.AddAtMostOne(shifts[(n,d,s)] for s in all_shifts)

#assign shifts evenly. each should have less than maximum and more than minimum

total_shifts = shift_num*days_num
minimum_shifts = total_shifts//nurse_num 

if total_shifts%nurse_num == 0 :
    maximum_shifts = minimum_shifts 
else :
    maximum_shifts = minimum_shifts + 1 

for n in range(nurse_num):
    shifts_total = [] 
    for d in all_days :
        for s in all_shifts : 
            shifts_total.append(shifts[(n,d,s)])

    model.Add(minimum_shifts <= sum(shifts_total))
    model.Add(maximum_shifts >= sum(shifts_total))

print(model.ModelStats() + "\n") 
solver = cp_model.CpSolver() 
solver.parameters.linearization_level = 0
solver.parameters.enumerate_all_solutions = True 


class NursesPartialSolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, shifts, num_nurses, num_days, num_shifts, limit):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self._shifts = shifts
        self._num_nurses = num_nurses
        self._num_days = num_days
        self._num_shifts = num_shifts
        self._solution_count = 0
        self._solution_limit = limit

    def on_solution_callback(self):
        self._solution_count += 1
        print('Solution %i' % self._solution_count)
        for d in range(self._num_days):
            print('Day %i' % d)
            for n in range(self._num_nurses):
                is_working = False
                for s in range(self._num_shifts):
                    if self.Value(self._shifts[(n, d, s)]):
                        is_working = True
                        print('  Nurse %i works shift %i' % (n, s))
                if not is_working:
                    print('  Nurse {} does not work'.format(n))
        if self._solution_count >= self._solution_limit:
            print('Stop search after %i solutions' % self._solution_limit)
            self.StopSearch()

    def solution_count(self):
        return self._solution_count

# Display the first five solutions.
solution_limit = 5
solution_printer = NursesPartialSolutionPrinter(shifts, nurse_num,
                                                days_num, shift_num,
                                                solution_limit)

solver.Solve(model, solution_printer) 
