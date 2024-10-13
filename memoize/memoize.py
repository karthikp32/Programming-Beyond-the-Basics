import urllib.request
import time

#Higher-order functions can take in other functions as input or output
#Lower-order functions can work with basic data types like integers, strings, etc. as input and output

def fetch(url):
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        return content

def fetch_with_cache(url, cache):
    if url in cache:
        return cache[url]
    else:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            cache[url] = content
            return content

def create_cached_version_of_function(function,function_cache, *args):
    input = args[0]
    if input not in function_cache:
        function_cache[input] = function(*args)
    output = function_cache[input]
    return output


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_with_cache(n, cache):
    if n in cache:
        return cache[n]
    else:
        if n <= 1:
            cache[n] = n 
            return n
        answer = fib_with_cache(n - 1, cache) + fib_with_cache(n - 2, cache)
        cache[n] = answer
        return answer

def time_function(function, *args):
    # Time the execution
    start = time.time()
    function(*args)
    end = time.time()
    print(f"Execution time: {end - start} seconds")       

def multiply(a, b):
    answer = 0
    for _ in range(0, b):
        answer += add(a, a)


if __name__ == '__main__':
    url_content = {}
    print(fetch_with_cache('http://google.com', url_content)[:80])

    # print(function_with_caching(fetch_without_cache, 'http://google.com')[:80])

    # cache = {}
    # print(fib(3, cache))
    # print(fib(5, cache))
    # print(fib(15, cache))

    # print(function_with_caching(fib, 3))
    # print(function_with_caching(fib, 5))
    # print(function_with_caching(fib, 15))

    # print("fibonacci without caching:")
    # time_function(fib, 15)
    # print("fibonacci with caching:")
    # time_function(fib_with_cache, 15, cache)

    function_cache = {}

    start = time.time()
    output = create_cached_version_of_function(fetch,function_cache,'http://google.com' )
    end = time.time()
    print(f"Execution time: {end - start} seconds. Output is {output}")       


    start2 = time.time()
    output = create_cached_version_of_function(fetch, function_cache,'http://google.com'  )
    end2 = time.time()
    print(f"Execution time of 2: {end2 - start2} seconds.  Output is {output}")  

    start3 = time.time()
    output = create_cached_version_of_function(fetch, function_cache,'http://google.com'  )
    end3 = time.time()
    print(f"Execution time of 3: {end3 - start3} seconds.  Output is {output}")  

    start4 = time.time()
    output = create_cached_version_of_function(fib,function_cache,13)
    end4 = time.time()
    print(f"Execution time of 4: {end4 - start4} seconds.  Output is {output}")       


    start5 = time.time()
    output = create_cached_version_of_function(fib, function_cache,13 )
    end5 = time.time()
    print(f"Execution time of 5: {end5 - start5} seconds. Output is {output}")  

    start6 = time.time()
    output = create_cached_version_of_function(fib, function_cache,13 )
    end6 = time.time()
    print(f"Execution time of 6: {end6 - start6} seconds.  Output is {output}")  


