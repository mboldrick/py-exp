from dbfread import DBF


filename = "2011dbf/11CUST.DBF"

#
table = DBF(filename, load=True)
print(table.field_names)
print(f"Type(table): {type(table)}")
print(f"Number of records: {len(table)}")

"""
Load content of a DBF file into a Pandas data frame.

The iter() is required because Pandas doesn't detect that the DBF
object is iterable.
"""
# from dbfread import DBF
# from pandas import DataFrame

# dbf = DBF('files/people.dbf')
# frame = DataFrame(iter(dbf))

# print(frame)
