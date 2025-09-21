import re

# 正規表現を使った解法


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        def normalize_address(email: str) -> str:
            email_pattern = re.compile(r"^([a-z\.]+)(\+?[a-z\.\+]*)@([a-z\.\+]+)$")
            match = email_pattern.match(email)
            local_name, domain_name = match[1], match[3]
            local_name = local_name.replace(".", "")
            return f"{local_name}@{domain_name}"

        unique_addresses = set()
        for email in emails:
            unique_address = normalize_address(email)
            unique_addresses.add(unique_address)
        return len(unique_addresses)
