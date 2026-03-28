_store: dict = {
    "contacts": {},  
    "drafts": [],
}

def get_store() -> dict:
    return _store