"""Get available budget from Cartola team."""

import os

import utils.http

HEADERS = {"Content-Type": "application/json", "X-GLB-Token": os.getenv("GLBID")}


def handler(event, context=None):  # pylint: disable=unused-argument
    """Lambda handler."""
    res = utils.http.get("https://api.cartola.globo.com/auth/time", headers=HEADERS)
    return {"budget": res["patrimonio"]}
