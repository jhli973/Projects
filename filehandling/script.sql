

SELECT ID, NAME, BirthDate
FROM LiveDb.dbo.Person

SELECT PersonID, EmployeeName, EmployeeID
FROM LiveDb.dbo.Employee e
JOIN LiveDb.dbo.Person p
ON e.PersonID = p.ID




SELECT ID, NAME, BirthDate
FROM [DatabaseName].dbo.Person

SELECT PersonID, EmployeeName, EmployeeID
FROM [DatabaseName].dbo.Employee e
JOIN [DatabaseName].dbo.Person p
ON e.PersonID = p.ID


