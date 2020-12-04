# basic sync methods

# sync problems

## reader-writer

### simple condition

Let's first consider the simpleset scenario, the readers and writers are granted the chance to read or write the book based on the sequence they come. But multiple readers cannot read at the same time.

```c
semaphore mutex = 1;
reader () {
  while (1) {
    P(mutex);
    Read();
    V(mutex);
  }
}
writer () {
  while (1) {
    P(mutex);
    Write();
    V(mutex);
  }
}
```

### reader first

To improve the throughput of the system. Multiple readers should be able to read the book at the same time. So we use the variable `rcount` to record the number of the readers. And encapsulate the `P(mutex)` process in reader function. 

```c
semaphore write = 1;
semaphore rmutex = 1;
int rcount = 0;
reader () {
  while (1) {
    P(rmutex);
    if (rcount == 0)
      P(write);
    rcount++;
    V(rmutex);
    Read();
    P(rmutex);
    rcount--;
    if (rcount == 0)
      V(write);
    V(rmutex);
  }
}
writer () {
  while (1) {
    P(write);
    Write();
    V(write);
  }
}
```

The problem with this method is that writers are blocked if the readers keep coming.

### equal access

In contrast to the reader first, the readers that come after the previous writer should be blocked. So we use `wmutex` to achieve this goal.

```c
/* Add the following stuff */
semaphore readable = 1; // mark if there is alreay a writer
reader () {
  while (1) {
    P(readable);
    ~~~
    V(readable);
    ~~~
  }
}
writer () {
  while (1) {
    P(readable);
    ~~~
    V(readable);
  }
}
```

### writer first

We follow the same idea to grant the higher priority to the writer.

```c
/* add the following stuff */
semaphore wmutex = 1;
int wcount = 0;
/* reader is the same as equal access */
writer () {
  while (1) {
    P(rmutex);
    if (wcount == 0)
      P(readable);
    wcount++;
    V(rmutex);
    P(write);
    Writer();
    V(write);
    P(wmutex);
    wcount--;
    if (wcount == 0)
      V(readable);
    V((wmutex);
  }
}
```
