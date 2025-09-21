import string

# 正規表現を使わない解法


class Solution:
    _VALID_CHARACTERS = set(string.ascii_lowercase + ".+@")

    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()
        for email in emails:
            normalized_email = self._normalize_email_address(email)
            if normalized_email is not None:
                unique_emails.add(normalized_email)
        return len(unique_emails)

    def _normalize_email_address(self, email: str) -> str | None:
        if any(ch not in self._VALID_CHARACTERS for ch in email):
            return None
        if email.count("@") != 1:
            return None

        local_name, domain_name = email.split("@")
        if (first_plus_index := local_name.find("+")) >= 0:
            local_name = local_name[:first_plus_index]
        local_name = local_name.replace(".", "")

        if not local_name or not domain_name:
            return None
        if not domain_name.endswith(".com"):
            return None
        # domain nameの.comの前に少なくとも1文字無ければいけない
        if domain_name == ".com":
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
