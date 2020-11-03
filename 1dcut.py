total_length = 25 #długość drutu
cuts = [8, 5, 3, 2, 1] #możliwe rozkroje
solutions = [[3, 0, 0, 0, 1]] #pierwsze rozwiązanie
 
#funkcja do obliczenia tego ile już drutu wykorzystaliśmy
def count_used_length(index, amounts):
        used_len = 0
        for i in range(index+1):
                used_len += cuts[i]*amounts[i]
        return used_len
 
def find_new_solution():
        next_solution = solutions[-1].copy()
        i=3
        while next_solution[i]==0:
                i -=1
        next_solution[i]-=1
        i+=1
        while i!=5:
                remaining_length = total_length - count_used_length(i-1, next_solution)
                next_solution[i] = remaining_length//cuts[i]
                i+=1
 
        #sprawdzamy czy na pewno mamy unikalne rozwiązanie
        if not next_solution in solutions:
                solutions.append(next_solution)
 
for j in range(500):
        find_new_solution()
print(len(solutions)) #sprawdzamy ile znaleźliśmy rozwiązań
for solution in solutions:
        print(solution)
 
print()
print()
 
#sprawdzamy czy wszystkie rozwiązania używają całej długości (bo powinny)
for solution in solutions:
        if sum(x * y for x, y in zip(solution, cuts))!=total_length:
                print(solution)
