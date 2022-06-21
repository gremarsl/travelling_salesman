import itertools


'''
   |  1   2    3  |
------------------|
 1 | 0  | 4  | 1  |
 2 | 4  | 0  | 3  |
 3 | 1  | 2  | 0  |
-------------------

How to read the matrix:
The distance from 1 (line) to 3 (column) is 1. 
The first line and the first column of this matrix is dedicated to the Nodes 1,2,3
'''

distance_matrix = [
    [0, 1, 2, 3],
    [1, 0, 4, 1],
    [2, 4, 0, 2],
    [3, 1, 2, 0]]


def distance_among_two_nodes(n1, n2):
    """
    :param n1: Node1
    :param n2: Node2
    :return: Distance between Node1 and Node2
    """

    print(f'Distance from {n1} to {n2} is: {distance_matrix[n1][n2]}')
    return distance_matrix[n1][n2]


def recursive_node(position, number_of_nodes_left):
    """

    :param position: Current position on the path based on the array
    :param number_of_nodes_left: For recursive reasons, this parameter is passed to now how many node positions we have to go
    :return: This function returns a distance.
    """

    array_position_start = nodes_to_reach[position]
    array_position_end = nodes_to_reach[position + 1]

    global distance

    # reduce number of nodes left by one
    number_of_nodes_left -= 1

    if number_of_nodes_left == 1:
        print(f'Distance is 0')
        return 0  # since distance from c to c is 0

    else:
        # start from nodes_to_reach[1:] since first element to be ignored. #TODO Improvement possible
        for node in nodes_to_reach[1:]:
            # print(f'Node: {node}')
            distance = distance_among_two_nodes(array_position_start, array_position_end) + recursive_node(node + 1,number_of_nodes_left)

            return distance


def get_second_element_from_array(A):
    """
    :param A: Array [x,y,z,...]
    :return:
    """
    return A[1]


def convert_tuple_to_list(T):
    return list(T)


def add_zero_to_list(L):
    return [0] + L


if __name__ == '__main__':

    # START PREPARING

    global nodes_to_reach
    nodes_to_reach = [0, 1, 2, 3]  # 0 only for dummy to improve understanding. #TODO improvements possible

    # return_distances array is supposed to contain the calculated paths and their length e.g. [[6, [0, 1, 2, 3]], [3, [0, 1, 3, 2]]]
    return_distances = []

    # create permutation: #TODO possible abstraction in separate func
    # start node is always 1 -> so start from index 2
    nodes_to_reach = list(itertools.permutations(nodes_to_reach[1:]))

    # filter all lists not starting with 1
    permutations = list(filter(lambda nodes_to_reach: nodes_to_reach[0] == 1, nodes_to_reach))

    # because tuples are immutable -> we need to transform the tuples in a list
    possible_paths_to_go = list(map(convert_tuple_to_list, permutations))

    print(possible_paths_to_go)
    nodes_to_reach = possible_paths_to_go[0]

    # add 0 again

    all_list_permutations = list(map(add_zero_to_list, possible_paths_to_go))

    print(
        f"According to the Node array with the nodes: {nodes_to_reach}, these are all permutations: {all_list_permutations}")
    nodes_to_reach = all_list_permutations[0]

    # STOP PREPARING
    print("###")

    # START PERMUTATION CALCULATION
    for n in all_list_permutations:
        global distance
        distance = 0
        nodes_to_reach = n

        # for testpurpose since first array works:
        # nodes_to_reach = [0, 1, 3, 2]

        return_distance = recursive_node(nodes_to_reach[1], 4)
        return_distances.append([nodes_to_reach] + [return_distance])

    # STOP PERMUTATION CALCULATION

    # START RESULT EXTRACTION
    print(return_distances)
    shortest_path_list = list(map(get_second_element_from_array, return_distances))

    # find minimum
    shortest_length = min(shortest_path_list)

    print(f'Shortest path has length: {shortest_length}')

    # STOP RESULT EXTRACTION

