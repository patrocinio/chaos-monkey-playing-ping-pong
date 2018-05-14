# chaos-monkey-playing-ping-pong
Study on Kubernetes resilience using Chaos Monkey and a Ping Pong application

## Running this application

First, clone this repository:

```
git clone git@github.ibm.com:eduardop/chaos-monkey-playing-ping-pong.git
cd chaos-monkey-playing-ping-pong
```

Now all the scripts are the `scripts/` directory, so you need to it to your PATH:

```
cd scripts
export PATH=$PATH:`pwd`
```

To play the first game, you need to switch to the Game-1 directory:

```
cd ../Game-1
```

Notice that the scripts need to run under one of the `Game-` directory. That's why you need to add the `scripts/` to the PATH, so that you can run under the `Game-` directory.

Now, open file `Game1-Steps` and
follow the steps there.

To play the second game, do:
 
 ```
cd ../Game-2
 ```
 
and so on


