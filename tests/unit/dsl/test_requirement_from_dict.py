from strictdoc.backend.dsl.models.document import Document
from strictdoc.backend.dsl.models.requirement import requirement_from_dict


def test_010_full_dict():
    requirement_dict = {
        "TITLE": "REQ TITLE",
        "STATEMENT": "REQ STATEMENT",
        "UID": "ABC-123",
        "RATIONALE": "REQ RATIONALE",
    }
    document = Document(None, "NONAME", None, [], [])
    requirement = requirement_from_dict(requirement_dict, document, 1)

    assert requirement.ng_level == 1
    assert requirement.uid == requirement_dict["UID"]
    assert requirement.title == requirement_dict["TITLE"]
    assert requirement.statement_multiline == requirement_dict["STATEMENT"]
    assert requirement.rationale_multiline == requirement_dict["RATIONALE"]


def test_020_empty_dict():
    requirement_dict = {}
    document = Document(None, "NONAME", None, [], [])
    requirement = requirement_from_dict(requirement_dict, document, 1)

    assert requirement.ng_level == 1
    assert requirement.uid is None
    assert requirement.title is None
    assert requirement.statement_multiline is None
    assert requirement.rationale_multiline is None
