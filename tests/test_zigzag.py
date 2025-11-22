import time

from zigzag import run_zigzag


def test_run_zigzag_prints_count(monkeypatch, capsys):
    # Avoid actually sleeping in tests
    monkeypatch.setattr(time, "sleep", lambda x: None)

    # Run with small count; should print exactly `count` lines
    run_zigzag(width=5, speed=0.01, char="X", count=3)
    captured = capsys.readouterr()
    lines = [l for l in captured.out.splitlines() if l.strip()]
    assert len(lines) == 3
