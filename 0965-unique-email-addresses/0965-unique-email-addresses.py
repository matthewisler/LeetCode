class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.replace(".", "")
            local = local.split("+")
            local = local[0]
            ans.add(f"{local}@{domain}")
        return len(ans)