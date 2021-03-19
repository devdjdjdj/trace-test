def problem_2_function(dataset, 
                       dimensions, 
                       depth, 
                       measure_col_tuple, 
                       metric_func, 
                       threshold_func):
    
    # depth : The max number of combinations for each dimension
    # For example:
    # d1 - {x,y}
    # d2 - {a,b,c}
    #
    # depth = 1 - Following combinations will be worked on
    #
    # 0x0 - (,)
    # 1x0 - (x,), (y,)
    # 0X1 - (,a), (,b), (,c)
    # 1x1 - (x,a), (y,a),(x,b) (y,b),(x,c), (y,c) 
    #
    # depth = 2 - Following combinations will be worked on
    #
    # 0x0 - (,)
    # 1x0 - (x,), (y,)
    # 0X1 - (,a), (,b), (,c)
    # 1x1 - (x,a), (y,a),(x,b) (y,b),(x,c), (y,c) 
    # 2x1 - (xy,a), (xy,b), (xy,c)
    # 1x2 - (x,ab), (x,bc), (x,ac), (y,ab), (y,bc), (y,ac)
    # 2x2 - (xy,ab), (xy,bc), (xy, ac)
    
    excluded_combinations = dict()
    result = dict()
    for d in range(0,depth+1):
        excluded_combinations_at_depth = set()
        combinations = get_combinations(dataset, 
                                        dimensions, 
                                        d,
                                        excluded_combinations)
        result_at_depth = initialize_result_matrix(combinations)
        for combination in combinations:
            if not is_a_subset(combination, excluded_combinations):
                if threshold_func(dataset, combination):
                    #Meets threshold
                    result_at_depth[combination] = metric_func(dataset, 
                                                               combination, 
                                                               measure_col_tuple)
                else:
                    excluded_combinations_at_depth.add(combination)
        excluded_combinations[d] = excluded_combinations_at_depth
        result[d] = result_at_depth
    return result

def metric_function(dataset, 
                    filters, 
                    measure_col_tuple):
    filtered_dataset = apply_filter(dataset, 
                                    filters)
    measure_1 = measure_col_tuple[0]
    measure_2 = measure_col_tuple[1]
    numerator = sum(filtered_dataset[measure_1])
    denominator = sum(filtered_dataset[measure_2])
    try:
        ratio = numerator/denominator
    except ZeroDivisionError as e:
        ratio = INFINITE_VALUE 
    finally:
        return ratio

def threshold_function(dataset,
                       filters):
    THRESHOLD = 9876 #Some number
    filtered_dataset = apply_filter(dataset, 
                                    filters)
    meets_threshold = count(filtered_dataset) >= THRESHOLD
    return meets_threshold

# Functions to be defined: 
# apply_filter(dataset, filters)
# get_combinations(dataset, dimensions, depth, excluded_combinations)
# initialize_result_matrix(combinations)
# is_a_subset(combination, excluded_combinations)
# count(filtered_dataset)


# Run the function:
problem_2_function(dataset, 
                   ('d1', 'd2', 'd3'), 
                   1, 
                   ('m1', 'm2'), 
                   metric_function, 
                   threshold_function)