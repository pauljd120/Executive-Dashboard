from exec_dash import to_usd, get_top_sellers

def test_to_usd():
    result = to_usd(50)
    assert result == "$50.00"

def test_get_top_sellers():
    
