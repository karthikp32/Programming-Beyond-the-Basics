import urllib.request
import time

#Higher-order functions can take in other functions as input or output
#Lower-order functions can work with basic data types like integers, strings, etc. as input and output

def fetch_without_cache(url):
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        return content

def fetch_with_cache(url, url_content):
    if url in url_content:
        return url_content[url]
    else:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            url_content[url] = content
            return content

def fib_without_cache(n):
    if n <= 1:
        return n
    return fib_without_cache(n - 1) + fib_without_cache(n - 2)


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


def function_with_caching(function, *args):
    cache = {}
    if args[0] in cache:
        return cache[args[0]]
    else:
        modified_args = list(*args)
        modified_args.append(cache)
        answer = function(*args)
        cache[args[0]] = answer
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
    # print(fetch_with_cache('http://google.com', url_content)[:80])

    # print(function_with_caching(fetch_without_cache, 'http://google.com')[:80])

    cache = {}
    # print(fib(3, cache))
    # print(fib(5, cache))
    # print(fib(15, cache))

    # print(function_with_caching(fib, 3))
    # print(function_with_caching(fib, 5))
    # print(function_with_caching(fib, 15))

    print("fibonacci without caching:")
    time_function(fib_without_cache, 15)
    print("fibonacci with caching:")
    time_function(fib_with_cache, 15, cache)