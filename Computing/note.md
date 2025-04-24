git status
status of repo (that's being tracked), changed show up to date with origin

git add README.MD
prepares file to be committed(staged)


git commit -m "hello world"
adds a new commit to the local repo with message as its label


git pull
download updates from remote repo and merges them locally, may cause merge confliced


git push
add commits from local to the remote repo


that is a commit?
snapshot of changes made to your repo commit ID


Git | Github diff

Git 
offline, local use 
CLI 
VCS

Github
online(cloud)
GUI
platform that hosts git repos and adds funtionality (dev community, portfolio site, issues, pull request)


whats is branch?

why do we write unit tests?
testing code boundaries written yourself validate changes/ logic

why are they called unit tests?
test code as isolated pieces


what does 'self.assertEquals(...)' do?
2 args (expected, actual), comparing for equality


whats does it mean to "mock"/"patch" in unit testing?
mimick a resource(and its functionality)
focus testing on that isolated unit


what does Big-O complexity explain?
worst-case runtime of an algorithm

why can we simplify computation 4n^2 + 20n + 10000 to be O(n^2)?
runtime, we care as n -> infite, when that happens, constant multipliers and lower order terms are negligible.

```python
def f(n): # O(n^2)
    for i in range(n): # n
        for j in range(0,n,2): # n/2
            print('hi') # constant
```


```python
def f(n): # O(n^1/3)
    for i in range(int(n ** (1/3))):
        print('hi') # constant
```


```python 
for i in range(n ** 4): # O(1)
    print('hi')
    break
```

```python
def f(n): # O(n ^ 5/2)
    for i in range(int(n ** (1/2))): # n ^ 1/2
        for j in range(n / 2): # n / 2
            for k in range(n): # n
                print("hi") # 1

# n^2 / 2 * n^1/2 = (n^2 * n^0.5)/2 -> O(n^2.5)
```

```python
# if n is even, constant runtime
# if n is odd, n^2 runtime
if n % 2 == 0: 
    return True

for i in range(n):
    for j in range(n):
        print('*')
```


O(1) O(log(n)) O(sqrt(n)) O(n) O(nlogn) O(n^2) O(n^k) O(k^n)


What is an API?
interface/framework that has a specific request/response structure with define functionality

How dos a route work for a Flask server?
PUT / beer-company, connects request to its specific code



What is the point of 'debug = True' when establishing a flask server?
exposes the call stack for exception lagging, server is running locally.


What is a 'Resource' in Flask? How is it used for a project?
class that contains the business lofic of an API.


What are the FOUR common request methods for a Rest API?
GET, POST, PUT, DELETE

Status Codes
404 Resource not found
200 Success ok
400 Bad input
403 Forbidden access deny


Describe http://127.0.0.1:5000
port 5000 running on your localhost(your PC)
