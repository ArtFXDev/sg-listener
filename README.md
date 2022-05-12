
# Shotgrid event watcher

Service used to listen for Shotgrid events and dispatch them to event bus.


## Acknowledgements

 - [shotgrid](https://developer.shotgridsoftware.com/python-api/)
 - [Shotgrid events](https://github.com/shotgunsoftware/shotgunEvents)


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

