def SynchronizingTables(N: int, ids: list, salary: list):

    ids_sorted = sorted(ids.copy())
    salary_sorted = sorted(salary.copy())

    for i in range(N):
        salary[ids.index(ids_sorted[i])] = salary_sorted[i]

    return salary


