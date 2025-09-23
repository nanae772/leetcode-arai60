# 正規表現を使わない解法
class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        def normalize_address(email: str) -> str:
            local_name, domain_name = email.split("@")
            if (first_plus_index := local_name.find("+")) >= 0:
                local_name = local_name[:first_plus_index]
            local_name = local_name.replace(".", "")
            return f"{local_name}@{domain_name}"

        unique_addresses = set()
        for email in emails:
            unique_address = normalize_address(email)
            unique_addresses.add(unique_address)
        return len(unique_addresses)
