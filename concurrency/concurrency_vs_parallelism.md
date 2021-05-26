# Concurrency Vs Parallelism

Concurrency and Parallelism are often confused to refer to the ability of a system to run multiple distinct programs at the same time.

## Serial Execution

When programs are serially executed, all the instructions are run one after the other.


## Concurrency and Parallelism

* A concurrent program is one which can be disposed off into multiple parts and can be run irrespective of the order, without changing the order of outcome.
* A concurrent system can run multiple parts of the code one after the other. For example, a waiter once takes an order for customer A, can take order for customer B, without waiting for completion of order of customer A.
* Parallelism implies you can run multiple copies of the same program at the same time. This means creating program stack for each instance, which might have some overhead.
* Note that concurrency does not implies paralellism - 
  * Let's imagine an instance, where we have 1 waiter and 1 chef cooking food and 3 customers making orders.
  *  Note that a waiter can take orders from multiple people, if he his required to wait for a customer. The waiter can simply let the customer A choose the order, while it caters to other customers. Note that the behaviour of waiter is **non-blocking**, which is an important fact to note. 
  *  The chef is however, a **blocking** worker which means, that once it starts preparing a order, it cannot stop midway, and needs to complete it before it moves on with the next dish.

> Here is a table for ordering for every customer, and the time taken to prepare the dish.
 
| Customer   |Time for Taking an Order|Time for preparing an Order| 
|---|---|---|
|A|2m|5m|   |   
|B|5m|6m|   |   
|C|7m|4m|   |

Note that **taking order** and **preparing order** are not dependent on each other, i.e. taking order 1 and preparing order 2 has no relation with each other.

Lets calculate the time taken for serving all customers using Synchronised manner, Concurrent and Parallelism.

| Execution Paradigm   |Ordering of timestamp|Total time(minutes)| 
|---|---|---|
|Synchronous|`(2 + 5) + (5 + 6) + (7 + 4)`|`29mins`|   
|Parallel|`max((2+5), (5+6), (7+4))`|`11mins`|   
|Concurrent|`(2 + 5) + (6) + (4)`|`17mins`|

* You can see that synchronus paradigm takes the most time, the waiter caters one customer and is stuck with that customer unless the order is prepared. We certainly dont benefit from the non-blocking nature of the waiter.
* For Parallel, we mean that we have `3 * 1` waiters, and `3 * 1` chefs, so the max time taken is total time taken to serve all the customers. This is as efficient as it can be.
* For concurrent, we also mean ***cooperative multitasking***, which means the cooperative nature of waiter, which has a non-blocking behaviour, and helps us speed up the task. The waiter picks up all the task inorder of the first customer that reverts with the order. It is not stuck with one customer, and it can also cater to other customer, once it shares the menu among the other customers. The only bottleneck is the chef, as it can only prepare one dish at a time. So we are blocked, and cannot switch to other dish.





