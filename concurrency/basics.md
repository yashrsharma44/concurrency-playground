# Concurrency

## Features of Concurrency
* Higher Throughput - CPU utilization is maximum
* Responsive Applications - Feels like breeze to work with
* Effective Utilization of resources


## Issues of Multithreading in Python

When we generally run our applications in Python using the multithreading, usually, the performance gains is not that great.

This is due to the fact of GIL, or the global interpreter lock(GIL). This lock is global to all the threads running under a single process, so any threads if it tries to access a resource is allowed only when no other thread is accessing. 

So even though our application uses multi-threading, behind the scenes, the bottle-neck is using the GIL which makes all the tasks run cooperative-multi-tasked way. This means that only one thread can access the resource(disk I/O, CPU cores and so on) at a time, and multi-reads cannot happen, at the same time.

If our application requires I/O work more than CPU intensive work, we can expect to see that multi-threading works like a charm. But if we want to leverage CPU intensive task in a thread, we wont notice much difference, in fact some delay might happen dut to overhead.

