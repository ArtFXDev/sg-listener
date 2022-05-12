import os
from pprint import pprint


def registerCallbacks(reg):
    script_name = os.environ["SG_ED_SCRIPT_NAME"]
    script_key = os.environ["SG_ED_API_KEY"]

    reg.registerCallback(
        script_name,
        script_key,
        init_entity,
        {"Shotgun_Asset_Change": None},
    )
    reg.logger.debug("Registered callback.")


def init_entity(sg, logger, event, args):
    pprint(locals())
