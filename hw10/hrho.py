import numpy as np
import time


def read_tsp(filename):
    ''' Reads a TSPLIB instance given by filename and returns the corresponding
    distance matrix C. Assumes that the edge weights are given in lower diagonal row
    form. '''

    f = open(filename,'r')

    n, C = 0, None
    i, j = -1, 0

    for line in f:
        words = line.split()
        if words[0] == 'DIMENSION:':
            n = int(words[1])
            C = np.zeros(shape=(n,n))
        elif words[0] == 'EDGE_WEIGHT_SECTION':
            i = 0 # Start indexing of edges
        elif i >= 0:
            for k in range(len(words)):
                if words[k] == 'EOF':
                    break
                elif words[k] == '0':
                    i += 1 # Continue to next row of the matrix
                    j = 0
                else:
                    C[i,j] = int(words[k])
                    C[j,i] = int(words[k])
                    j += 1

    return C


def traveling_salesman(C):
    '''
    Finds the shortest route that goes through all the given cities.

    C: a distance matrix between all possible combinations of two cities
    '''
    # get number of rows & columns of C
    num_rows, num_cols = C.shape

    # make a list of cities labeled [1, 2, ... ,n]
    cities = []
    for i in range(num_cols):
        cities.append(i+1)
    # print("Cities: ", cities)

    # initialize hashmap of visited status
    visit_status = {}
    for i in range(len(cities)):
        visit_status[i+1] = False
    # print("Visit Status: ", visit_status)

    # initialize queue/stack? to keep track of route
    route = []
    total_dist = 0

    # start at first city from cities & mark it visited
    route.append(cities[0])
    visit_status[cities[0]] = True

    # find the closest city each iteration and run until all the cities are visited
    # while False not in visit_status.values():
    while len(route) != len(cities):
        closest_dist = 100000.0
        closest_city = None

        # find the closest city
        for j in range(num_rows):
            # case when at C[i,i]
            if C[route[-1]-1][j] == 0:
                continue
            
            # case when unvisited, closer distance city is found
            if C[route[-1]-1][j] < closest_dist and visit_status[j+1] == False:
                closest_dist = C[route[-1]-1][j] 
                closest_city = j+1

        # add closest_dist to total_dist, add closest city to route, and mark it visited
        total_dist += closest_dist
        route.append(closest_city)
        visit_status[closest_city] = True
    
    # add the distance between the last city and the first city
    total_dist += C[route[-1]-1][route[0]-1]

    # return the total distance required for the route and the route
    return total_dist, route


def local_search_heuristic(total_dist, route, C):
    '''
    A local search heuristic algorithm on the traveling salesman problem.
    Improves the greedy approach taken in traveling_salesman()

    total_dist: the total distance required to go through the route calculated from traveling_salesman()
    route: a list that contains the order that the cities should be visited
    C: a distance matrix between all possible combinations of two cities
    '''
    # set optimized distance and route
    optimized_dist = 100000000000000000000.0
    optimized_route = []

    # remove all the cities one by one
    for i in range(len(route)-1):
        # start current_dist from total_dist for each city
        current_dist = total_dist
        current_route = route

        # print(i, len(route))
        # remove a city from route & subtract the distances to that removed city
        if i == (len(route)-1):
            current_dist -= C[current_route[i-1]-1][current_route[i]-1] + C[current_route[0]-1][current_route[i]-1]

        current_dist -= C[current_route[i-1]-1][current_route[i]-1] + C[current_route[i+1]-1][current_route[i]-1] # two edges get deleted when one city is removed
        removed_city = current_route[i]
        current_route.remove(current_route[i])
        # print(current_dist, route)

        # reinsert in best spot - go through all possible locations and find the shortest route
        for idx in range(len(route)):
            # insert removed_city at different idx
            current_route.insert(idx, removed_city)

            # add edges back again between city before and after that removed city
            current_dist += C[current_route[idx]-1][current_route[idx+1]-1] + C[current_route[idx]-1][current_route[idx-1]-1]
            # print(current_dist, current_route)

            # if the optimized distance is smaller than the total distance, update total distance
            if current_dist < optimized_dist:
                optimized_dist = current_dist
                optimized_route = current_route
            
            current_route.remove(current_route[idx])
        
        # add the removed_city back into the route
        current_route.insert(i, removed_city)

    # return the total distance required for the route and the route
    return optimized_dist, optimized_route


def get_runtime_traveling_salesman(C):
    ''' 
    Returns the total runtime of the traveling_salesman() algorithm

    C: a distance matrix between all possible combinations of two cities
    '''
    start_time = time.time()
    traveling_salesman(C)

    return time.time() - start_time


def get_runtime_local_search(C):
    ''' 
    Returns the total runtime of the local_search_heuristic() algorithm

    C: a distance matrix between all possible combinations of two cities
    '''
    dist, route = traveling_salesman(C)
    start_time = time.time()
    local_search_heuristic(dist, route, C)

    return time.time() - start_time


def get_optimality_gap(opt_soln, alg_soln):
    ''' 
    Finds the optimality gap of a solution derived by an algorithm.

    opt_soln: the optimal solution
    alg_soln: the solution output by the algorithm
    ''' 
    return abs(opt_soln - alg_soln)/opt_soln


def gr17():
    C_gr17 = read_tsp('gr17.tsp')
    total_d, tour = traveling_salesman(C_gr17)
    opt_total_dist, opt_route = local_search_heuristic(total_d, tour, C_gr17)

    get_runtime_traveling_salesman(C_gr17)
    get_runtime_local_search(C_gr17)
    print(get_optimality_gap(2085, opt_total_dist))


def gr21():
    C_gr21 = read_tsp('gr21.tsp')
    total_d, tour = traveling_salesman(C_gr21)
    opt_total_dist, opt_route = local_search_heuristic(total_d, tour, C_gr21)

    get_runtime_traveling_salesman(C_gr21)
    get_runtime_local_search(C_gr21)
    print(get_optimality_gap(2707, opt_total_dist))


def gr24():
    C_gr24 = read_tsp('gr24.tsp')
    total_d, tour = traveling_salesman(C_gr24)
    opt_total_dist, opt_route = local_search_heuristic(total_d, tour, C_gr24)

    get_runtime_traveling_salesman(C_gr24)
    get_runtime_local_search(C_gr24)
    print(get_optimality_gap(1272, opt_total_dist))


def gr48():
    C_gr48 = read_tsp('gr48.tsp')
    total_d, tour = traveling_salesman(C_gr48)
    opt_total_dist, opt_route = local_search_heuristic(total_d, tour, C_gr48)

    get_runtime_traveling_salesman(C_gr48)
    get_runtime_local_search(C_gr48)
    print(get_optimality_gap(5046, opt_total_dist))


if __name__ == "__main__":
    C = read_tsp('gr24.tsp')

    total_d, tour = traveling_salesman(C)
    # print(traveling_salesman(C))
    print(total_d)
    print(tour)

    print("===========")

    opt_total_dist, opt_route = local_search_heuristic(total_d, tour, C)
    # print(local_search_heuristic(total_d, tour, C))
    print(opt_total_dist)
    print(opt_route)

    #######
    # gr17()
    # gr21()
    # gr24()
    # gr48()
