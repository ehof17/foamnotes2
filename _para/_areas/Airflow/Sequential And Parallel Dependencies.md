### Sequence only what must wait

When to sequence if you need to:
- wait for a shared result
- order a shared resource
- stop work after a failure 


When to not sequence:
- sequence independent inputs
- block available concurrency
- bypass an intentional join

> A worflow can be split into several paths and come back together again
### Expose fan-out and fan-in

- Source task supplies input that later task needs
Fan out, several tasks depend on the same earlier task.
Once it wins, they can run at the same time if enough capacity is available

Fan in, one task depends on several earlier tasks
- Like publishing may need 2 checks to finish
- Both checks must succeed before publishing can start

Graph view can show Connections

