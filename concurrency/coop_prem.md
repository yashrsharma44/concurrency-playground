# Multitasking Variants

A system can achieve concurrency by using one of the multitasking models.
* Pre-emptive Multitasking
* Co-operative Multitasking

## Preemptive Multitasking

In preemptive multitasking, the operating system preempts a program to allow another waiting task to run on the CPU.

## Cooperative Multitasking

Cooperative Multitasking involves well-behaved programs voluntarily giving up control back to the scheduler so that another program can run.

The Linux OS uses Cooperative Multi-tasking for running processes.
Since the cooperative multi-tasking requires the application to yield the execution to the scheduler, so that other program could run. This has a flaw, where a malicious program can bring an entire system down, which is not we want.
