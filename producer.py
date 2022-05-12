from pprint import pprint

from shotgunEventDaemon import Engine
from shotgunEventDaemon import _getConfigPath

app = Engine(_getConfigPath())

print(app.config.getShotgunURL())
print(app.config.getEngineScriptName())
print(app.config.getEngineScriptKey())

if __name__ == "__main__":
    app.start()
