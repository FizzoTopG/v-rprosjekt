def vinnerlag(hjemmelag: str, bortelag: str, hjemmemaal: int, bortemaal: int):
    if hjemmemaal > bortemaal:
        return hjemmelag
    if hjemmemaal == bortemaal:
        return print("uavgjort")
    if hjemmemaal < bortemaal:
        return bortelag
    


print(vinnerlag("brann", "molde", 2, 2))