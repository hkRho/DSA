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

    # return the total distance required for the route and the route
    return total_dist, route


def local_search_heuristic(total_dist, route):
    '''
    A local search heuristic algorithm on the traveling salesman problem.
    Improves the greedy approach taken in traveling_salesman()

    total_dist: the total distance required to go through the route calculated from traveling_salesman()
    route: a list that contains the order that the cities should be visited
    '''
    # remove random city from route


    # build connection/edge between city before and after that removed city

    ## reinsert in best spot
    # go through all possible edges and find the shortest route


if __name__ == "__main__":
    C = read_tsp('gr24.tsp')
    # print(C)

    total_d, tour = traveling_salesman(C)
    # print(traveling_salesman(C))
    print(total_d)
    print(tour)