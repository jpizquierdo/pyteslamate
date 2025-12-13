"""Smoke test for package distribution."""


def test_import() -> None:
    """Verify package can be imported."""
    import pyteslamate

    assert pyteslamate is not None


def test_version() -> None:
    """Verify version is accessible."""
    from pyteslamate import __version__

    assert isinstance(__version__, str)
    assert len(__version__) > 0


def test_basic_functionality() -> None:
    """Verify core feature works."""
    from pyteslamate import Teslamate

    result = Teslamate(base_url="https://api.example.com", api_key="test")
    assert result is not None


if __name__ == "__main__":
    test_import()
    test_version()
    test_basic_functionality()
    print("✓ All smoke tests passed")
