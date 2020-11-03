#To cutomize the code to your specific settings edit the three lines below.
total_length = 25 #rod length
cuts = [8, 5, 3, 2, 1] #possible piece lengths
#first solution is added by hand to bootstrap the possible cut finding algorithm
#to generate the first solution add as many longest pieces as possible and then as many 2nd longest pieces etc.
#for cuts = [13,5,3,2] the first solution would be [1, 2, 0, 1] (1 13-piece, 2 5-pieces, finally 1 2-piece to sum up to 25)
solutions = [[3, 0, 0, 0, 1]] #TODO: make a function to find the first solution so it doesn't have to be put in manually
 
#counting how much of the rod has been used up so far
def count_used_length(index, amounts):
        used_len = 0
        for i in range(index+1):
                used_len += cuts[i]*amounts[i]
        return used_len
 
def find_new_solution():
        next_solution = solutions[-1].copy()
        i=len(cuts)-2
        while next_solution[i]==0:
                i -=1
        next_solution[i]-=1
        i+=1
        while i!=5:
                remaining_length = total_length - count_used_length(i-1, next_solution)
                next_solution[i] = remaining_length//cuts[i]
                i+=1
 
        #check if the new solution is a new one for sure
        if not next_solution in solutions:
                solutions.append(next_solution)
 
for j in range(500):
        find_new_solution()
print(len(solutions)) #check how much soultions have been found
for solution in solutions:
        print(solution)
 
print()
print()
 
#check if all of the solutions use up the total lenght, this is always the case if a 1-piece is available, isn't guaranteed otherwise.
for solution in solutions:
        if sum(x * y for x, y in zip(solution, cuts))!=total_length:
                print(solution)
