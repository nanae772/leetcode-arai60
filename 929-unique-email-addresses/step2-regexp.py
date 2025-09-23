import re

# 正規表現を使った解法


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()
        for email in emails:
            unique_email = self._normalize_email_address(email)
            if unique_email is not None:
                unique_emails.add(unique_email)
        return len(unique_emails)

    def _normalize_email_address(self, email: str) -> str | None:
        email_pattern = re.compile(r"^([a-z\.]+)(\+?[a-z\.\+]*)@([a-z\.\+]+\.com)$")
        match = email_pattern.match(email)
        if match is None:
            return None

        local_name, domain_name = match[1], match[3]
        local_name = local_name.replace(".", "")
        if not local_name:
            return None

        return f"{local_name}@{domain_name}"


def test_valid_emails():
    solver = Solution()
    assert solver._normalize_email_address("foo@bar.com") == "foo@bar.com"
    assert solver._normalize_email_address("foo.bar@baz.com") == "foobar@baz.com"
    assert solver._normalize_email_address("foo+bar@baz.com") == "foo@baz.com"


def test_invalid_emails():
    solver = Solution()
    assert solver._normalize_email_address("Foo@bar.com") is None
    assert solver._normalize_email_address("foo@bar@baz.com") is None
    assert solver._normalize_email_address("@foo.com") is None
    assert solver._normalize_email_address("foo@baz.jp") is None
    assert solver._normalize_email_address("foo@.com") is None
