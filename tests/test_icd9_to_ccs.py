def test_import():
    from icdmappings.mappers import ICD9toCCS
    return

def test_init():
    from icdmappings.mappers import ICD9toCCS
    mapper = ICD9toCCS()
    return 

def test_mapper():
    from icdmappings.mappers import ICD9toCCS
    mapper = ICD9toCCS()

    code = ""
    expected = None
    result = mapper.map(code)
    assert result is expected

    code = "123.45"
    expected = None
    result = mapper.map(code)
    assert result == expected

    code = "5352"
    expected = "140"
    result = mapper.map(code)
    assert result == expected

    code = 2.45
    expected = None
    result = mapper.map(code)
    assert result is expected

    code = ["20104",123, "4339", "", "918283818"]
    expected = ["37", None, "110", None, None]
    result = mapper.map(code)
    assert result == expected