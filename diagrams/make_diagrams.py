"""Create README.md overview diagram."""

# pylint: disable=expression-not-assigned

import os

from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.integration import StepFunctions
from diagrams.custom import Custom


THIS_DIR = os.path.dirname(__file__)
ICONS_DIR = os.path.join(THIS_DIR, "icons")


with Diagram(
    filename=os.path.join(THIS_DIR, "architecture"),
    show=False,
    curvestyle="curved",
):
    cartola = Custom("/auth/time", os.path.join(ICONS_DIR, "cartola.png"))
    cartola_salvar = Custom("/auth/time/salvar", os.path.join(ICONS_DIR, "cartola.png"))

    with Cluster("Step Function"):
        (
            cartola
            >> Edge(label="get")
            >> Lambda("budget")
            >> StepFunctions("draft")
            >> Lambda("submit")
            >> Edge(label="post")
            >> cartola_salvar
        )
