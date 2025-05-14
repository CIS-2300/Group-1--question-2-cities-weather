from src.introduction import introduction

def test_introduction_output(capsys):
    """
    Test that introduction() prints the correct welcome message.
    """
    introduction()
    captured = capsys.readouterr()
    assert "Average Comparator Program" in captured.out
    assert "Enter 3 integers" in captured.out
    assert "999 999 999" in captured.out


