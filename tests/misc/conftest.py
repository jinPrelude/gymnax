def pytest_generate_tests(metafunc):
    if "env_name" in metafunc.fixturenames:
        if metafunc.config.getoption("all"):
            metafunc.parametrize(
                "env_name",
                [
                    "BernoulliBandit-misc",
                    "GaussianBandit-misc",
                    "FourRooms-misc",
                    "MetaMaze-misc",
                    "PointRobot-misc",
                ],
            )
        else:
            metafunc.parametrize("env_name", ["PointRobot-misc"])
