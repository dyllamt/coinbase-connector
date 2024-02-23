import json

from coinbase.utils import run_script


def test_messages_in_topic(kubernetes_services):
    # executes kafka listener on a broker node
    out, err = run_script("scripts/test-consumer.sh")

    # checks for any issues running the kafka listener
    assert not err

    # checks that there are valid json messages
    res = [json.loads(i) for i in out.strip().split("\n")]
    assert res[0]["type"] == "ticker"
