"""Cartola bot."""

import os

import utils.http

HEADERS = {"Content-Type": "application/json", "X-GLB-Token": os.getenv("13d54bb7aa90f3715dbdc0b53bb38287b3056756335656a4e7a415a62477738394761754e55534b584a566a714d4d32717953583566705376784955394e5f65425830355769497657696453433467516e396b3255502d384d4957642d5134346970366c6d65673d3d3a303a73696c76612e76697267696c696f")}

POSITION = {
    "goalkeeper": "1",
    "fullback": "2",
    "defender": "3",
    "midfielder": "4",
    "forward": "5",
    "coach": "6",
}


def handler(event, context=None):  # pylint: disable=unused-argument
    """Lambda handler."""
    body = {
        "esquema": 3,  # 433
        "atletas": [p["id"] for p in event["players"]],
        "capitao": max(event["players"], key=lambda p: p["points"])["id"],
        "reservas": {POSITION[p["position"]]: p["id"] for p in event["bench"]},
    }
    res = utils.http.post(
        "https://api.cartola.globo.com/auth/time/salvar",
        body=body,
        headers=HEADERS,
    )
    if "problema" in res["mensagem"]:
        raise ValueError(res["mensagem"])
    return res
