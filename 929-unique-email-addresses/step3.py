class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        def canonicalize_email(email: str) -> str:
            local_name, domain_name = email.split("@")
            if (first_plus_index := local_name.find("+")) >= 0:
                local_name = local_name[:first_plus_index]
            local_name = local_name.replace(".", "")
            return f"{local_name}@{domain_name}"

        unique_emails = set(canonicalize_email(email) for email in emails)
        return len(unique_emails)
