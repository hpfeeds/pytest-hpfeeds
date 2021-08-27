from _pytest.pytester import Pytester


def test_client(pytester: Pytester):
    pytester.makepyfile(
        test_hpfeeds_connection="\n".join(
            (
                "async def test_1(hpfeeds_client):",
                "    hpfeeds_client.subscribe('test')",
                "    hpfeeds_client.publish('test', 'hello')",
                "    assert await hpfeeds_client.read() == (",
                "        'test', 'test', b'hello')",
            )
        )
    )
    result = pytester.runpytest()
    result.assert_outcomes(passed=1, errors=0)


def test_hpfeeds_environment(pytester: Pytester):
    pytester.makepyfile(
        test_hpfeeds_connection="\n".join(
            (
                "import pytest",
                "",
                "@pytest.fixture()",
                "def hpfeeds_broker_channels():",
                "    return ['mychannel']",
                "",
                "async def test_1(hpfeeds_client):",
                "    hpfeeds_client.subscribe('mychannel')",
                "    hpfeeds_client.publish('mychannel', 'hello')",
                "    assert await hpfeeds_client.read() == (",
                "        'test', 'mychannel', b'hello')",
            )
        )
    )
    result = pytester.runpytest()
    result.assert_outcomes(passed=1, errors=0)
