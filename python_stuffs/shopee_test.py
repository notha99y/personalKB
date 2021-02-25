import time
L = [(1, 3), (2, 3), (1, 4), (3, 4), (4, 6), (5, 6),(4,7)]
N = 7


def show_parallel_tasks(task_list, tot_num_tasks):
    '''Show tasks that can be done in parallel
    Strategy:
    - Find out which tasks can be done without dependencies.
    - Do them
    - Update the tasks as done
    - Repeat
    '''
    res = dict()
    done_tasks = []
    done_previous = []
    count = 1
    while len(done_tasks) < tot_num_tasks:
        print(count)
        time.sleep(0.5)
        non_dep = get_non_dependent_tasks(task_list, done_tasks, tot_num_tasks)
        print('non_dep: ', non_dep)

        for task in non_dep:
            if task in done_tasks:
                continue

            done_tasks.append(task)
        done_this_round = [
            task for task in done_tasks if task not in done_previous]
        done_previous = done_tasks[:]
        print('done_tasks: ', done_tasks)
        res[count] = done_this_round
        count += 1
    return res


def get_non_dependent_tasks(task_list, done_tasks, tot_num_tasks):
    '''Returns a list of non dependent tasks.
    Strategy:
    - For each task
    - Checks if it is dependent
    - take complement
    '''
    dep_tasks = []
    for task in range(1, tot_num_tasks+1):
        if task in done_tasks:
            continue
        dep = False
        for task_tup in task_list:
            if task == task_tup[1] and task_tup[0] not in done_tasks:
                dep = True
            if dep:
                dep_tasks.append(task)
    dep_tasks = list(set(dep_tasks))
    print('dep: ', dep_tasks)
    non_dep = [task for task in range(
        1, tot_num_tasks+1) if task not in dep_tasks]
    return non_dep


if __name__ == "__main__":
    print('L: ', L)
    res = show_parallel_tasks(L, N)
    print(res)
