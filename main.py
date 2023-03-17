# python3

def parallel_processing(n, m, data):
    output = []
    # write the function for simulating parallel tasks, 
    # create the output pairs

    # izveido virkņu sarakstu, lai sekotu pavedienu apstrādes laikam un pavedienu indeksam
    threads = [(0, i) for i in range(n)]

    #iziet cauri katram darbam
    for i in range(m):
        # saņem darba apstrādes laiku
        job_time = data[i]

        # atrod pavedienu ar vismazāko apstrādes laiku
        next_thread = min(threads)

        # pievieno izvadei pavediena indeksu un sākuma laiku
        output.append((next_thread[1], next_thread[0]))

        # atjaunina apstrādes laiku izvēlētajam pavedienam
        threads.remove(next_thread)
        threads.append((next_thread[0] + job_time, next_thread[1]))
        
    return output

def main():
    # create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count

    n, m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    data = list(map(int, input().split()))

    # create the function
    result = parallel_processing(n,m,data)
    
    # print out the results, each pair in it's own line
    for i in range(m):
        print(result[i][0], result[i][1])


if __name__ == "__main__":
    main()
