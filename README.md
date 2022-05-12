
# Gazu event watcher

Service used to listen for gazu events and dispatch them to event bus.


## Acknowledgements

 - [Gazu](https://pypi.org/project/gazu/)
 - [Gazu events](https://gazu.cg-wire.com/events.html)


## Installation

Install with pip

```bash
  python -m pip install requirements.txt
```
    
## Deployment

To deploy this project run

```bash
  docker build -t sg-listener .
  docker run --name sg_listener -v "/d/projects/sg_watcher:/app" sg-listener
```


## Usage/Examples

```bash

python -m main
```

