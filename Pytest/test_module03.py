def test_read_global(shared_datadir):
    contents = (shared_datadir / 'testcase1.txt').read_text()
    assert contents == '1\n'

def test_read_module(datadir):
    contents = (datadir / 'testcase2.txt').read_text()
    assert contents == '2\n'
