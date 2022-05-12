from enum import Enum

class OrganizationRole(Enum):
	CEO = "ceo"
	PRESIDENT = "president"
	MANAGER = "manager"
	STAFF = "staff"

class OrgRoleRange(Enum):
	CEO, PRESIDENT, MANAGER, STAFF = range(4)


def main()
	my_role = OrganizationRole.MANAGER
	print(my_role)
	print(my_role.value)
	
	
if __name__ = "__main__"
	main()
	
	