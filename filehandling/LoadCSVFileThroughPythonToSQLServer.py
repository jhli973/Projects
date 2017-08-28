"""
This program includes two parts:
Part 1 is to stream line the process from reading, processing and analysis file from a folder
Basically is to find files from bar module
Part 2 is to demo how to connect SQL servers with pyodbc driver
""" 

#Part one: read and process files with python
import os
import glob
import csv
import ast
import sys
import pyodbc
import time


###Read all files into a file

###insert data into the table





start_time = time.time()
path = r'D:'
os.chdir(path)
with open("SourceTableFile.csv", "r") as inputfile:
    filereader = csv.reader(inputfile, delimiter = ',')
    connection_str = """
    Driver={SQL Server Native Client 11.0};
    Server=localhost;
    Database=Test;
    Trusted_Connection=yes;
    """
    db_connection = pyodbc.connect(connection_str)
    db_connection.autocommit = True
    db_cursor = db_connection.cursor()
    cnt = 0
    for row in filereader:
        cnt += 1
        if row[0] != 'SourceID':

            col1 = row[0]
            col2 = row[1]
            col3 = row[2]
            col4 = row[3]
            col5 = row[4]
            col6 = row[5]
            col7 = row[6]
            col8 = row[7]
            col9 = row[8]
            col10 = row[9]
            col11 = row[10]
            col12 = row[11]
            col13 = row[12]
            col14 = row[13]
            col15 = row[14]
            col16 = row[15]
            col17 = row[16]
            col18 = row[17]
            col19 = row[18]
            col20 = row[19]
            col21 = row[20]
            col22 = row[21]
            col23 = row[22]
            col24 = row[23]
            col25 = row[24]
            col26 = row[25]
            col27 = row[26]
            col28 = row[27]
            col29 = row[28]
            col30 = row[29]
            col31 = row[30]
            col32 = row[31]
            col33 = row[32]
            col34 = row[33]
            sql_command = ("""INSERT INTO TargetTable (SourceID, VisitID, Vendor_UnvUserID,RowUpdateDateTime,IsPrimaryCareVendor,
            IsAdmittingVendor,IsAttendingVendor,IsEmergencyVendor,IsOtherVendor,IsFamilyVendor,IsConsultVendor,IsReferringVendor,
            FreeTextVendorAddress1,FreeTextVendorAddress2,FreeTextVendorCity,FreeTextVendorState_MisStateProvID,FreeTextVendorZip,
            FreeTextVendorEmail,FreeTextVendorPhone,FreeTextVendorFacsimile,FreeTextVendorNpiNumber,FreeTextVendorLicense,
            FreeTextNameFlag,IsVisitVendor,FreeTextCareCommentsZold,AdmitVendorCareTeamComment,PrimaryCareVendorCareTeamComment,
            AttendVendorCareTeamComment,EmergencyVendorCareTeamComment,FamilyVendorCareTeamComment,OtherVendorCareTeamComment,
            ReferringVendorCareTeamComment,FreeTextVendorNumber,IsSupervisingVendor) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""")	
            Values = [col1, col2, col3, col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24,col25,col26,col27,col28,col29,col30,col31,col32,col33,col34] 
            try: 
                db_cursor.execute(sql_command,Values) 
            except:
                print(row)
            
    db_cursor.close()
    del db_cursor
    db_connection.close()
    print("Total row" + str(cnt))
##============================

print("--- %s seconds ---" % (time.time() - start_time))
###create a table
'''
sql_command =   """
CREATE TABLE [dbo].[TargetTable](
	[SourceID] [varchar](3) NOT NULL,
	[VisitID] [varchar](30) NOT NULL,
	[Vendor_UnvUserID] [varchar](82) NOT NULL,
	[RowUpdateDateTime] [datetime] NULL,
	[IsPrimaryCareVendor] [varchar](30)  NULL,
	[IsAdmittingVendor] [varchar](2)  NULL,
	[IsAttendingVendor] [varchar](2)  NULL,
	[IsEmergencyVendor] [varchar](2)  NULL,
	[IsOtherVendor] [varchar](2)  NULL,
	[IsFamilyVendor] [varchar](2)  NULL,
	[IsConsultVendor] [varchar](3)  NULL,
	[IsReferringVendor] [varchar](3)  NULL,
	[FreeTextVendorAddress1] [varchar](45)  NULL,
	[FreeTextVendorAddress2] [varchar](45)  NULL,
	[FreeTextVendorCity] [varchar](45)  NULL,
	[FreeTextVendorState_MisStateProvID] [varchar](30)  NULL,
	[FreeTextVendorZip] [varchar](15)  NULL,
	[FreeTextVendorEmail] [varchar](92)  NULL,
	[FreeTextVendorPhone] [varchar](92)  NULL,
	[FreeTextVendorFacsimile] [varchar](40)  NULL,
	[FreeTextVendorNpiNumber] [varchar](36)  NULL,
	[FreeTextVendorLicense] [varchar](23)  NULL,
	[FreeTextNameFlag] [varchar](45)  NULL,
	[IsVisitVendor] [varchar](45)  NULL,
	[FreeTextCareCommentsZold] [varchar](45)  NULL,
	[AdmitVendorCareTeamComment] [varchar](45)  NULL,
	[PrimaryCareVendorCareTeamComment] [varchar](45)  NULL,
	[AttendVendorCareTeamComment] [varchar](45)  NULL,
	[EmergencyVendorCareTeamComment] [varchar](45)  NULL,
	[FamilyVendorCareTeamComment] [varchar](45)  NULL,
	[OtherVendorCareTeamComment] [varchar](45)  NULL,
	[ReferringVendorCareTeamComment] [varchar](45)  NULL,
	[FreeTextVendorNumber] [varchar](23)  NULL,
	[IsSupervisingVendor] [varchar](3)  NULL
) ON [PRIMARY]

"""

'''