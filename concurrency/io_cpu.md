## I/O vs CPU Bound

A program can be judged depending on whether the predominant resource required is Input Output or CPU.

For example, calculating a fibonacci number is CPU intensive task.
Waiting on network I/O is a I/O task, as it can always take some time to return the response. This does not hog CPU, while the former does.

Different languages have different implementation of threading and concurrency, which works in a different manner, as we discussed in concurrency and parallelism.